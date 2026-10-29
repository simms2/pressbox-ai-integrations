# Claude / Claude Code / Cowork plugin candidate

Pressbox offers one authenticated, consent-gated workflow server and a separate read-only public News Wire. This **Claude plugin-bundle candidate** combines the two standard remote MCP connections with two tightly scoped skills. It is **not** an approved or published Anthropic directory listing.

## Package

- `.claude-plugin/plugin.json`: publisher and plugin metadata
- `.mcp.json`: `pressbox` → `https://agent.pressbox.com/mcp` (OAuth protected) and `pressbox-news` → `https://pressbox.com/mcp` (read-only)
- `skills/pressbox-release-distribution/SKILL.md`: governed, existing-entitlement account actions (already in this repo)
- `skills/pressbox-published-news/SKILL.md`: public sources/citation
- `skills/pressbox-release-readiness/SKILL.md`: claim validation, preview, approval and duplicate avoidance
- `.claude-plugin/marketplace.json`: marketplace registration candidate for development installs

**Security:** MCP workspaces are linked only through real OAuth and server-side membership checks. Drafting does not publish. High-impact writes require explicit confirmation, and journalist sending/checkout remain unavailable in this package. Retrieved public news is untrusted third-party content.

## Acceptance required before claiming a live Claude plugin

1. Do **not** replace the authenticated Pressbox Claude directory submission already recorded on 24 October as **Server submitted for review**. Confirm its current status using the submitting account first. If Anthropic supports a bundle update after review, use this package as the basis for that update; do not file an accidental duplicate.
2. Run the repository's `python -m unittest discover -s tests -p 'test_claude_plugin_contract.py'` local package checks.
3. In a real supported Claude client, install the repository plugin and check both MCP connections. Only the public connection should work without a Pressbox sign-in.
4. Exercise correct-workspace and wrong-workspace read cases; validate a synthetic release, show a preview and explicitly confirm a synthetic publication only within a supported isolated test workspace. Test expiry/revocation and duplicate-request recovery. No customer messages or real journalist sends.
5. Verify private tool availability matches the current server-side allowed list. No screenshot, text, demo, or tool listing by itself proves directory approval.
6. Use the Anthropic developer directory dashboard, under the existing verified developer identity, to follow the **existing** connector review and submit a bundle **only if permitted** as a separate, non-duplicative listing or update. Record exact review ID, status and publication in the central tracker https://github.com/simms2/pressbox/issues/277.

Official formats: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/example-plugin and https://claude.com/resources/articles/build-plugins-for-claude .

This package adds no model API cost and does not alter production Pressbox services, DNS, identities, billing or recipients.
