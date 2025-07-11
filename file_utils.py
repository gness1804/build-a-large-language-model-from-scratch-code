import os
import urllib.request

def download_and_read_text_file(file_path: str , url : str) -> str:
    """
    Download a text file if it doesn't exist and read its contents.
    
    Args:
        file_path (str): Path to the text file to download and read
        url (str): URL to the text file to download
    
    Returns:
        str: The contents of the text file
    """
    if not os.path.exists(file_path):
        urllib.request.urlretrieve(url, file_path)
        print(f"File downloaded to {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        raw_text = f.read()
    
    return raw_text 