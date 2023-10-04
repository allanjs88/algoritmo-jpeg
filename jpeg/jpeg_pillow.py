from PIL import Image

def encode_and_save_image_jpeg(input_path):
    image = Image.open(input_path)
    encoded_path = input_path.replace('.jpg', '.jpeg')
    image.save(encoded_path, 'JPEG')
    print(f'Imagen codificada y guardada en {encoded_path}')
    
    return encoded_path

def decode_and_save_image_jpeg(input_path, output_path):
    encoded_image = Image.open(input_path)
    encoded_image.save(output_path, 'JPEG')
    print(f'Imagen decodificada y guardada en {input_path}')