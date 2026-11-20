import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.prepare_medium_sync import ValidationError, pending_diff, prepare_markdown


class PrepareMarkdownTests(unittest.TestCase):
    def test_resolves_relative_markdown_and_html_links_to_pages_urls(self):
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "images").mkdir()
            (root / "images" / "example image.png").write_bytes(b"image")

            prepared = prepare_markdown(
                '![example](images/example%20image.png) '
                '<img src="images/example%20image.png">',
                root,
            )

        expected = "https://rytina.github.io/code4future/images/example%20image.png"
        self.assertEqual(prepared, f"![example]({expected}) <img src=\"{expected}\">")

    def test_rejects_missing_relative_links(self):
        with TemporaryDirectory() as temporary_directory:
            with self.assertRaisesRegex(ValidationError, "does not exist"):
                prepare_markdown("[missing](missing.pdf)", Path(temporary_directory))

    def test_rejects_links_that_escape_repository(self):
        with TemporaryDirectory() as temporary_directory:
            with self.assertRaisesRegex(ValidationError, "escapes the repository"):
                prepare_markdown("[outside](../outside.pdf)", Path(temporary_directory))

    def test_keeps_supported_absolute_and_mailto_links(self):
        markdown = "[site](https://example.com) [email](mailto:hello@example.com) [section](#sources)"
        self.assertEqual(prepare_markdown(markdown, Path(".")), markdown)

    def test_initial_diff_contains_the_complete_article(self):
        diff = pending_diff("", "0123456789abcdef", "First line\nSecond line\n")

        self.assertIn("+First line", diff)
        self.assertIn("+Second line", diff)


if __name__ == "__main__":
    unittest.main()
