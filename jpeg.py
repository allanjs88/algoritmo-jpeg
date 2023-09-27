import numpy as np
import cv2

# Load the image using OpenCV
image = cv2.imread("Carro.jpg")

#1. Color Space Conversion: Convert the image to YCbCr color space
ycbcr_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)


#2. Chroma Subsampling

# Apply chroma subsampling (e.g., 4:2:0 subsampling)
#subsampling_ratio = (2, 2)  # (horizontal subsampling factor, vertical subsampling factor)

# Perform subsampling on the Cb and Cr channels
#ycbcr_image[:, :, 1::] = cv2.resize(ycbcr_image[:, :, 1::], None, fx=1/subsampling_ratio[0], fy=1/subsampling_ratio[1], interpolation=cv2.INTER_LINEAR)

#3. Block Splitting: Split the image into 8x8 blocks.

#4. Discrete Cosine Transform (DCT): Perform the discrete cosine transform (DCT) on each channel
dct_image = np.zeros_like(ycbcr_image, dtype=np.float32)
for i in range(3):
    dct_image[:, :, i] = cv2.dct(np.float32(ycbcr_image[:, :, i]))

# 5. Quantize the DCT coefficients (you can define your quantization matrix)
quantization_matrix = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                                [12, 12, 14, 19, 26, 58, 60, 55],
                                [14, 13, 16, 24, 40, 57, 69, 56],
                                [14, 17, 22, 29, 51, 87, 80, 62],
                                [18, 22, 37, 56, 68, 109, 103, 77],
                                [24, 35, 55, 64, 81, 104, 113, 92],
                                [49, 64, 78, 87, 103, 121, 120, 101],
                                [72, 92, 95, 98, 112, 100, 103, 99]])

print(dct_image.shape)

quantized_dct_image = np.zeros_like(dct_image)
for i in range(3):
    quantized_dct_image[:, :, i] = np.round(dct_image[:, :, i] / quantization_matrix)

# Save the quantized DCT coefficients as a compressed image
cv2.imwrite("compressed_image.jpg", quantized_dct_image.astype(np.uint8))
