from enum import Enum

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