import unittest
from gencontent import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_one_tag(self):
        markdown = '# Test'
        self.assertEqual(
            extract_title(markdown),
            'Test'
        )

    def test_multiple_tags(self):
        markdown = '# ## Test'
        self.assertEqual(
            extract_title(markdown),
            '## Test'
        )

    def test_no_header(self):
        markdown = 'Test'
        with self.assertRaises(Exception):
            extract_title(markdown)