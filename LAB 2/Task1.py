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

# ===================
#   access pixel val
# ===================
# Get access to the pixel values through the matrix im_gray_pixels.
im_gray_pixels = asarray(im_gray)

# ===================
#   Max Pixel Value
# ===================
rows, cols = im_gray_pixels.shape
for row in range(rows):
    for col in range(cols):
        # get the current pixel value
        current_pixel_value = im_gray_pixels[row, col]
        # Manipulating your pixel values
        # for example: print pixel values that are greater than 200
        if current_pixel_value >= 240:
            print("Max Pixel Value is: ", current_pixel_value)


# copy pixel values from 'im_gray_pixels'

# ===================
#  img dimensions
# ===================

# Determine the dimensions of the image.
rows, cols = im_gray_pixels.shape
print("Image size of gray : ", rows, "rows x", cols, "columns")


# =======================
#   Gray Rotate 90-deg
# =======================

# otate im_gray 1x @yaxis and set it to 'a'
a = np.rot90(im_gray, 1, (0,1))
im_gray_rot = asarray(a) # set the array of 'a' to im_gray_rot
rows, cols = im_gray_rot.shape
print("Image size of rotated gray : ", rows, "rows x", cols, "columns")




# ===================
#   access pixel val
# ===================
# Get access to the pixel values through the matrix im_gray_pixels.
im_gray_rot_pixels = asarray(im_gray)

# ===================
#   Max Pixel Value
# ===================
rows, cols = im_gray_rot_pixels.shape
for row in range(rows):
    for col in range(cols):
        # get the current pixel value
        current_pixel_value = im_gray_rot_pixels[row, col]
        # Manipulating your pixel values
        # for example: print pixel values that are greater than 200
        if current_pixel_value >= 240:
            print("Max Pixel Value gray rotate is: ", current_pixel_value)






# ===============================
#   display and save gray_rot
# ===============================

# set pixels of gray_rot as an array
im_gray_rot_pixels = asarray(im_gray_rot)

# Create an image from im_gray_rot_pixels.
im_gray_rot = Image.fromarray(np.uint8(im_gray_rot_pixels))

# Display the image.
im_gray_rot.show()

# Save the image.
im_gray_rot.save("Beginnings_grayscale_Rotated.jpg")




#---------------------------------------------------
#---------------------------------------------------
#---------------------------------------------------
#---------------------------------------------------
#---------------------------------------------------




# =========================
#   access pixel val
# =========================
# Get access to the pixel values through the matrix im_gray_pixels.
im_pixels = asarray(im)


# =========================
#    Rotate 90-deg
# =========================

# otate im_gray 1x @yaxis and set it to 'a'
b = np.rot90(im_pixels, 1, (1,0))
im_rot = asarray(b) # set the array of 'a' to im_gray_rot


# ===============================
#   display and save rotation
# ===============================

# set pixels of gray_rot as an array
im_rot_pixels = asarray(im_rot)

# Create an image from im_gray_rot_pixels.
im_rot = Image.fromarray(np.uint8(im_rot_pixels))

# Display the image.
im_rot.show()

# Save the image.
im_rot.save("Beginnings_Rotated.jpg")

# ===================
#   Max Pixel Value
# ===================
rows, cols, zeds = im_pixels.shape
for row in range(rows):
    for col in range(cols):
        for zed in range(zeds):
            # get the current pixel value
            current_pixel_value2 = im_pixels[row, col, zed]
            # Manipulating your pixel values
            # for example: print pixel values that are greater than 200
            if current_pixel_value2 == 255:
                print("Max Pixel Value is: ", current_pixel_value2)







# rows, cols = im_gray_pixels.shape
# im_gray_rot = np.zeros([rows, cols], dtype = np.uint8)

# for i in range (rows):
#     for j in range (cols):
#         im_gray_rot[i,j] = im_gray_rot[j-1, i-1]

# print("here we goooooo", im_gray_rot[i,j])
# # ===============================