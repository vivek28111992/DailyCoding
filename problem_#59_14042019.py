"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Implement a file syncing algorithm for two computers over a low-bandwidth network. What if we know the files in the two computers are mostly the same?


https://scammingthecodinginterview.com/coding_problems/005.html
https://github.com/vineetjohn/daily-coding-problem/blob/master/solutions/problem_059.py
"""

from hashlib import md5

class MerkerFile(object):

    def __init__(self):
        self.content = ''
        self.hash = ''
        self.children = []
        self.is_dir = None
        self.parent = None

    def set_content(self, new_content):

        if self.is_dir:
            raise Exception("Can't set the contents of a directory")

        self.content = new_content
        self.recalculate_directory_hash()

    def recalculate_directory_hash(self):
        parent = self.parent

        if not self.is_dir:
            self.hash = md5(self.content.encode()).hexdigest()

        while parent:
            children = parent.children
            collated_hash = ''
            for child in children:
                collated_hash += child.hash


            parent.hash = md5(collated_hash.encode()).hexdigest()

            parent = parent.parent

    def add_file_to_directory(self, directory):
        directory.children.append(self)

        self.parent = directory

        self.recalculate_directory_hash()

def get_files_that_are_different(root_1, root_2, file_changes_for_system_1, file_changes_for_system_2):

    if not root_1 or not root_2:
        return file_changes_for_system_1, file_changes_for_system_2

    if not root_1 or not root_2:
        file_changes_for_system_1.append(root_2)
        file_changes_for_system_2.append(root_1)

        return file_changes_for_system_1, file_changes_for_system_2

    if root_1.hash != root_2.hash:
        file_changes_for_system_1.append(root_2)
        file_changes_for_system_2.append(root_1)

        root_1_children = root_1.children
        root_2_children = root_2.children

        len_diff = abs(len(root_1_children) - len(root_2_children))

        if len(root_1_children) > len(root_2_children):
            root_2_children = root_2_children + [None for i in range(0, len_diff)]
        elif len(root_2_children) > len(root_1_children):
            root_1_children = root_2_children + [None for i in range(0, len_diff)]

        for child1, child2 in zip(root_1_children, root_2_children):
            get_files_that_are_different(child1, child2, file_changes_for_system_1, file_changes_for_system_2)

    return file_changes_for_system_1, file_changes_for_system_2

if __name__ == '__main__':

    # create a directory structure on the first computer
    root_directory = MerkerFile()
    root_directory.is_dir = True

    file1 = MerkerFile()
    file1.is_dir = False
    file1.add_file_to_directory(root_directory)
    file1.set_content("owl city rocks!")

    file2 = MerkerFile()
    file2.is_dir = False
    file2.add_file_to_directory(root_directory)
    file2.set_content("owl city rocks again!")

    directory_2 = MerkerFile()
    directory_2.is_dir = True
    directory_2.add_file_to_directory(root_directory)

    file3 = MerkerFile()
    file3.is_dir = False
    file3.add_file_to_directory(directory_2)
    file3.set_content("owl city rocks!")

    # create a directory structure on the second computer
    root_directory_2 = MerkerFile()
    root_directory_2.is_dir = True

    file1_2 = MerkerFile()
    file1_2.is_dir = False
    file1_2.add_file_to_directory(root_directory_2)
    file1_2.set_content("owl city rocks!")

    file2_2 = MerkerFile()
    file2_2.is_dir = False
    file2_2.add_file_to_directory(root_directory_2)
    file2_2.set_content("owl city rocks again!")

    directory_2_2 = MerkerFile()
    directory_2_2.is_dir = True
    directory_2_2.add_file_to_directory(root_directory_2)

    file3_2 = MerkerFile()
    file3_2.is_dir = False
    file3_2.add_file_to_directory(directory_2_2)
    # This is the only file that is different
    file3_2.set_content("owl city rocks! pop")

    # Now to know the files that have changed, we can just compare the two trees
    # and effectively know which files have changed and need syncing.

    file_changes_for_system_1, file_changes_for_system_2 = get_files_that_are_different(
        root_directory, root_directory_2, [], []
    )

