# Pressbox AI integrations

Minimal public integration files for the OAuth-protected Pressbox MCP service. Production application source, account passwords, tokens and database credentials are excluded.

## Gemini CLI candidate

This repository contains a candidate Gemini CLI extension. The official Gemini CLI 0.65.0 validates the package and installs it in an isolated test workspace. Direct native OAuth/MCP protocol acceptance has passed. Google account authentication and an actual Gemini model tool-use test remain pending. No Google gallery listing or provider endorsement is claimed.

After reviewing the files, developers can test installation with:

```sh
gemini extensions install https://github.com/simms2/pressbox-ai-integrations
```

The endpoint is https://agent.pressbox.com/mcp. Pressbox sign-in uses a verified identity and only the delegated pressbox:agent scope, with PKCE. The configured native client ID is public and is not a client secret. The local callback is http://localhost:43187/oauth/callback. Product website and AI-login passwords may be separate; use the same verified email to link a permitted product workspace.

The server checks workspace membership and object access. Preparation does not save or publish a release. Publication and scheduling require exact-copy approval and submitter responsibility. Outbound journalist sending is disabled. Commerce, paid quotations, checkout and payment links are unavailable. Existing account allowances can be inspected without an upsell. No bulk journalist email export is supported.

Instructions: [Pressbox AI integrations](https://pressbox.com/ai). Support: [Pressbox support](https://pressbox.com/support). [Privacy](https://pressbox.com/privacy) and [Terms](https://pressbox.com/terms).

## Review evidence

[Download the 80-second evidence walkthrough](https://github.com/simms2/pressbox-ai-integrations/raw/refs/heads/main/pressbox-review-walkthrough.mp4).

The video is assembled from actual screenshots and test receipts, rather than a continuous screen recording. It contains no passwords or tokens. Native protocol testing does not establish natural-language model behavior. It is not evidence of directory approval or external publication.
