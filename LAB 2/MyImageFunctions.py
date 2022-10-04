# MyImageFunctions.py
# Import pillow

from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray
def myImageInverse( inImage_pixels ):



    # compute size of the matrix
    x = np.size(inImage_pixels, 0)
    y = np.size(inImage_pixels, 1)

    # emulate matrix numpy of the same exact size
    outImage = np.zeros((x,y), dtype=int)

    for i in range(x): # traverse through i
        for j in range(y): # traverse through j
            # now we get the difference between the two
            outImage[i][j] = 255 - inImage_pixels[i][j]


    # return the image
    return outImage;
