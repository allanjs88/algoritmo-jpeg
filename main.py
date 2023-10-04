import os
from utils import is_image, get_file_extension, create_dir
from jpeg.jpeg_pillow import encode_and_save_image_jpeg, decode_and_save_image_jpeg
from webp.webp_pillow import encode_and_save_image_webp, decode_and_save_image_webp

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

            if is_jpeg:
                encoded_path = encode_and_save_image_jpeg(input_image_path)
                decode_and_save_image_jpeg(encoded_path, encrypted_images_path)
            else:
                encoded_path = encode_and_save_image_webp(input_image_path)
                decode_and_save_image_webp(encoded_path, encrypted_images_path)
        else:
            print(f"{image} is not a valid image.")

if __name__ == '__main__':
    generate_input_images(True, IMAGE_PATH, ENCRYPTED_JPEG_IMAGE_PATH)
    generate_input_images(False, IMAGE_PATH, ENCRYPTED_WEBP_IMAGE_PATH)