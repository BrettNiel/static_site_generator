import unittest

from textnode import TextNode, TextType
from textnode import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_typenoteq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_textnoteq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is not a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_url_notnone(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://google.com")
        self.assertIsNotNone(node.url, None)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertIsNone(node.url, None)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode(None, TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, None)

    def test_image(self):
        node = TextNode('Test', TextType.IMAGE, 'https://www.google.com')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, '')
        self.assertEqual(html_node.props, {'src': 'https://www.google.com', 'alt': 'Test'})

if __name__ == "__main__":
    unittest.main()