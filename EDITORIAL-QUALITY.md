# Editorial quality checks for authenticated clients

Verified against the Pressbox production policy on 25 October 2026. This is guidance for clients that already expose the relevant Pressbox tools; it does not grant additional access.

## Beta publication standard

The minimum automated quality score is **70/100**. The body must describe an actual announcement, provide specific supporting detail and contain at least 100 substantive words outside recognised company boilerplate. A headline containing “launches” or “expands” is insufficient when the body is only a standing company description.

Concrete product functionality can support a launch without a numerical metric. A quotation, website or separate location field is not always required to pass. Never invent a number, quotation, date or claim just to raise the score. Automated overall scores are capped at 95; this is not a fact-check or guarantee of editorial coverage.

## Handle review results correctly

If the client already has `prepare_press_release_draft` or `validate_press_release`, use that tool before asking for publication approval. These review tools do not save the release or consume a publication allowance.

Read **`assessment.decision`**, not only `valid`. `validate_press_release` can return `valid: true` for correctly formatted fields while the assessment still says `revise` or `block`. Only `assessment.decision: "accept"` indicates the current automated gate passed. The preparation response also reports `ready_to_submit`.

For `revise`, retain the user's copy and explain the relevant `reasons` and `suggestions`. Ask for missing facts or revise with facts already supplied. For `block`, explain the feedback; do not repeatedly retry unchanged copy, fabricate supporting evidence or alter client-side scores. Passing review still requires the existing user's explicit publication approval and workspace entitlement. Publication is separate from journalist sending or purchases.

Pressbox rechecks current content at final publication and before previously approved automated schedules run. An older passing result is not a permanent exemption. Previously published articles are not automatically withdrawn by this policy.

## Respect the client's tool limits

The supplied Antigravity starter exposes only three account/workspace read tools. It does **not** expose release preparation or publication. Do not expand its allowlist, obtain new grants or run extra model calls because this guide describes other server tools. The public News Wire is read-only and cannot review or submit drafts.

Suggested future acceptance cases: a concise factual announcement; a profile with a news-style headline but no new event; a detailed product launch without numerical claims; and an invalid draft that stays editable without consuming allowance. These are a checklist, not a statement that new model tests ran. Use the existing [acceptance checklist](ACCEPTANCE.md) and obtain any additional test or write authorization required.
