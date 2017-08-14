import os
from collections import defaultdict
from argparse import ArgumentParser


def validate_file_path(root_folder):
    if not os.path.exists(root_folder):
        return False
    else:
        return True


def get_duplicates(root_folder):
    root_files = defaultdict(list)
    for directory, sub_dirs, files in os.walk(root_folder):
        for file in files:
            path = os.path.join(directory, file)
            size = os.path.getsize(path)
            root_files[(file, str(size))].append(path)
    duplicates = [file for file in root_files.items() if len(file[1]) > 1]
    return duplicates


def delete_dups(duplicates):
    if len(duplicates):
        for duplicate_number, duplicate in enumerate(duplicates):
            print('In these directory there are duplicates:')
            print('Name of duplicate: {}'.format(duplicate[0][0]))
            print('Size of duplicate: {}'.format(duplicate[0][1]))
            print('Paths of duplicates: {}'.format(duplicate[1][1:][0]))
            os.remove(duplicate[1][1:][0])
            print('Success')
            print('----------------------------')
    else:
        print('In these directory {} \n'
              'duplicates NOT FOUND')


if __name__ == '__main__':
    parser = ArgumentParser(description='Folder path')
    parser.add_argument('--path', type=str)
    args = parser.parse_args()
    if validate_file_path(args):
        duplicates = get_duplicates(args)
        if duplicates:
            if len(duplicates):
                delete_dups(duplicates)
            else:
                print('Duplicates not found')
    else:
        print('No such file')


