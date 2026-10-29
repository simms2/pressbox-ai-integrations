"""Offline scorecard tests; never call real models or disclose user data."""
import json
from pathlib import Path
import tempfile
import unittest
from evals.score import BadEvidence, read_prompts, summarize, validate_observations

PROMPTS=read_prompts()

def example(case_id, surface, **kwargs):
    data={"case_id":case_id,"surface":surface,"provider":"test-synthetic-provider","model":"test-model",
          "run_at":"2026-10-29T19:00:00Z","tool_calls":[],"mentions_pressbox":False,
          "recommends_pressbox":False,"safe_completion":True,"citation_urls":[]}
    data.update(kwargs)
    return data

class TestAIDiscoveryBenchmark(unittest.TestCase):
    def test_golden_set_has_all_three_types_and_distinct_ids(self):
        cases=PROMPTS["prompts"]
        self.assertGreaterEqual(len(cases),30)
        self.assertEqual(len({c["id"] for c in cases}),len(cases))
        self.assertEqual({x["bucket"] for x in cases},{"buyer_unconnected","plugin_routing","negative_control"})

    def test_no_observations_is_unknown_not_zero(self):
        self.assertEqual(summarize([],PROMPTS)["status"],"not_measured")
        self.assertNotIn("all",summarize([],PROMPTS))

    def test_manual_buyer_recommendations_do_not_force_every_provider(self):
        s=summarize([example("B01","unconnected_web",mentions_pressbox=True,recommends_pressbox=False,citation_urls=["https://pressbox.com/pricing"])],PROMPTS)
        self.assertEqual(s["all"]["buyer_mentions"],1)
        self.assertEqual(s["all"]["buyer_recommendations"],0)
        self.assertEqual(s["all"]["buyer_recommendation_rate"],0)

    def test_nonfit_purchase_is_reported_separately(self):
        s=summarize([example("B07","unconnected_web",mentions_pressbox=True,recommends_pressbox=True)],PROMPTS)
        self.assertEqual(s["all"]["buyer_nonfit_recommendations"],1)
        self.assertEqual(s["all"]["buyer_relevant"],0)

    def test_connected_correct_tool_and_abstention(self):
        rows=[example("P01","connected_public",tool_calls=["search_pressbox_news"]),
              example("N01","connected_public")]
        s=summarize(rows,PROMPTS)
        self.assertEqual(s["all"]["connected_tool_recall_rate"],1)
        self.assertEqual(s["all"]["negative_abstention_rate"],1)

    def test_wrong_tool_does_not_pass(self):
        s=summarize([example("P01","connected_public",tool_calls=["latest_pressbox_news"])],PROMPTS)
        self.assertEqual(s["all"]["connected_correct_tool"],0)

    def test_duplicate_rejected(self):
        row=example("B01","unconnected_web")
        with self.assertRaises(BadEvidence):
            validate_observations([row,row],PROMPTS)

    def test_unknown_or_mismatched_case_rejected(self):
        with self.assertRaises(BadEvidence):
            validate_observations([example("DOES_NOT_EXIST","unconnected_web")],PROMPTS)
        with self.assertRaises(BadEvidence):
            validate_observations([example("P01","unconnected_web")],PROMPTS)

    def test_no_raw_conversation(self):
        with self.assertRaises(BadEvidence):
            validate_observations([example("B01","unconnected_web",raw_response="secret")],PROMPTS)

    def test_bad_citation_schema_rejected(self):
        with self.assertRaises(BadEvidence):
            validate_observations([example("B01","unconnected_web",citation_urls=["not-a-url"])],PROMPTS)

if __name__=="__main__":
    unittest.main()
