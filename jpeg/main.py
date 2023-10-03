import os
from jpeg_pillow import encode_and_save_image, decode_and_save_image
from utils import is_image

IMAGE_PATH = "images/"
ENCRYPTED_IMAGE_PATH = "encrypted_images/"

if __name__ == '__main__':

    images = os.listdir(IMAGE_PATH)

    for image in images:
        print("Imagen: "+ image)
        if is_image(image):
            # Reemplaza 'tu_imagen.jpg' con la ruta de tu imagen
            input_image_path = IMAGE_PATH + image
            encrypted_images_path = ENCRYPTED_IMAGE_PATH + image
            
            # Codificar y guardar la imagen
            encoded_path = encode_and_save_image(input_image_path)
            
            # Decodificar y guardar la imagen
            decode_and_save_image(encoded_path, encrypted_images_path)
        else:
            print(f"{input_image_path} is not a valid image.")