import os

root = os.path.abspath(os.getcwd())
folders = list(os.walk(root))[1:]

for folder in folders:
    if not folder[2] and not folder[1]:
        os.rmdir(folder[0])