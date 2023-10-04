import imghdr
import os

def is_image(file_path):
    # Check the file extension
    file_extension = os.path.splitext(file_path)[-1].lower()
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico']
    return file_extension in image_extensions

def get_file_extension(file):
    split_tup = os.path.splitext(file)
    return split_tup[1]

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)