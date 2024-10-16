import os

def list_dir_files(dir):
    dirs = []
    for file in os.listdir(dir):
        file_path = os.path.join(dir, file)
        if not os.path.isfile(file_path):
            dirs.append(file)
    return dirs

def check_file_type(file, target_extensions):
    _, extension = os.path.splitext(file)
    extension = extension[1:]
    #TODO: this is O(n), with sorting it could be O(log(n))
    #n being number of target extensions
    for target_extension in target_extensions:
        if extension == target_extension:
            return True                                                   
    return False

def find_files(dir, target_extensions):
    target_files = []

    for path, _, files in os.walk(dir):
        for file in files:
            if check_file_type(file, target_extensions):
                file_path = os.path.join(path, file)
                target_files.append(file_path)

    return target_files
