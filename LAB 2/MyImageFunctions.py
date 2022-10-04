# MyImageFunctions.py
# Import pillow

from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray
def myImageInverse( inImage_pixels ):



    # compute size of the matrix
    cols = np.size(inImage_pixels, 0)
    rows = np.size(inImage_pixels, 1)

    # emulate matrix numpy of the same exact size
    outImage = np.zeros((cols,rows), dtype=int)

    for col in range(cols): # traverse through i
        for row in range(rows): # traverse through j
            # now we get the difference between the two
            outImage[col][row] = 255 - inImage_pixels[col][row]


    # return the image
    return outImage;
