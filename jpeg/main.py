from PIL import Image

# Open the image you want to compress
image = Image.open("Carro.jpg")

# Specify the compression quality (0-100, higher values mean better quality)
# You can adjust this value as needed
compression_quality = 1

# Save the compressed image
image.save("compressed_image2.jpg", format="JPEG", quality=compression_quality)
