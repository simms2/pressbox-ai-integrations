"""Validate the public Pressbox Claude plugin candidate without making network calls.

Run with: python -m unittest discover -s tests -p 'test_claude_plugin_contract.py'
"""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PUBLIC = "https://pressbox.com/mcp"
EXPECTED_PRIVATE = "https://agent.pressbox.com/mcp"

class ClaudePluginContract(unittest.TestCase):
    def test_manifest_and_marketplace_identity(self):
        manifest = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        self.assertEqual(manifest["name"], "pressbox")
        self.assertEqual(market["plugins"][0]["name"], manifest["name"])
        self.assertEqual(market["plugins"][0]["source"], "./")
        self.assertNotIn("hooks", manifest)

    def test_remote_mcp_hosts_are_separate_and_no_secrets(self):
        config = json.loads((ROOT / ".mcp.json").read_text())["mcpServers"]
        self.assertEqual(set(config), {"pressbox", "pressbox-news"})
        self.assertEqual(config["pressbox"]["url"], EXPECTED_PRIVATE)
        self.assertEqual(config["pressbox-news"]["url"], EXPECTED_PUBLIC)
        for server in config.values():
            self.assertEqual(server["type"], "http")
            self.assertNotIn("headers", server)
            self.assertNotIn("env", server)
            self.assertNotIn("token", server)
            self.assertNotIn("command", server)

    def test_all_three_skills_have_discoverable_frontmatter(self):
        for name in ("pressbox-release-distribution", "pressbox-published-news", "pressbox-release-readiness"):
            path = ROOT / "skills" / name / "SKILL.md"
            raw = path.read_text()
            self.assertTrue(raw.startswith("---\n"), name)
            head = raw.split("---", 2)[1]
            self.assertIn("name: " + name, head)
            self.assertIn("description:", head)
            self.assertGreater(len(raw), 300, name)

    def test_safe_behaviour_in_public_and_editorial_skills(self):
        public = (ROOT/"skills/pressbox-published-news/SKILL.md").read_text().lower()
        editorial = (ROOT/"skills/pressbox-release-readiness/SKILL.md").read_text().lower()
        account = (ROOT/"skills/pressbox-release-distribution/SKILL.md").read_text().lower()
        self.assertIn("read-only", public)
        self.assertIn("untrusted", public)
        self.assertIn("explicit user approval", editorial)
        self.assertIn("never invent", editorial)
        self.assertIn("sending is disabled", account)
        self.assertIn("no digital commerce", account)

if __name__ == "__main__":
    unittest.main()
