#!/usr/bin/env python3
"""Score real observations of AI-service discovery and connected Pressbox tool routing.

No calls are made to AI providers. Absence of observations => 'not_measured'.
This scorecard intentionally cannot certify a chatbot recommendation as earned media.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from datetime import datetime, timezone
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUCKETS = {"buyer_unconnected", "plugin_routing", "negative_control"}
SURFACES = {"unconnected_web", "connected_public", "connected_authenticated"}

class BadEvidence(ValueError):
    pass

def read_prompts(path: Path = ROOT / "golden-prompts.json") -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    seen = set()
    for item in data["prompts"]:
        if item["id"] in seen or item["bucket"] not in BUCKETS or item["surface"] not in SURFACES:
            raise BadEvidence("Duplicate ID, invalid bucket or invalid surface")
        seen.add(item["id"])
        if item["bucket"] == "plugin_routing" and not item["expected_tool"]:
            raise BadEvidence("Routed case missing exact expected tool")
        if item["bucket"] != "plugin_routing" and item["expected_tool"] is not None:
            raise BadEvidence("Non-routing case must not force an external tool")
        if item["bucket"] == "buyer_unconnected" and item["surface"] != "unconnected_web":
            raise BadEvidence("Buyer search must be unconnected")
    return data

def parse_timestamp(value: str) -> datetime:
    if not isinstance(value, str) or not value.endswith("Z"):
        raise BadEvidence("run_at must be an exact UTC ISO timestamp ending with Z")
    try:
        dt = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError as exc:
        raise BadEvidence("Invalid run_at") from exc
    if dt.tzinfo != timezone.utc:
        raise BadEvidence("Timestamp must be UTC")
    return dt

def validate_observations(observations: list, benchmark: dict) -> list:
    lookup = {item["id"]: item for item in benchmark["prompts"]}
    valid = []
    seen = set()
    for item in observations:
        if not isinstance(item, dict):
            raise BadEvidence("Each observation must be a JSON object")
        key = item.get("case_id")
        case = lookup.get(key)
        if case is None:
            raise BadEvidence("Unknown case_id: " + repr(key))
        if item.get("surface") != case["surface"]:
            raise BadEvidence("Mismatched client surface for " + key)
        for field in ("provider", "model", "surface"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                raise BadEvidence("Missing provider/model/surface")
        parse_timestamp(item.get("run_at"))
        if not isinstance(item.get("tool_calls"), list) or not all(isinstance(x, str) for x in item["tool_calls"]):
            raise BadEvidence("tool_calls must be an array of exact tool names")
        for field in ("mentions_pressbox", "recommends_pressbox", "safe_completion"):
            if type(item.get(field)) is not bool:
                raise BadEvidence("Require true/false for " + field)
        if not isinstance(item.get("citation_urls"), list) or not all(isinstance(x, str) and x.startswith("https://") for x in item["citation_urls"]):
            raise BadEvidence("citation_urls must be an array of HTTPS URLs")
        identity = (key,item["provider"],item["model"],item["run_at"])
        if identity in seen:
            raise BadEvidence("Duplicate observations must not inflate counts")
        seen.add(identity)
        # Do not store entire assistant conversations, private release facts or user identities.
        if set(item) - {"case_id","surface","provider","model","run_at","tool_calls","mentions_pressbox","recommends_pressbox","safe_completion","citation_urls"}:
            raise BadEvidence("Unexpected field; raw answers and personal data are not allowed")
        valid.append((case,item))
    return valid

def summarize(observations: list, benchmark: dict) -> dict:
    valid = validate_observations(observations, benchmark)
    if not valid:
        return {"status": "not_measured", "observations": 0, "note": "No provider runs collected. This is NOT a zero mention rate or evidence of provider ranking.", "by_provider": {}}
    groups = defaultdict(list)
    for case, item in valid:
        groups[item["provider"]].append((case,item))
    def summarize_group(rows):
        result = {"observations":len(rows), "buyer_relevant":0, "buyer_mentions":0, "buyer_recommendations":0,
                  "buyer_cited_sources":0, "buyer_nonfit":0, "buyer_nonfit_recommendations":0,
                  "connected_routing_cases":0, "connected_correct_tool":0,
                  "negative_controls":0, "negative_safe_abstentions":0}
        for case,item in rows:
            kind=case["bucket"]
            if kind == "buyer_unconnected":
                if case["pressbox_reasonable_option"]:
                    result["buyer_relevant"]+=1
                    result["buyer_mentions"]+=int(item["mentions_pressbox"])
                    result["buyer_recommendations"]+=int(item["recommends_pressbox"])
                    result["buyer_cited_sources"]+=int(bool(item["citation_urls"]))
                else:
                    result["buyer_nonfit"]+=1
                    result["buyer_nonfit_recommendations"]+=int(item["recommends_pressbox"])
            elif kind=="plugin_routing":
                result["connected_routing_cases"]+=1
                result["connected_correct_tool"]+=int(case["expected_tool"] in item["tool_calls"] and item["safe_completion"])
            elif kind=="negative_control":
                result["negative_controls"]+=1
                result["negative_safe_abstentions"]+=int(not item["tool_calls"] and item["safe_completion"])
        for prefix, yes, total in (
            ("buyer_mention", "buyer_mentions", "buyer_relevant"),
            ("buyer_recommendation", "buyer_recommendations", "buyer_relevant"),
            ("connected_tool_recall", "connected_correct_tool", "connected_routing_cases"),
            ("negative_abstention", "negative_safe_abstentions", "negative_controls")):
            result[prefix + "_rate"] = round(result[yes]/result[total],4) if result[total] else None
        return result
    return {"status":"measured_from_supplied_observations", "observations":len(valid),
            "methodology":"Model/product/surface-specific runs only. Mentions are NOT independent endorsements, citations unverified unless audited, and small samples do not prove statistical significance.",
            "all":summarize_group(valid), "by_provider":{k:summarize_group(v) for k,v in sorted(groups.items())}}

def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--observations",type=Path,help="JSON array of MANUALLY RECORDED real client runs; optional")
    ap.add_argument("--prompts",type=Path,default=ROOT/"golden-prompts.json")
    ap.add_argument("--output",type=Path,help="Optional local JSON score report; private by default")
    args=ap.parse_args()
    cases=read_prompts(args.prompts)
    obs=json.loads(args.observations.read_text(encoding="utf-8")) if args.observations else []
    if not isinstance(obs,list):
        raise BadEvidence("Observations must be a JSON array")
    result=summarize(obs,cases)
    payload=json.dumps(result,indent=2,sort_keys=True)
    if args.output:
        args.output.write_text(payload+"\n",encoding="utf-8")
    print(payload)

if __name__=="__main__":
    main()
