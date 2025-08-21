#Python file detection
import os

file_path='C:/Users/user/Desktop/you_tube'
if os.path.exists(file_path):
    print(f'The file "{file_path}" exists!')
    if os.path.isfile(file_path):
        print(f'The file "{file_path}" is a file!')
    elif os.path.isdir(file_path):
        print("This is a directory!")
else:
    print(f'The file "{file_path}" does not exist!')
