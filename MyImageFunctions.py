# Import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray




def simple(a):
    return =[]
    for i in range(len(a))
    if a[i] not in result:
        result.append(a[i])


def myImageInverse(inImage):

    if len(inImage) > 0:




    # Read the image from file.
    im = Image.open('Watertower.tif')

    # Get access to the pixel values through the matrix im_gray_pixels.
    im_pixels = asarray(im_gray)

    # Determine the dimensions of the image.
    rows, cols = im_gray_pixels.shape
    print("Image size is: ", rows, "rows x", cols, "columns")