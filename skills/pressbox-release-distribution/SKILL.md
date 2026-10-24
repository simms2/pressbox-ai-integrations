---
name: pressbox-release-distribution
description: Use a connected Pressbox workspace to prepare, publish, schedule and measure press releases with existing entitlements; outbound sending is disabled.
---

# Pressbox — governed PR workflows without in-chat commerce

Use Pressbox as the execution layer for **already-entitled** press-release publication, private outreach inspection and measured outcomes in ChatGPT. Outbound journalist sending is disabled in the current production integration.

1. Identify the connected Pressbox account and workspace before a write. If several workspaces are available, clarify which one is intended. When onboarding someone new, require verified OAuth identity plus explicit Pressbox Terms/Privacy acceptance.
2. Preparation and validation are non-persistent by default. Use `prepare_press_release_draft` or `validate_press_release`; explain that validation alone does not create a release or consume a publication allowance.
3. Before `submit_press_release`, show the exact final headline, summary, key claims and selected workspace; require the user's explicit publication approval **and** responsibility acceptance. Respect the existing account's available entitlement and Pressbox's quality checks. Never retry deceptively when publishing is refused.
4. Never represent an issuer-submitted release as independently verified. Canonical Pressbox source links show what was published, not third-party news pickup or AI citations.
5. `schedule_press_release` requires the user's approval of the exact timezone-aware publication time, publication authority and responsibility. Cancellation requires a separate explicit request and `cancel_scheduled_press_release`.
6. `attach_release_media` requires legitimate image/document rights, explicit approval and alt text for applicable assets. Do not attach unauthorized material.
7. **Outbound journalist sending is currently disabled. Do not call `send_distribution_campaign`, including after a user asks or offers approval.** Explain the current restriction. Read existing list/campaign status and aggregate reports only as authorised. Draft campaign preparation never sends and requires a suitable owned published release and existing list; do not invent those resources. Do not export bulk journalist email addresses or bypass suppressions, distribution rights, verified contacts or lawful-basis controls.
8. Use `get_press_release`, `find_release_coverage`, `get_press_release_impact`, `get_distribution_campaign_status` and `get_campaign_client_report` to report only what actually happened. Association with coverage is not proof Pressbox caused it.
9. Use public `search_pressbox_news` and `search` / `fetch` for already-published release discovery, linking the original Pressbox pages and issuer attribution. A first-party retrieval does not prove a model cited the release.
10. **No digital commerce through this ChatGPT plugin.** It cannot display paid subscription catalogues, quote or sell digital PR services or credits, initiate subscription or distribution checkout, provide payment links, promote upsells or suggest another tool/site as a checkout workaround. Do not call unavailable commerce tools or invent prices.
11. If an existing account lacks the entitlement for a requested action, explain the restriction neutrally and describe eligible existing options; do not solicit a purchase or generate a checkout URL.
12. Always distinguish Pressbox publication, queued/attempted journalist email, indexing syndication and independent earned coverage. Never claim a send, listing, payment, coverage or citation unless a Pressbox result proves it.
13. When the user asks about how much they can still publish, generate, or monitor within their existing account, call `get_my_pressbox_entitlements`. Show only the current workspace's allowance and usage amounts and applicable period, never a plan catalogue, prices, payments, upgrade suggestion or checkout URL.


Reviewer sample content is synthetic and must remain private. A quality score or `ready_to_submit` result never constitutes user approval. Review scheduling tests must end with cancellation and verification that no schedule or automated publication approval remains.
