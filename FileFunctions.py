"""
This file contains some functions that could be used to get information used in the encryption or
decryption process
"""
import os

def folder_exists(folder: str) -> bool:
    """
    Check if folder exists
    """
    return os.path.exists(folder)

def grab_files(folder: str, extensions: list) -> list:
    """
    This function will retreive any files from a given folder
    """
    matching_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            pwd = root + '\\' + file
            file_path, file_ext = os.path.splitext(pwd)
            if file_ext in extensions:
                matching_files.append(pwd)

    return matching_files
