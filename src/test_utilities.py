import unittest

from textnode import TextNode, TextType
from utilities import split_nodes_delimiter
from utilities import extract_markdown_images
from utilities import extract_markdown_links
from utilities import split_nodes_image
from utilities import split_nodes_link
from utilities import text_to_textnodes
from utilities import markdown_to_blocks

class TestUtilities(unittest.TestCase):

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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.google.com) and another [second link](https://www.youtube.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://www.youtube.com"),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        node = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(node)
        self.assertListEqual(
            [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ], new_nodes,
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a [link](https://www.google.com)")
        self.assertListEqual([("link", "https://www.google.com")], matches)