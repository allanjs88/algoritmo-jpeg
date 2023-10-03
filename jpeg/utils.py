import imghdr
import os

def is_image(file_path):
    # Check the file extension
    file_extension = os.path.splitext(file_path)[-1].lower()
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico']

    if file_extension in image_extensions:
        return True

    # Check the file content using imghdr
    image_type = imghdr.what(file_path)
    return image_type is not None