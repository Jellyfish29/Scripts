import os


files = os.listdir(os.getcwd())


i = 0
name = input('name >>> ')
for file in files:
    if file != "bulk_rename.py":
        os.rename(file, f"{str(i).rjust(4, '0')}_{name}.png")
        i += 1
