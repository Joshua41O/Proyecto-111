import os
import shutil

from_dir = "C:/Users/Joshua/Downloads"
to_dir = "C:/User/Joshua/Desktop"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)

path = "C:/Users/Joshua/Desktop/python"
IsExist = os.path.exists(path)
print(IsExist)