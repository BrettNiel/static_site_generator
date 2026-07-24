import os
import shutil
from copystatic import copy_contents
from gencontent import generate_page

dir_path_static = './static'
dir_path_public = './public'
dir_path_content = './content'
template_path = './template.html'

def main():

    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    copy_contents(dir_path_static, dir_path_public)

    generate_page(os.path.join(dir_path_content, 'index.md'), template_path, os.path.join(dir_path_public, 'index.html'))

main()