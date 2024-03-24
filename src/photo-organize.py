import argparse
import os
from datetime import datetime
from exif import Image
import shutil

import hashlib  # For hash calculation

def compute_hash(file_path):
    """
    Compute the SHA-256 hash of a file.
    """
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def parse_date_exif(date_string):
    """
    Parse EXIF date strings in the format YYYY:MM:DD HH:MM:SS.
    """
    try:
        return datetime.strptime(date_string, '%Y:%m:%d %H:%M:%S')
    except ValueError:
        return None

def get_oldest_timestamp(image_path):
    """
    Extract the oldest timestamp from an image's EXIF data.
    """
    try:
        with open(image_path, 'rb') as image_file:
            image = Image(image_file)
            if image.has_exif:
                datetime_original = getattr(image, 'datetime_original', None)
                datetime_digitized = getattr(image, 'datetime_digitized', None)
                datetime_modified = getattr(image, 'datetime', None)

                print(f"Original: {datetime_original}, Digitized: {datetime_digitized}, Modified: {datetime_modified}")

                # Convert all to datetime objects
                dates = [parse_date_exif(d) for d in [datetime_original, datetime_digitized, datetime_modified] if d]

                # Return the oldest date
                return min(dates) if dates else None
            else:
                return None
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def sort_photos(src_dir, dest_dir, recursive=False):
    """
    Sort photos into folders by their EXIF timestamps.
    """
    if recursive:
        for root, dirs, files in os.walk(src_dir):
            for name in files:
                process_file(os.path.join(root, name), dest_dir)
    else:
        for name in os.listdir(src_dir):
            file_path = os.path.join(src_dir, name)
            if os.path.isfile(file_path):
                process_file(file_path, dest_dir)

def process_file(file_path, dest_dir):
    """
    Process a single file, moving it to the correct location based on its EXIF timestamp.
    """
    date = get_oldest_timestamp(file_path)
    if date:
        # Create folder structure based on the date
        date_folder = date.strftime('%Y/%m/%d')
        dest_path = os.path.join(dest_dir, date_folder)

        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

        # Compute SHA-256 hash of the image
        hash_value = compute_hash(file_path)

        # Prepare the destination filename with the format YYYYMMDD_HHMMSS_hashvalue.jpg
        timestamp = date.strftime('%Y%m%d_%H%M%S')
        filename = os.path.basename(file_path)
        name, ext = os.path.splitext(filename)
        new_filename = f"{timestamp}_{hash_value[:8]}{ext}".lower()  # Using first 8 characters of the hash

        # Copy file to the new destination with the new filename
        shutil.copy(file_path, os.path.join(dest_path, new_filename))
        print(f"Copied {file_path} to {os.path.join(dest_path, new_filename)}")
    else:
        print(f"No EXIF date found for {file_path}. File will not be moved.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort photos into folders based on their EXIF timestamps and file content hash.")
    parser.add_argument("src_directory", type=str, help="Source directory containing files to sort.")
    parser.add_argument("dest_directory", type=str, help="Destination directory where sorted files will be placed.")
    parser.add_argument("-r", "--recursive", action="store_true", help="Search src_directory recursively for files to sort.")

    args = parser.parse_args()

    print("Starting sorting photos")
    sort_photos(args.src_directory, args.dest_directory, args.recursive)
