# Pressbox AI integrations

Public setup files for the Pressbox News Wire and OAuth-protected workspace service. Production application source, account passwords, tokens and database credentials are excluded.

## Gemini through Google Antigravity

Use the [Antigravity setup guide](antigravity/README.md) for Google's current developer client. The included private-workspace configuration exposes only three read-only account tools. It was exercised with Antigravity CLI 1.4.7 and Gemini 3.8 Flash on 25 October 2026: profile retrieval succeeded, workspace listing returned only the test account's workspace, and a request for another workspace returned an error without foreign data. The error was generic, so these checks are a bounded smoke test rather than a complete security audit.

Google has [retired consumer-account Google sign-in for Gemini CLI and Code Assist](https://developers.google.com/gemini-code-assist/docs/deprecations/code-assist-individuals). Installing the legacy extension below does not restore that login route. Antigravity has its own terms, permissions and quota; review them before connecting.

These files are a manual developer setup. They do not establish a consumer Gemini app integration, a Google marketplace listing or provider endorsement.

## Public News Wire

The public, read-only MCP endpoint is `https://pressbox.com/mcp`. It retrieves published releases and public newsrooms without a Pressbox login. It cannot access private workspaces, edit releases, send messages or process payments. An [Antigravity configuration example](antigravity/public-news-wire.json) is supplied separately; this example was checked against the public server's tool definitions, but was not part of the three model tests above.

## Gemini Apps custom connection

See the [Gemini Apps eligibility and setup notes](gemini-apps/README.md) for a separate public News Wire route. Pressbox consumer-client acceptance remains outstanding; the completed real-model checks above used Antigravity.

## Legacy Gemini CLI extension

The repository root retains the Gemini CLI extension for compatible developer environments. Gemini CLI 0.65.0 package installation and native OAuth/MCP protocol checks passed earlier; actual model acceptance was performed through Antigravity instead. Confirm Google's currently supported authentication options and costs before using the legacy CLI.

```sh
gemini extensions install https://github.com/simms2/pressbox-ai-integrations
```

The protected endpoint is `https://agent.pressbox.com/mcp`. Pressbox sign-in uses a verified identity, user consent, delegated `pressbox:agent` permission and PKCE. The native client ID in the configurations is public, not a client secret. Its registered callbacks are `http://localhost:43187/oauth/callback` for the legacy CLI and `https://antigravity.google/oauth-callback` for Antigravity. Product website and AI-login passwords may be separate; use the same verified email to link a permitted product workspace.

The server checks workspace membership and object access. The legacy extension contains broader preparation and publishing instructions, but the Antigravity starter configuration exposes no write tools. Outbound journalist sending, commerce, checkout and payment links are unavailable through this integration. No bulk journalist email export is supported.

[Pressbox AI integrations](https://pressbox.com/ai) · [Support](https://pressbox.com/support) · [Privacy](https://pressbox.com/privacy) · [Terms](https://pressbox.com/terms)

## Review evidence

[Download the 80-second evidence walkthrough](https://github.com/simms2/pressbox-ai-integrations/raw/refs/heads/main/pressbox-review-walkthrough.mp4).

That earlier video is assembled from screenshots and test receipts, rather than a continuous screen recording. It contains no passwords or tokens. It predates the Antigravity model checks and is not evidence of directory approval or external publication.
