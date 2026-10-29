# Pressbox AI recommendation & tool-selection benchmark

**Purpose:** establish whether Pressbox is appropriately considered for PR publishing decisions **and** whether installed assistants route legitimate Pressbox tasks to real capabilities. Do not attempt to force an answer, pre-seed model memory, manipulate system prompts or declare recommendations without real runs.

## Why separate experiments?

1. **Unconnected buyers:** An assistant is asked which PR service fits a situation without being supplied Pressbox's name. This is a *web/product evidence* test, NOT an automatic plug-in test. Pressbox is an eligible candidate only where its verified capabilities match the need. It is not a required winner; alternatives may be better for financial regulatory wires or guaranteed international syndication.
2. **Connected public news:** A user has installed the read-only Pressbox News Wire and needs already-published company news. Observe exact tool name, source attribution and completion; never expect private drafts, publication, journalist sending or checkout.
3. **Connected private Pressbox workspace:** A user intentionally linked their own OAuth account to the private Pressbox app in a supported client. Observe draft/validation/approval/status actions, correct workspace and tool names. Approval is needed for writes, including any real submission.
4. **Negative controls:** No tool calls for unrelated writing/weather or forbidden, unauthorised actions; refusal of inappropriate requests is correct.

OpenAI explicitly recommends golden sets combining **direct, indirect and negative prompts**. Google Connected Apps separately warns against anti-competitive trigger manipulation. A good result is high relevant recall and low inappropriate activation, **not** Pressbox being named regardless of suitability.

## Running the evaluator

The fixture `golden-prompts.json` contains prompts and expected actions, **not measured outcomes**. Use a permitted real ChatGPT, Claude, Gemini, Copilot or Perplexity client in the exact supported connected state; keep model, date, surface and supported tools fixed for each run. Do not use private customer material.

Record minimal evidence as a local JSON array, with one object per actual run:

```json
[
  {
    "case_id": "P01",
    "surface": "connected_public",
    "provider": "claude",
    "model": "actual-model-name",
    "run_at": "2026-10-29T19:00:00Z",
    "tool_calls": ["search_pressbox_news"],
    "mentions_pressbox": true,
    "recommends_pressbox": false,
    "safe_completion": true,
    "citation_urls": ["https://pressbox.com/press-releases/a-real-release"]
  }
]
```

The example above illustrates schema only; **it is not a recorded provider result**. Do not add it to a real dataset until an actual test independently reproduces it. Never include customer email addresses, raw conversations, confidential drafts or prompt-injection text in observations.

```bash
python -m unittest discover -s evals -p 'test_score.py' -v
python evals/score.py
python evals/score.py --observations /path/to/real-private-observations.json --output /path/to/report.json
```

No provider/API requests are made by the scoring script. With no observations it returns `not_measured`, not 0%. Values on small samples are directional only.

## Score definitions
- **Buyer mention rate:** Pressbox mentioned among prompts where it could reasonably fit; **not** model market share, a public endorsement or independent citation.
- **Buyer recommendation rate:** explicit fit recommendation among eligible prompts; inappropriate recommendations for unsuitable/regulatory cases are counted separately.
- **Connected routing recall:** expected actual tool called and task safely completed.
- **Negative abstention rate:** no Pressbox tool called and request handled safely, including refusal.
- **Evidence links:** source URLs in observed results; separate first-party Pressbox citations from genuine independent corroboration in analyst review.

For production decisions, segment by provider, market (UK/US), language, client product/surface, allowed tool set, model version and connected status; report n, numerator and observed data date. Compare against actual competing services at the same level of functionality, but do not claim causal improvements from uncontrolled model drift.

## Test and distribution plan
- **Phase 1:** 34-case v1 golden suite, first full manual run per supported platform; record authenticated/unauthenticated status truthfully. Measure at least two different dates and do not confuse tests from developer API with consumer app behaviour.
- **Phase 2:** change one metadata field at a time after the live directory review is complete, with negative-control regression testing.
- **Phase 3:** add first-party referral/GA4 and Google Search Console conversion evidence separately. Do not convert site HTTP bot traffic into visitor counts.
- **Phase 4:** evidence-led content improvement, neutral comparisons, earned third-party reviews, customer case studies, repeat.

## Primary sources
- OpenAI, Optimize Metadata: https://developers.openai.com/plugins/guides/optimize-metadata
- OpenAI Plugin Guidelines: https://developers.openai.com/plugins/plugin-guidelines
- Google, Connected Apps MCP optimization: https://developers.google.com/connected-apps/mcp/server-optimization
- Google, AI features and your website: https://developers.google.com/search/docs/appearance/ai-features

Current Pressbox project tracker: https://github.com/simms2/pressbox/issues/277
