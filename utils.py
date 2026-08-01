"""
utils.py

Helper functions used throughout the project.
"""

import os
import time
from pathlib import Path


def create_directory(directory_path: str):
    """
    Create a directory if it does not exist.
    """
    Path(directory_path).mkdir(parents=True, exist_ok=True)


def create_project_directories(directories):
    """
    Create multiple directories.
    """
    for directory in directories:
        create_directory(directory)


def validate_pdf(file_path: str):
    """
    Validate PDF file.
    """
    if not os.path.exists(file_path):
        return False

    if not file_path.lower().endswith(".pdf"):
        return False

    if os.path.getsize(file_path) == 0:
        return False

    return True


def get_file_size(file_path):
    """
    Return file size in MB.
    """
    size = os.path.getsize(file_path)
    return round(size / (1024 * 1024), 2)


def calculate_processing_time(start_time):
    """
    Calculate total execution time.
    """
    end_time = time.time()
    return round(end_time - start_time, 2)


def format_time(seconds):
    """
    Convert seconds into readable format.
    """
    if seconds < 60:
        return f"{seconds} sec"

    minutes = seconds // 60
    seconds = seconds % 60

    return f"{int(minutes)} min {int(seconds)} sec"


def print_success(message):
    print(f"✅ {message}")


def print_error(message):
    print(f"❌ {message}")


def print_info(message):
    print(f"ℹ️ {message}")