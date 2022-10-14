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

    # M and N are new width and
    # height of image required
    #after scaling
    M = int(w * 1 / 2);
    N = int(h * 1 / 2);

    # calculating the scaling factor
    # work for more than 2 pixel
    xScale = M/(w-1);
    yScale = N/(h-1);

    # using numpy taking a matrix of M
    # width and N height with
    # 4 attribute [alpha, B, G, B] values
    interpolation_method = np.zeros([M, N, 4]);

    for i in range(M-1):
        for j in range(N-1):
            interpolation_method[i + 1, j + 1]= m[1 + int(i / xScale),
                                    1 + int(j / yScale)]
    return interpolation_method

    # Save the image after scaling
    #img.imsave('scaled.png', newImage);

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

#def myRMSE( first_im_pixels, second_im_pixels ):
#< your implementation>





#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

def mybilinear(array_in, width_in, height_in, array_out, width_out, height_out):
    for i in range(height_out):
        for j in range(width_out):
            # Relative coordinates of the pixel in output space
            x_out = j / width_out
            y_out = i / height_out

            # Corresponding absolute coordinates of the pixel in input space
            x_in = (x_out * width_in)
            y_in = (y_out * height_in)

            # Nearest neighbours coordinates in input space
            x_prev = int(np.floor(x_in))
            x_next = x_prev + 1
            y_prev = int(np.floor(y_in))
            y_next = y_prev + 1

            # Sanitize bounds - no need to check for < 0
            x_prev = min(x_prev, width_in - 1)
            x_next = min(x_next, width_in - 1)
            y_prev = min(y_prev, height_in - 1)
            y_next = min(y_next, height_in - 1)
            
            # Distances between neighbour nodes in input space
            Dy_next = y_next - y_in;
            Dy_prev = 1. - Dy_next; # because next - prev = 1
            Dx_next = x_next - x_in;
            Dx_prev = 1. - Dx_next; # because next - prev = 1
            
            # Interpolate over 3 RGB layers
            for c in range(3):
                array_out[i][j][c] = Dy_prev * (array_in[y_next][x_prev][c] * Dx_next + array_in[y_next][x_next][c] * Dx_prev) \
                + Dy_next * (array_in[y_prev][x_prev][c] * Dx_next + array_in[y_prev][x_next][c] * Dx_prev)
                
    return array_out

















#     def mybilinear(x1,y1,p1,x2,y2,p2,x3,y3,p3,x4,y4,p4,x5,y5):
# #< your implementation>

# #@function
# #def mybilinear(pixelLocs=None,pixelVals=None,interpoLoc=None,*args,**kwargs):
#     varargin = mybilinear.varargin
#     nargin = mybilinear.nargin

#     #UNTITLED2 Summary of this function goes here
# #   Detailed explanation goes here
    
#     P51=(np.dot((p3 - p1),((interpoLoc(1) - pixelLocs(1)) / (pixelLocs(5) - pixelLocs(1))))) + p1
# # mybilinear.m:5
#     P52=(np.dot((p3 - p1),((interpoLoc(1) - pixelLocs(3)) / (pixelLocs(7) - pixelLocs(3))))) + p2
# # mybilinear.m:7
#     P5=(np.dot((P52 - P51),((interpoLoc(2) - pixelLocs(2)) / (pixelLocs(4) - pixelLocs(2))))) + P51
# # mybilinear.m:9
#     bilinearValue=copy(P5)
# # mybilinear.m:11
#     return bilinearValue
    
# if __name__ == '__main__':
#     pass
    