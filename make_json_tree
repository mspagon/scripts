import json
import os

from collections import OrderedDict

"""
This file prints a json of the directory structure.  It ignores hidden files and files with the extensions in the top
level `files_to_ignore` list.

From Spagon to nntrn.
"""

# Joins path of current working directory (CWD) to a folder called posts = ./posts
root = os.path.join('.', 'posts')

# Ignore these files
files_to_ignore = ['.md', '.js']


def get_dirs(path: str) -> list:
    """
    Get list of directories within path.
    """
    dir_names = []
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            dir_names.append(item)
    return sorted(dir_names)


def get_files(path: str, ignore: list = None) -> list:
    """
    Get list of files within path.
    """
    if ignore is None:
        ignore = []

    files = []
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            if not item.startswith('.') and not item.endswith(tuple(ignore)):
                files.append(item)
    return sorted(files)


def make_tree(path: str, ignore: list = None) -> OrderedDict:
    """
    Makes an ordered dict of directory structure one level deep.

    Disregards files ending with the extensions found in ignore.

    {
    'dirname': [file1, ..., file2],
    'dirname': [file1, ..., file2]
    }
    """
    if ignore is None:
        ignore = []

    dir_tree = OrderedDict()
    for directory in get_dirs(path):
        subpath = os.path.join(root, directory)
        dir_tree[directory] = get_files(subpath, ignore=ignore)
    return dir_tree


def main():
    tree = make_tree(root, files_to_ignore)

    js_json = "files=" + json.dumps(tree, indent=2)
    print('\n\n' + js_json + '\n\n')

    with open("pages.js", 'w+') as f:
        f.write(js_json)


if __name__ == '__main__':
    main()
