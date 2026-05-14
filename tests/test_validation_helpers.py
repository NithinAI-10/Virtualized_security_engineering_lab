import unittest

from scripts.generate_lab_inventory import ASSETS, render_inventory
from scripts.secret_scan import PATTERNS
from scripts.validate_markdown import validate_markdown


class FakeMarkdownPath:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def read_text(self, encoding):
        return self.content

    def __str__(self):
        return self.name


class ValidationHelperTests(unittest.TestCase):
    def test_inventory_render_includes_all_assets(self):
        rendered = render_inventory(ASSETS)

        self.assertIn("# Lab Asset Inventory", rendered)
        self.assertIn("fw01", rendered)
        self.assertIn("win11-user01", rendered)
        self.assertEqual(rendered.count("|"), 6 * (len(ASSETS) + 2))

    def test_markdown_validator_accepts_basic_document(self):
        path = FakeMarkdownPath("README.md", "# Valid Document\n\nBody text.\n")

        self.assertEqual(validate_markdown(path), [])

    def test_markdown_validator_flags_missing_h1(self):
        path = FakeMarkdownPath("bad.md", "No heading\n")

        issues = validate_markdown(path)
        self.assertTrue(any("level-1 heading" in issue for issue in issues))

    def test_secret_scan_pattern_flags_synthetic_private_key_marker(self):
        marker = "-----BEGIN " + "PRIVATE KEY-----\n"

        self.assertIsNotNone(PATTERNS["private_key"].search(marker))


if __name__ == "__main__":
    unittest.main()
