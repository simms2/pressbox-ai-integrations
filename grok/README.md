# Pressbox with the Grok developer API

`public-news-wire-request.json` is a request-body example for xAI's Responses API. It uses only public announcements and explicitly lists the four read-only News Wire tools.

Developers supply their own xAI API key privately and review provider pricing before execution. No model call or paid API use was performed to validate this example. The server's transport and tool contract are checked separately; that is not real Grok model acceptance.

This is an API integration, not a consumer Grok app installation or directory listing. xAI currently documents that `require_approval` is unsupported, so this starter has no private or write tools and does not rely on that parameter for protection. Never substitute the private agent endpoint or an unrestricted tool list without a separate access review.

[xAI remote MCP documentation](https://docs.x.ai/developers/tools/remote-mcp)
