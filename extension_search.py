import os
import shutil
import threading


"""
A Script that recursivly searches the specified root directory for all files
with the specified file extension
Options:
[1]Print Path: Prints the Path to all found files
[2]Copy to: Copies the found files to specified directory

"""

print_path = False
copy_to = False


def search_dir(directory, extension, dest=None):
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isfile(path):
            if not item[0] == "$":
                file_extension = item.split(".")[-1]
                if file_extension == extension:
                    if print_path:
                        print(path)
                    elif copy_to:
                        shutil.copy(path, dest)
                        print(f"copying:    {item}")

        elif os.path.isdir(path):
            try:
                search_dir(path, extension, dest=dest)
            except PermissionError:
                with open(os.path.join(os.getcwd(), "extension_search_log.txt"), "a") as f:
                    f.write(f"PermissionError for {path}\n")


root = input("root directory >>> ")
extension = input("extension >>> ")
option = input("options: [1] Print Path  [2] Copy to\n>>> ")


if option == "1":
    print_path = True
    search_dir(root, extension)
elif option == "2":
    copy_to = True
    dest_dir = input("destination directory: ")
    thread = threading.Thread(target=search_dir, args=[root, extension, dest_dir])
    thread.start()
    # search_dir(root, extension, dest=dest_dir)
else:
    print("Wrong input")
