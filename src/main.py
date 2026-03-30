from textnode import TextNode, TextType

def main():
    test_node = TextNode("Hello World", TextType.TEXT, "https://www.google.com")

    print(test_node)

main()