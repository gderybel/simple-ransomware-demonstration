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

def grab_files(folder: str, recursive: bool) -> list[str]:
    """
    This function will retreive any files from a given folder
    """
    matching_files = []

    if recursive:
        for root, _, files in os.walk(folder):
            for file in files:
                full_path = os.path.join(root, file)
                matching_files.append(full_path)
    else:
        for file in os.listdir(folder):
            full_path = os.path.join(folder, file)
            if os.path.isfile(full_path):
                matching_files.append(full_path)

    return matching_files
