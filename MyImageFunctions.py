# MyImageFunctions.py
# Import pillow

from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray
def myImageInverse( inImage_pixels ):



# # This function takes as input a numpy matrix representing a grayscale image and
# # outputs another numpy matrix which is the image inverse of the input.
# # That is, for each pixel, output_value = 255 - input_value

# Syntax:
# out_numpy_matrix = myImageInverse( in_numpy_matrix )

# Input:
# in_numpy_matrix = the grayscale values of the input image

# Output:
# out_numpy_matrix = the grayscale of the inverse image

    # determine the size of input matrix
    x = np.size(inImage_pixels, 0)
    y = np.size(inImage_pixels, 1)
    # created new numpy matrix of the same size
    outImage = np.zeros((x,y), dtype=int)
    # applying the formula
    for i in range(x):
        for j in range(y):
            outImage[i][j] = 255 - inImage_pixels[i][j]
    # returning the output image
<<<<<<< HEAD
    return outImage;
=======
    return outImage;
            
>>>>>>> b6fcd64086e65d1eecc2d6800bea19d2b78b5e10
