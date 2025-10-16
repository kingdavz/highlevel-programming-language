#!/usr/bin/python
"""A module that ensure folder exist and move file"""

import shutil

def ensure_dir(path):
    path.mkdir(parents=True, exist_ok=True)


def move_file (src, dest):
    ensure_dir(dest)
    des_path = dest / src.name

    if des_path.exists():
        stem, suffix = src.stem, src.suffix
        counter = 1
        while True:
            candidate = dest / f"{stem}_{counter}{suffix}"
            if not candidate.exists():
                break
            counter += 1
    shutil.move(src, dest)
    return des_path