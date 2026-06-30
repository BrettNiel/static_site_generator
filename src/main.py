import os
import shutil
from copystatic import copy_contents

def main():

    if os.path.exists('public/'):
        shutil.rmtree('public/')

    copy_contents('static/', 'public/')

main()