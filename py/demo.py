# a_string = "this is\na string split\t\tand tabbed"
# print(a_string)

# raw_string = r"this is\na string split\t\tand tabbed"
# print(raw_string)

# b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
# print(b_string)

# backslash_string = "this is a backslash \followed by some text"
# print(backslash_string)

# backslash_string = "this is a backslash \\followed by some text"
# print(backslash_string)

# error_string = r"this string ends with \\"
# l = [1,2,3,4,5]
# print(l[2:3])

import os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}|- {}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}|- {}'.format(subindent, f))

list_files(os.getcwd())

