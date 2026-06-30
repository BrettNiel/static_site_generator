import shutil
import os

def copy_contents(source, destination):

    if not os.path.exists(destination):
        print(f'Creating directory: {destination}')
        os.mkdir(destination)

    for item in os.listdir(source):
        from_path = os.path.join(source, item)
        to_path = os.path.join(destination, item)

        if os.path.isdir(from_path):
            copy_contents(from_path, to_path)
        
        elif os.path.isfile(from_path):
            print(f'Copying {from_path} to {to_path}')
            shutil.copy(from_path, to_path)