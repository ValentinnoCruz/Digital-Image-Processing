# Import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

# Read the image from file.
im = Image.open('Beginnings.jpg')

# Show the image.
im.show()

# Convert image to gray scale.
im_gray = ImageOps.grayscale(im)

# Show the grayscale image.
im_gray.show()

# Get access to the pixel values through the matrix im_gray_pixels.
im_gray_pixels = asarray(im_gray)

# Create a new matrix w/ no pixel difference .
crop_rows = rows - 0
crop_cols = cols - 0
im_gray_crop_pixels = np.zeros(shape=(crop_rows, crop_cols))




# Determine the dimensions of the image.
rows, cols = im_gray_pixels.shape
print("Image size is: ", rows, "rows x", cols, "columns")

