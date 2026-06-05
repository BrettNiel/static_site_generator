from textnode import TextNode
from textnode import TextType
import re
 
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if not node.text_type == TextType.TEXT:
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise Exception("Incorrect syntax, missing closing delimiter!")
        for indice, text in enumerate(split_text):
            if text == '':
                continue
            if indice % 2 == 0:
                new_nodes.append(TextNode(text, TextType.TEXT))
            else:
                new_nodes.append(TextNode(text, text_type))
    return new_nodes



def extract_markdown_images(text):
    pattern = r'!\[([^\[\]]*)\]\(([^\(\)]*)\)'
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)'
    matches = re.findall(pattern, text)
    return matches