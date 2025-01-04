import os
import shutil
import sys

def cleanup_directory(base_dir, confirm_all):
    if not confirm_all:
        print("Operation cancelled.")
        return

    for root, dirs, files in os.walk(base_dir, topdown=False):
        # Delete .py files
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")
              
        for dir in dirs:
            if dir == '__pycache__':
                pycache_path = os.path.join(root, dir)
                for pyc_file in os.listdir(pycache_path):
                    if pyc_file.endswith('.pyc'):
                        pyc_file_path = os.path.join(pycache_path, pyc_file)
                        new_location = os.path.join(root, pyc_file)
                        shutil.move(pyc_file_path, new_location)
                        print(f"Moved: {pyc_file_path} to {new_location}")

                shutil.rmtree(pycache_path)
                print(f"Deleted directory: {pycache_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        base_directory = sys.argv[1]
        if not os.path.isdir(base_directory):
            print(f"Error: {base_directory} is not a valid directory.")
            sys.exit(1)
    else:
        base_directory = os.getcwd()  

    confirm = input(
        f"This will delete all .py files, move .pyc files from __pycache__, "
        f"and delete all __pycache__ directories in {base_directory}. Proceed? (y/n): "
    ).strip().lower()

    if confirm == 'y':
        print(f"Starting operations in {base_directory}...")

        cleanup_directory(base_directory, True)
    else:
        print("Operation cancelled.")
