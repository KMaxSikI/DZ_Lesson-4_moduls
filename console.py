import os
import shutil


def copy_folder(old, new):
     return shutil.copy(old, new)


def viewer():
    folder = []
    for fol in os.listdir():
        if os.path.isdir(fol):
            folder.append(fol)
    return folder



