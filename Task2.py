# Import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

# Read the image from file.
im = Image.open('Watertower.tif')



# check if its in grayscale
print("image mode is:", im.mode)


# Display Image on screen
im.show()

# Get access to the pixel values through the matrix im_gray_pixels.
im1_pixels = asarray(im)
print("array", im1_pixels)
