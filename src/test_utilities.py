import unittest

from utilities import split_nodes_delimiter
from textnode import TextNode, TextType
from utilities import extract_markdown_images
from utilities import extract_markdown_links


class TestNodeDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode('This is a text node with `code` in it', TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '`', TextType.CODE)
        self.assertListEqual(
            [
                TextNode('This is a text node with ', TextType.TEXT),
                TextNode('code', TextType.CODE),
                TextNode(' in it', TextType.TEXT)
            ],
            new_nodes,
        )

class TestNodeDelimiter(unittest.TestCase):
    def test_bold(self):
        node = TextNode('This is a text node with **bold words** in it', TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '**', TextType.BOLD)
        self.assertListEqual(
            [
                TextNode('This is a text node with ', TextType.TEXT),
                TextNode('bold words', TextType.BOLD),
                TextNode(' in it', TextType.TEXT)
            ],
            new_nodes,
        )

class TestNodeDelimiter(unittest.TestCase):
    def test_italic(self):
        node = TextNode('This is a text node with _italic words_ in it', TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '_', TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode('This is a text node with ', TextType.TEXT),
                TextNode('italic words', TextType.ITALIC),
                TextNode(' in it', TextType.TEXT)
            ],
            new_nodes,
        )

class TestExtractImage(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

class TestExtractLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a [link](https://www.google.com)")
        self.assertListEqual([("link", "https://www.google.com")], matches)