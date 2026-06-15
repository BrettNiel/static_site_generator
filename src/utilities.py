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

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        images = extract_markdown_images(node.text)
        remaining_text = node.text
        if not images:
            result.append(node)
            continue
        for (alt, url) in images:
            sections = remaining_text.split(f'![{alt}]({url})', 1)
            if sections[0]:
                result.append(TextNode(sections[0], TextType.TEXT))
            result.append(TextNode(alt, TextType.IMAGE, url))
            remaining_text = sections[1]
        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))
    return result

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        links = extract_markdown_links(node.text)
        remaining_text = node.text
        if not links:
            result.append(node)
            continue
        for (anchor, url) in links:
            sections = remaining_text.split(f'[{anchor}]({url})', 1)
            if sections[0]:
                result.append(TextNode(sections[0], TextType.TEXT))
            result.append(TextNode(anchor, TextType.LINK, url)) 
            remaining_text = sections[1]
        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))
    return result

def text_to_textnodes(text):
    list_text = [TextNode(text, TextType.TEXT)]
    list_text = split_nodes_delimiter(list_text, '**', TextType.BOLD) 
    list_text = split_nodes_delimiter(list_text, '_', TextType.ITALIC)
    list_text = split_nodes_delimiter(list_text, '`', TextType.CODE)
    list_text = split_nodes_image(list_text)
    list_text = split_nodes_link(list_text)
    return list_text

def extract_markdown_images(text):
    pattern = r'!\[([^\[\]]*)\]\(([^\(\)]*)\)'
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)'
    matches = re.findall(pattern, text)
    return matches