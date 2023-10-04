import os
from utils import is_image, get_file_extension, create_dir
from jpeg.jpeg_pillow import encode_and_save_image, decode_and_save_image

IMAGE_PATH = "images/"
ENCRYPTED_IMAGE_PATH = "encrypted_images/"

if __name__ == '__main__':

    create_dir(ENCRYPTED_IMAGE_PATH)
    images = os.listdir(IMAGE_PATH)

    for image in images:
        print("Imagen: "+ image)
        if is_image(image):
            extension = get_file_extension(image)
            input_image_path = IMAGE_PATH + image

            encrypted_images_path = ENCRYPTED_IMAGE_PATH + image
            encrypted_images_path = encrypted_images_path.replace(extension, '_2.jpg')

            encoded_path = encode_and_save_image(input_image_path)
            decode_and_save_image(encoded_path, encrypted_images_path)
        else:
            print(f"{image} is not a valid image.")