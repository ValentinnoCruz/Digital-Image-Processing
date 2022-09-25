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


# print out max pixel value 
biggest = np.amax(im_gray_pixels)
print("the max pixel value is", biggest)


# Determine the dimensions of the image.
rows, cols = im_gray_pixels.shape
print("Image size is: ", rows, "rows x", cols, "columns")

