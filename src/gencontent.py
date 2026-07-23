from markdown_blocks import markdown_to_html_node
from htmlnode import to_html

def extract_title(markdown):
    split_lines = markdown.split('\n')
    for line in split_lines:
        if line.startswith('# '):
            return line.lstrip('#').strip()
    raise Exception('No such line exists')

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    content_file = open(from_path)
    from_contents = content_file.read()

    template_file = open(template_path)
    template_contents = template_file.read()

