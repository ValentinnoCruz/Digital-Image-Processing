# Import pillow
from PIL import Image, ImageOps
# Import numpy
import numpy as np
from numpy import asarray

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


newImage.show()
newImage.save('image.tif')


