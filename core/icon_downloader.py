import gdown
import zipfile
import os
import hashlib
import shutil

KNOWN_GOOD_HASH = 'a53c748e04baf70f9bbdae4f04186adc'  # Replace with actual hash

def md5_dir(directory):
    hash_md5 = hashlib.md5()
    for root, dirs, files in os.walk(directory):
        for filename in sorted(files):
            filepath = os.path.join(root, filename)
            with open(filepath, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
    return hash_md5.hexdigest()

def get_icons():
    url = 'https://drive.google.com/uc?id=1hzbHyF8qGSA53fYnl8H7UMNUrmFC49KU'
    zip_path = '../data/icons.zip'
    extract_path = '../data/icons/'

    # Check for valid icons folder via MD5
    if os.path.exists(extract_path):
        print("Found existing icons folder. Verifying integrity...")
        current_hash = md5_dir(extract_path)
        if current_hash == KNOWN_GOOD_HASH:
            print("Icons folder is valid. No need to download.")
            return extract_path
        else:
            print("Icons folder hash mismatch. Cleaning up...")
            shutil.rmtree(extract_path)
            if os.path.exists(zip_path):
                os.remove(zip_path)

    # Check if icons.zip already exists
    if os.path.exists(zip_path):
        print("Found existing icons.zip. Extracting...")
    else:
        print("Downloading icons.zip...")
        downloaded = gdown.download(url, zip_path, quiet=False)
        if not downloaded or not os.path.exists(zip_path):
            print("Download failed.")
            return None

    # Extract icons.zip
    print("Extracting icons.zip...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print(f"Icons extracted to {extract_path}")

    # Optional: Remove the zip after extraction
    os.remove(zip_path)
    print("Cleaned up icons.zip")

    return extract_path

