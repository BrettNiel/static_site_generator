import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    split_lines = markdown.split('\n')
    for line in split_lines:
        if line.startswith('# '):
            return line.lstrip('#').strip()
    raise Exception('No such line exists')

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    with open(from_path) as content_file:
        from_contents = content_file.read()

    with open(template_path) as template_file:
        template_contents = template_file.read()

    html_content = markdown_to_html_node(from_contents).to_html()
    title = extract_title(from_contents)

    final_html_content = template_contents.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    with open(dest_path, mode='w') as destination_file:
        destination_file.write(final_html_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for file in os.listdir(dir_path_content):
        source_file_path = os.path.join(dir_path_content, file)
        destination_file_path = os.path.join(dest_dir_path, file)

        if os.path.isfile(source_file_path):
            if source_file_path.endswith('.md'):
                destination_html_path = destination_file_path.replace('.md', '.html')
                generate_page(source_file_path, template_path, destination_html_path)
        else:
            if not os.path.exists(destination_file_path):
                os.makedirs(destination_file_path, exist_ok=True)
            generate_pages_recursive(source_file_path, template_path, destination_file_path)