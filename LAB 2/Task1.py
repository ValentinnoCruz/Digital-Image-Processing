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
rows, cols = im_gray_pixels.shape

for row in range(rows):
    for col in range(cols):
        # get the current pixel value
        current_pixel_value = im_gray_pixels[row, col]
        # Manipulating your pixel values
        # for example: print pixel values that are greater than 200
        if current_pixel_value >= 240:
            print("Max Pixel Value is: ", current_pixel_value)




# # print out max pixel value 
# biggest = np.amax(im_gray_pixels)
# print("the max pixel value is", biggest)


# a = np.array(im_gray)
# print(np.transpose(a))
#np.rot90(im_gray, k=2, axes=(0,1) )
#im_gray.show()


# Determine the dimensions of the image.
rows, cols = im_gray_pixels.shape
print("Image size is: ", rows, "rows x", cols, "columns")

