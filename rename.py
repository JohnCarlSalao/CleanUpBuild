import os

def rename_pyc_files(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.cpython-312.pyc'):
                old_file_path = os.path.join(root, file)
                

                new_file_name = file.replace('.cpython-312.pyc', '.pyc')
                new_file_path = os.path.join(root, new_file_name)
                
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} -> {new_file_path}")

if __name__ == "__main__":
    base_directory = os.getcwd()
    rename_pyc_files(base_directory)
