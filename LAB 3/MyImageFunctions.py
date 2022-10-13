# MyImageFunctions.py


# Import pillow
from PIL import Image, ImageOps


# Import numpy
import numpy as np
from numpy import asarray

# For sqrt(), floor()
import math

import matplotlib.image as img

def myImageResize( inImage_pixels, M, N, interpolation_method ):
    #< your implementation>
    m = img.imread('LAB 3\Lab_03_image.tif');

    # determining the length of original image
    w, h = m.shape[:2];

    # xNew and yNew are new width and
    # height of image required
    #after scaling
    xNew = int(w * 1 / 2);
    yNew = int(h * 1 / 2);

    # calculating the scaling factor
    # work for more than 2 pixel
    xScale = xNew/(w-1);
    yScale = yNew/(h-1);

    # using numpy taking a matrix of xNew
    # width and yNew height with
    # 4 attribute [alpha, B, G, B] values
    newImage = np.zeros([xNew, yNew, 4]);

    for i in range(xNew-1):
        for j in range(yNew-1):
            newImage[i + 1, j + 1]= m[1 + int(i / xScale),
                                    1 + int(j / yScale)]

    # Save the image after scaling
    img.imsave('scaled.png', newImage);

#def myRMSE( first_im_pixels, second_im_pixels ):
#< your implementation>


#def mybilinear(x1,y1,p1,x2,y2,p2,x3,y3,p3,x4,y4,p4,x5,y5):
#< your implementation>