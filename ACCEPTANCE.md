# Cross-client acceptance checklist

The public endpoint is `https://pressbox.com/mcp`. Expected tools:

- `search_pressbox_news`
- `get_pressbox_release`
- `latest_pressbox_news`
- `get_pressbox_newsroom`
- `get_pressbox_public_capabilities`

For each client, record its version/product, account eligibility, date and result:

1. Add the public connection using documented settings.
2. Discover exactly the expected read-only tools.
3. Search for published news and retrieve one returned release.
4. Confirm the result includes the original Pressbox source URL and attributes issuer claims.
5. Verify no private-workspace, sending or payment tools are offered.
6. Disconnect, reconnect and repeat a read-only request.

Keep the evidence levels distinct: configuration prepared; live server contract checked; actual client tool use passed; directory approval confirmed. None establishes organic citations in unrelated answers.

For a future private connection, separately test verified-email sign-in, per-user workspace boundaries, token expiry/revocation and reconnect. Never put passwords or tokens into evidence files. An unrecognized client cannot be approved merely because public discovery works.

Current actual-model acceptance remains the three bounded Antigravity tests described in the repository README. Perplexity, Copilot Studio, Grok API and consumer Gemini acceptance remain outstanding until their real clients are tested.

Live server contract checked on 25 October 2026: all five public tools discovered with read-only annotations; published search/retrieval and a real public newsroom passed. This is transport evidence, not acceptance in each external client.
