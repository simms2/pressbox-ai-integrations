---
name: pressbox-release-readiness
description: Help prepare and fact-check a user-approved press release before any Pressbox publication; activate for press-release readiness, factual checks and final approval workflows.
---

# Press release review before publishing

This skill is **preparation**, not permission to publish. It applies to material that the user has supplied or expressly authorised for use.

## Verify the source material
- Identify issuer, announcement, actual news event, supporting sources, dates, place, public contact details and image rights from user-provided facts.
- Flag missing or unsupported metrics, quotations, claims, statistics, legal assertions and promotional superlatives. Never invent facts to achieve a quality score.
- Remove or highlight unfilled placeholders such as `[launch date]` or `[confirmed opening date]`; ask for real approved replacements.
- Check for near-identical duplicate announcements and recommend one canonical story where appropriate.
- Differentiate headline/summary/body and cite external links when the user supplies them. The issuer remains responsible for accuracy.

## Preparation and authority
- Draft a factual release and show the exact text, intended issuer and planned public URL/workspace only if retrieved from real Pressbox tools.
- Drafting in Claude is local: it does not automatically make the text public or send it to Pressbox.
- If the user specifically wants a Pressbox tool to validate, ensure the authenticated `pressbox` MCP connection is linked to the correct user/workspace, then use the nonpersistent `validate_press_release` or `prepare_press_release_draft`.
- Before `submit_press_release` or `schedule_press_release`, show final text, approved source facts, exact workspace and publication time if scheduled; obtain explicit user approval and submitter-responsibility acceptance. Never assume consent from general brainstorming or an earlier unrelated turn.
- A retry after an uncertain publication result must first check whether the release was created, to prevent duplicates.
- If the user lacks an entitlement, explain available authorised actions neutrally; do not sell digital services or generate checkout URLs inside this plugin.

## Boundaries
- Current public News Wire tools are read-only. They cannot publish or provide private workspaces.
- Distribution preparation is **not** sending. Outbound journalist sending and checkout are not enabled in this release; never attempt to work around these controls.
- Preserve image rights, lawful-basis requirements, suppression rules, no bulk journalist email exports and Pressbox's server-enforced approvals.
- Report only confirmed publication, notification, delivery, coverage and citation outcomes, distinguishing them from each other.
