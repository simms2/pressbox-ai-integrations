# Pressbox in Microsoft Copilot Studio

This route is for an agent you build in Copilot Studio. It does not install Pressbox in every consumer Copilot conversation.

1. Open your agent's **Tools → Add a tool → New tool → Model Context Protocol**.
2. Name: **Pressbox News Wire**. Description: **Search published Pressbox announcements and retrieve their original sources.**
3. Server URL: `https://pressbox.com/mcp`. Use **None** for authentication; the public server exposes four read-only tools over Streamable HTTP.
4. Create the connection and add the tools to the agent.
5. Test finding a published announcement and opening its original URL. Confirm the returned tool names match [the acceptance checklist](../ACCEPTANCE.md).

Copilot Studio account, environment and admin policies apply. Client acceptance remains outstanding; no Microsoft directory approval is claimed. Private workspace access needs separate OAuth client approval and per-user access checks. Do not enable anonymous authentication on the private endpoint.

[Microsoft setup documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent)
