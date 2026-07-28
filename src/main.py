import os
import shutil
import sys
from copystatic import copy_contents
from gencontent import generate_pages_recursive

dir_path_static = './static'
dir_path_docs = './docs'
dir_path_content = './content'
template_path = './template.html'

def main():

    if len(sys.argv) < 2:
        basepath = '/'
    else:
        basepath = sys.argv[1]

    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    copy_contents(dir_path_static, dir_path_docs)

    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)

main()