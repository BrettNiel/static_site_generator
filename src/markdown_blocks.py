from enum import Enum
from utilities import text_to_textnodes
from textnode import *
from htmlnode import ParentNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):

    lines = block.split('\n')
    counter = 1

    if block.startswith(('# ', '## ', '### ', '#### ', '##### ', '###### ')):
        return BlockType.HEADING
    elif block.startswith('```\n') and block.endswith('```'):
        return BlockType.CODE
    elif block.startswith('>'):
        for line in lines:
            if not line.startswith('>'):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    elif block.startswith('- '):
        for line in lines:
            if not line.startswith('- '):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    elif block.startswith(f'{counter}. '):
        for line in lines:
            if not line.startswith(f'{counter}. '):
                return BlockType.PARAGRAPH
            counter += 1
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    split_lines = markdown.split('\n\n')
    stripped_lines = []
    for line in split_lines:
        if not line:
            continue
        stripped_lines.append(line.strip())
    return stripped_lines

def markdown_to_html_node(markdown):
    split_markdown = markdown_to_blocks(markdown)
    node_list = []
    for block in split_markdown:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            node = heading_to_html_node(block)
        elif block_type == BlockType.CODE:
            node = code_to_html_node(block)
        elif block_type == BlockType.QUOTE:
            node = quote_to_html_node(block)
        elif block_type == BlockType.UNORDERED_LIST:
            node = ul_to_html_node(block)
        elif block_type == BlockType.ORDERED_LIST:
            node = ol_to_html_node(block)
        elif block_type == BlockType.PARAGRAPH:
            node = paragraph_to_html_node(block)
        else:
            raise Exception("Error with block type value")
        node_list.append(node)
    return ParentNode('div', node_list)


def text_to_children(text):
    textnodes = text_to_textnodes(text)
    htmlnodes = []
    for node in textnodes:
        htmlnodes.append(text_node_to_html_node(node))
    return htmlnodes

def paragraph_to_html_node(block):
    lines = block.split('\n')
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode('p', children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == '#':
            level += 1
        else:
            break
    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f'h{level}', children)

def code_to_html_node(block):
    raw_text = block[4:-3]
    text = TextNode(raw_text, TextType.TEXT)
    htmlnode = text_node_to_html_node(text)
    code = ParentNode('code', [htmlnode])
    return ParentNode('pre', [code])

def quote_to_html_node(block):
    lines = block.split('\n')
    updated_lines = []
    for line in lines:
        updated_lines.append(line.lstrip('>').strip())
    quote = " ".join(updated_lines)
    children = text_to_children(quote)
    return ParentNode('blockquote', children)

def ul_to_html_node(block):
    lines = block.split('\n')
    updated_lines = []
    for line in lines:
        line = line[2:]
        children = text_to_children(line)
        updated_lines.append(ParentNode('li', children))
    return ParentNode('ul', updated_lines)

def ol_to_html_node(block):
    lines = block.split('\n')
    updated_lines = []
    for line in lines:
        line = line.split('. ', 1)[1]
        children = text_to_children(line)
        updated_lines.append(ParentNode('li', children))
    return ParentNode('ol', updated_lines)