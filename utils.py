import os
from PIL import Image

def is_image(file_path):
    file_extension = os.path.splitext(file_path)[-1].lower()
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico']
    return file_extension in image_extensions

def get_file_extension(file):
    split_tup = os.path.splitext(file)
    return split_tup[1]

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def encode_and_save_image(input_path, format='JPEG'):
    intermediate_ext = '.' + format.lower()
    image = Image.open(input_path)
    encoded_path = input_path.replace(get_file_extension(input_path), intermediate_ext)
    image.save(encoded_path, format)
    print(f'Imagen codificada y guardada en {encoded_path}')
    
    return encoded_path

def decode_and_save_image(encoded_path, output_path):
    encoded_image = Image.open(encoded_path)
    encoded_image.save(output_path, 'JPEG')
    print(f'Imagen decodificada y guardada en {output_path}')