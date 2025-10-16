#!/usr/bin/python
"""A module that maps a file to the corresponding extension"""

CATEGORY_MAP = {
    "Image" : {".jpg", ".png", ".gif", ".bmp", ".tiff",".webp"},
    "Videos" : {".mp4", ".avi", ".mkv", ".mov", ".wmv"},
    "Documents" : {".pdf", ".txt", ".doc", ".xls", ".xlsx", "ppt", ".pptx"},
    "Archives" : {".zip", ".zar", ".7z", ".tar", ".gz"},
    "code" : {".py", ",java", ".c", ".cpp", ".html", ".css", ".js"}
    }

def detect_category(filename):
    ext = filename.suffix.lower()
    for category, extensions in CATEGORY_MAP.items():
        if ext in extensions:
            return category
    return "other"
