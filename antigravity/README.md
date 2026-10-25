# Connect Pressbox to Google Antigravity

Check your Pressbox account and workspaces from Gemini through Google's Antigravity developer client. This starter connection is read-only; it does not draft, publish, schedule, send or purchase anything.

## Private workspace connection

1. Install Antigravity from [Google's official instructions](https://antigravity.google/docs/getting-started/), sign in to Google and review its terms, permissions and data-use choices. Check your available quota before asking the model to work.
2. Review [mcp_config.json](mcp_config.json). Add its `pressbox` entry to your project's `.agents/mcp_config.json`. Merge it with existing server entries; do not replace other connections or copy credentials from another person.
3. Open that project in Antigravity CLI. Run `/mcp`, select `pressbox`, then choose **Authenticate**.
4. Complete the Pressbox sign-in using the same verified email as your Pressbox workspace. The consent screen may call this native application **Pressbox Gemini CLI**. It uses only `pressbox:agent`; no client secret is needed. Do not enter a Google password into the Pressbox login.
5. If the browser shows an authorization code, paste it directly into Antigravity's authorization-code field. Treat it as a password: never paste it into a chat, issue, screenshot or repository.
6. Confirm that the server shows **Authed** and only these tools: `get_my_pressbox_profile`, `list_my_workspaces`, `get_my_pressbox_entitlements`.
7. Try: “Use Pressbox to show which account and workspaces I am connected to. Do not change anything.” Review and approve individual tool calls. Keep the normal permission prompts enabled.

This configuration uses the registered public native client and Google's HTTPS callback with PKCE. It contains no access token, refresh token or client secret. Authorizing an account does not add it to another organisation: Pressbox workspace membership remains required. If your workspace is missing, check the verified email and membership rather than trying a different workspace's identifier.

Product website and Pressbox AI-login passwords can be separate. Start with your own account; the private reviewer account used for testing is not a shared customer login. To stop use, disable/remove this MCP entry in Antigravity and revoke the application's account grant through the supported account/provider controls. Removing a local configuration alone does not necessarily revoke a previously issued token.

## Published news without a private account

[public-news-wire.json](public-news-wire.json) is a separate optional configuration for `https://pressbox.com/mcp`. Merge its `pressbox_news_wire` entry into the same project configuration. It requires no Pressbox sign-in and retrieves only public releases/newsrooms. For example: “Find recent published Pressbox announcements about renewable energy and link to the original releases.”

The public example was validated against Pressbox's tool definitions. Actual Antigravity model tests in this release covered the private starter connection only. Neither connection guarantees that another user's assistant will find or cite a release.

## What was tested

On 25 October 2026, Antigravity CLI 1.4.7 displayed Gemini 3.8 Flash and included Starter quota. Three model prompts each selected and executed one Pressbox tool, with one-time approvals:

- Profile retrieval succeeded for a verified synthetic reviewer account.
- Workspace listing returned exactly its own single workspace.
- An entitlements request for a different workspace returned a generic tool error and no foreign data.

The negative check did not return a detailed permission-error code. These checks do not establish expiry/refresh behaviour, a complete isolation audit, write-workflow acceptance, consumer Gemini app availability or a Google marketplace listing. No sends, publications or purchases were performed.

[Google MCP documentation](https://antigravity.google/docs/mcp/) · [Pressbox support](https://pressbox.com/support)

For the separate consumer app, see [Gemini Apps eligibility and setup notes](../gemini-apps/README.md).
