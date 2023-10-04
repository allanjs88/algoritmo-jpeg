from PIL import Image

def encode_and_save_image(input_path):
    # Abrir la imagen original
    image = Image.open(input_path)
    
    # Guardar la imagen codificada en formato JPEG
    encoded_path = input_path.replace('.jpg', '.cod')
    image.save(encoded_path, 'JPEG')
    print(f'Imagen codificada y guardada en {encoded_path}')
    
    return encoded_path

def decode_and_save_image(input_path, output_path):
    encoded_image = Image.open(input_path)
    encoded_image.save(output_path, 'JPEG')
    print(f'Imagen decodificada y guardada en {input_path}')