

def markdown_to_blocks(markdown):
    split_lines = markdown.split('\n\n')
    stripped_lines = []
    for line in split_lines:
        if not line:
            continue
        stripped_lines.append(line.strip())
    return stripped_lines

