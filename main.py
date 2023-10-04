import os
from utils import is_image, get_file_extension, create_dir, encode_and_save_image, decode_and_save_image

IMAGE_PATH = "images/"
ENCRYPTED_JPEG_IMAGE_PATH = "jpeg_images/"
ENCRYPTED_WEBP_IMAGE_PATH = "webp_images/"

def generate_input_images(is_jpeg, images_path, dest_path):
    create_dir(dest_path)
    images = os.listdir(images_path)

    for image in images:
        print("Imagen: "+ image)
        if is_image(image):
            extension = get_file_extension(image)
            input_image_path = images_path + image

            encrypted_images_path = dest_path + image
            encrypted_images_path = encrypted_images_path.replace(extension, '_2.jpg')

            encoded_path = encode_and_save_image(input_image_path, 'JPEG' if is_jpeg else 'WEBP')
            decode_and_save_image(encoded_path, encrypted_images_path)
        else:
            print(f"{image} is not a valid image.")

if __name__ == '__main__':
    generate_input_images(True, IMAGE_PATH, ENCRYPTED_JPEG_IMAGE_PATH)
    generate_input_images(False, IMAGE_PATH, ENCRYPTED_WEBP_IMAGE_PATH)