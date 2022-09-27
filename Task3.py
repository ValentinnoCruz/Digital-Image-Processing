# Import pillow
from PIL import Image, ImageOps
# Import numpy
import numpy as np
from numpy import asarray
import math

# The size of the gradient image.
rows = 100
cols = 256


# Create a numpy matrix of this size.
im_pixels = np.zeros(shape=(rows, cols))


# 256 values between 255 - 0 (back - white)
x = np.linspace(255, 0, 256)

#repeat the vector 100 times
image2_grad = np.tile(x, (100, 1)).T

#flip image 90degrees
a = np.rot90(image2_grad, 1, (1,0))
image_pix = asarray(a) # set as an array

#Generate image from array.
newImage = Image.fromarray(np.uint8(image_pix))




#--------------------------
# get average pixel value
#--------------------------
x = np.size(image_pix, 0)
y = np.size(image_pix, 1)



total =0
for i in range(x):
    for j in range(y):
        total+=image_pix[(i,j)]
    b=x*y
mean=(total)/b
print("Mean Value is: ",np.mean(mean))

newImage.show()
newImage.save('image.tif')


# total =0
# for i in range(0, cols):
#     for j in range(0, rows):
#         total+= image_pix.getpixel((i,j))[0]

# mean = total/(rows * cols)
# print(mean)

