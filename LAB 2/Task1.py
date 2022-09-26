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

# --------------------------------
#       get max pixel value
# --------------------------------
rows, cols = im_gray_pixels.shape
for row in range(rows):
    for col in range(cols):
        # get the current pixel value
        current_pixel_value = im_gray_pixels[row, col]
        # Manipulating your pixel values
        # for example: print pixel values that are greater than 200
        if current_pixel_value >= 240:
            print("Max Pixel Value is: ", current_pixel_value)


# --------------------------------
#     rotate matrix 90 deg ccw
# --------------------------------
# otate im_gray 1x @yaxis and set it to 'a'
a = np.rot90(im_gray, 1, (0,1))
im_gray_rot = asarray(a) # set the array of 'a' to im_gray_rot


# --------------------------------
#    plug into rotated matrix
# --------------------------------
x = np.size(im_gray_rot, 0)
y = np.size(im_gray_rot, 1)

im_new = np.zeros(shape=(x,y), dtype=int)
for i in range(x):
    for j in range(y):
        im_new[i][j] = im_gray_rot[i][j]


# set pixels of gray_rot as an array
im_gray_rot_pixels = asarray(im_gray_rot)

# Create an image from im_gray_rot_pixels.
im_gray_rot = Image.fromarray(np.uint8(im_gray_rot_pixels))

# Display the image.
im_gray_rot.show()

# Save the image.
im_gray_rot.save("Beginnings_grayscale_Rotated.jpg")




#============================================
#           second rotation
#============================================



# Get access to the pixel values through the matrix im_gray_pixels.
im_pixels = asarray(im)


# --------------------------------
#     rotate matrix 90 deg cw
# --------------------------------

# otate im_gray 1x @yaxis and set it to 'a'
b = np.rot90(im_pixels, 1, (1,0))
im_rot = asarray(b) # set the array of 'a' to im_gray_rot


# --------------------------------
#   display and save rotation
# --------------------------------

# set pixels of gray_rot as an array
im_rot_pixels = asarray(im_rot)

# Create an image from im_gray_rot_pixels.
im_rot = Image.fromarray(np.uint8(im_rot_pixels))

# Display the image.
im_rot.show()

# Save the image.
im_rot.save("Beginnings_Rotated.jpg")
