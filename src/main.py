from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    #test_node = TextNode("Hello World", TextType.TEXT, "https://www.google.com")

    test_node = HTMLNode("<p>", "Test paragraph", "<div>", "id: 1")

    print(test_node)

main()