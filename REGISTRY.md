# Official MCP Registry — Pressbox News Wire

This public repository is the published metadata source for the **read-only Pressbox News Wire**:
- Registry identity: `io.github.simms2/pressbox-news-wire`
- Remote Streamable HTTP MCP: `https://pressbox.com/mcp`
- Five public tools: search, open a published release, latest news, newsroom, describe capabilities.
- It exposes **no** Pressbox account, draft, publication, journalist address, payment or outbound send tools.

`server.json` is the standard remote-only MCP metadata. The publishing workflow uses **GitHub Actions OIDC**, authenticating the `io.github.simms2/*` namespace without a PAT, secrets or DNS changes. It downloads a **pinned v1.8.1 official mcp-publisher**, verifies its Sigstore signature and source identity, validates the metadata, authenticates against the official public registry and publishes. Runs only on `main` when `server.json` or the workflow changes, or on explicit manual dispatch. This registry is currently in preview.

## Evidence and protection
A successful GitHub workflow alone proves metadata was accepted by the registry. It does not establish ChatGPT, Claude, Gemini, Microsoft, Perplexity or any specific AI model automatically recommends Pressbox. Those platforms have separate app directories, permission reviews, tool invocation behaviour and submission/approval gates, tracked in https://github.com/simms2/pressbox/issues/277 .

GitHub publishing is public and requires no user credentials at runtime. OIDC is scoped to `simms2`'s GitHub namespace. If another publisher already owns the same server name or URL, do not work around ownership checks; investigate the existing listing.

## Before changing
- Keep the public MCP URL immutable for this identity. **Do not add `https://agent.pressbox.com/mcp`** to this public read-only registry record; it has different OAuth and private workflow capabilities.
- Changing server version or tool surface merits a deliberate update and validation, not mass automation. Preserve the schema and current official release/signature checks.
- Do not declare standalone auth/payment or government/press-source authority that the public MCP does not provide.

Official docs:
https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/quickstart.mdx
https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/github-actions.mdx
