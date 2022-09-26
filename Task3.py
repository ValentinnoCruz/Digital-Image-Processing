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



im_pixels = np.zeros(shape=(rows, cols), dtype=int)
for i in range(0, rows):
    for j in range(0, cols):
        im_pixels[i][j] = im_gray_rot[i][j]





# img = Image.new('RGB', im_pixels,)

# x = np.linspace(0, 1, 100)
# image = np.tile(x, (100, 1)).T

# img.save('image.png')
# img.show()

