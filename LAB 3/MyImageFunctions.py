import numpy as np
import math

#..........................................................
#                Root Mean Squared Error 
#..........................................................


def myImageResize(inImage_pixels, M, N, interpolation_method):

    #assert interpolation_method == 'nearest' or interpolation_method == 'bilinear'

    # set up empty array.
    ImageOut = np.zeros((M, N))

    # determining the length of original image
    h, w = inImage_pixels.shape
    # M and N are new width and height of image required after scaling
    wRat = w / N
    hrat = h / M

# -------------------------------------------
#      Nearest neighbor interpolation
# -------------------------------------------
    if interpolation_method == 'nearest': 
        for i in range(M):
            for j in range(N):
                y, x = int(j * wRat), int(i * hrat)
                ImageOut[i][j] = inImage_pixels[x][y]
# -------------------------------------------
#          Bilinear interpolation
# -------------------------------------------
    if interpolation_method == 'bilinear':
        for i in range(M):
            for j in range(N):
                y, x = j * wRat, i * hrat
                x_floor, y_floor = int(x), int(y)
                x_ceil, y_ceil = min(h - 1, int(math.ceil(x))), min(w - 1, int(math.ceil(y)))

                # Set our pixel location values
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

#..........................................................
#                Root Mean Squared Error 
#..........................................................

#  Here we are taking a comparision between two sets of values
#  This is done by looping through the pixels and comparing
#  the actual difference between the estimated and measured vals


def myRMSE(first_im_pixels, second_im_pixels):
#< your implementation>
    # Take the dimensions from the first pixels. 
	M, N = np.shape(first_im_pixels)

	
	# Find the RMSE by looping through pixels and comparing.
	rmse = 0
	for m in range(M):
		for n in range(N):
			rmse += (first_im_pixels[m,n] - second_im_pixels[m,n])**2
	
	rmse = np.sqrt(rmse/(M*N))
	
	return rmse

#----------------------------------------------------------
#----------------------------------------------------------
#----------------------------------------------------------

def mybilinear(x1,y1,p1,x2,y2,p2,x3,y3,p3,x4,y4,p4,x5,y5):
# #< your implementation>

    # Get Min_x, Max_x, Min_y, Max_y of x and y coordinates of 4 pixels.
    # Min_x = min(x1, x2, x3, x4)
    # Max_x = max(x1, x2, x3, x4)
    # Min_y = min(y1, y2, y3, y4)
    # Max_y = max(y1, y2, y3, y4)

    Min_x = min(np.floor(x1),np.floor(x2),np.floor(x3),np.floor(x4))
    Max_x = max(np.ceil(x1),np.floor(x2),np.floor(x3),np.floor(x4))
    Min_y = min((np.floor(y1),np.floor(y2),np.floor(y3),np.floor(y4)))
    Max_y = max((np.ceil(y1),np.floor(y2),np.floor(y3),np.floor(y4)))

    # if min x & max x are equal
    if (Min_x == Max_x):
        return p1
    # if min y & max y are equal
    if (Min_y == Max_y):
        return p1

    # if y min & max value are equivalent
    if (Min_x == Max_x): 
        totx = (Max_y - y5) * p1 + (y5 - Min_y) * p4
        return totx

    # if y min & max value are equivalent
    if (Min_y == Max_y): 
        min_max_y = (Max_x - x5) * p1 + (x5 - Min_x) * p4
        return min_max_y

    val_1 = (Max_x - x5) * p1 + (x5 - Min_x) * p2
    val_2 = (Max_x - x5) * p3 + (x5 - Min_x) * p4
    Bilinear = (Max_y - y5) * val_1 + (y5 - Min_y) * val_2

    return Bilinear
