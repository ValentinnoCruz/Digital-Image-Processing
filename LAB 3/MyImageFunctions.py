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
    assert interpolation_method == 'nearest' or interpolation_method == 'bilinear'
    ImageOut = np.zeros((M,N))

    # determining the length of original image
    w,h = inImage_pixels.shape

    # determining the length of original image
    #w, h = ImageOut.shape[:2];

    # M and N are new width and height of image required after scaling
    wRatio = w/N
    hRation = h/M

    if interpolation_method == 'nearest':
        for i in range(M):
            for j in range(N):
                y, x = int(j * wRatio), int(i * hRation)
                ImageOut[i][j] = inImage_pixels[x][y]

    else: #interpolation_method == 'bilinear'
        for i in range(M):
            for j in range(N):
                y, x = j * w, i * h
                x_floor, y_floor = int(x), int(y)
                x_ceil, y_ceil = min(hRation - 1, int(math.ceil(x))), min(wRatio - 1, int(math.ceil(y)))

                p1 = inImage_pixels[x_floor, y_floor]
                p2 = inImage_pixels[x_floor, y_ceil]
                p3 = inImage_pixels[x_ceil, y_floor]
                p4 = inImage_pixels[x_ceil, y_ceil]

                ImageOut[i, j] = mybilinear(x_floor, y_floor, p1, 
                                            x_floor, y_ceil, p2, 
                                            x_ceil, y_floor, p3, 
                                            x_ceil, y_ceil, p4, 
                                            x, y)

    return ImageOut
    # using numpy taking a matrix of M
    # width and N height with
    # 4 attribute [alpha, B, G, B] values
    # interpolation_method = np.zeros([M, N, 4]);

    # for i in range(M-1):
    #     for j in range(N-1):
    #         interpolation_method[i + 1, j + 1]= m[1 + int(i / xScale),
    #                                 1 + int(j / yScale)]
    # return interpolation_method

    # Save the image after scaling
    #img.imsave('scaled.png', newImage);

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

#function rmse()
# def myRMSE(first_im_pixels, second_im_pixels):
#     answer = 1 / len(first_im_pixels)

#   #find the sum from i = 0 to n of (xi - ni) * (xi - ni)
#     sum = 0
#     for i in range(len(first_im_pixels)):
#         sum += (first_im_pixels[i] - second_im_pixels[i]) * (first_im_pixels[i] - second_im_pixels[i])
#         answer *= sum

# #return sqrt of answer
#     return math.sqrt(answer)

#first_im_pixels = [1, 3, 5]
#second_im_pixels = [2, 1, 4]
#-----------------------------------------------------------------
def myRMSE(first_im_pixels, second_im_pixels):
    sse = ((first_im_pixels - second_im_pixels) ** 2).sum()
    return np.sqrt(sse / (first_im_pixels.shape[0] * first_im_pixels.shape[1]))


# def myRMSE(first_im_pixels, second_im_pixels):
#     r,c=first_im_pixels.shape
# # myRMSE.m:2
    
#     pixelDiff=0
# # myRMSE.m:4
#     for x in np.arange(1,r).reshape(-1):
#         for y in np.arange(1,c).reshape(-1):
#             pixel_diff=pixelDiff + (((first_im_pixels(x,y)) - (second_im_pixels(x,y))) ** 2).sum()
# # myRMSE.m:8
#     return np.sqrt(pixel_diff / (np.dot(r,c)))
# # myRMSE.m:12
#     #return RMSE
#-----------------------------------------------------------------

# def myRMSE(first_im_pixels, second_im_pixels):
#     #< your implementation>
#     Val = np.sum(np.sqrt(first_im_pixels - second_im_pixels)) / first_im_pixels.shape[0] * first_im_pixels.shape[1]

#     return Val
#-----------------------------------------------------------------
    
    # diffs = 0
    # for p, a in zip(first_im_pixels, second_im_pixels):
    #     diffs += (p - a)**2
    # return diffs / len(first_im_pixels)
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
    