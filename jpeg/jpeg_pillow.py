from PIL import Image


def encode_and_save_image(input_path):
    # Abrir la imagen original
    image = Image.open(input_path)
    
    # Guardar la imagen codificada en formato JPEG
    encoded_path = input_path.replace('.jpg', '.cod')
    image.save(encoded_path, 'JPEG')
    print(f'Imagen codificada y guardada en {encoded_path}')
    
    return encoded_path

def decode_and_save_image(encoded_path):
    # Abrir la imagen codificada
    encoded_image = Image.open(encoded_path)
    
    # Guardar la imagen decodificada con "_2" al final del nombre
    decoded_path = encoded_path.replace('.cod', '_2.jpg')
    encoded_image.save(decoded_path, 'JPEG')
    print(f'Imagen decodificada y guardada en {decoded_path}')


