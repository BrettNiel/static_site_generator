import unittest

from utilities import split_nodes_delimiter
from textnode import TextNode, TextType


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