from pathlib import Path


def parse_folder(path):
    files = []
    folders = []
    for i in path.iterdir():

        if i.is_dir():
            folders.extend([i.name])
        else:
            files.extend([i.name])
    print(files)
    print(folders)

    return files, folders