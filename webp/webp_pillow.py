from PIL import Image

def encode_and_save_image_webp(input_path):
    image = Image.open(input_path)
    encoded_path = input_path.replace('.jpg', '.webp')
    image.save(encoded_path, 'WEBP')
    print(f'Imagen codificada y guardada en {encoded_path}')
    
    return encoded_path

def decode_and_save_image_webp(encoded_path, output_path):
    encoded_image = Image.open(encoded_path)
    encoded_image.save(output_path, 'JPEG')
    print(f'Imagen decodificada y guardada en {output_path}')
