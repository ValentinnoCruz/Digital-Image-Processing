# MyHEFunctions.py

# Import numpy
import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt



# --------------------------------------------
#            Computer Histogram
# --------------------------------------------

def compute_histogram(image_pixels): 
    hist = np.zeros(shape=(256))              
    for x in range(image_pixels.shape[0]):        
        for y in range(image_pixels.shape[1]):            
            hist[int(image_pixels[x][y])] += 1
            
    return hist
#     # using ravel we represent our img as a 1-dimensional vector
#     vectorized_image = image_pixels.ravel() 
#     histogram = np.zeros(shape=(256)) 
#     histogram = np.histogram(vectorized_image, 
#                             bins=256, 
#                             range=(0,255)) 
#     # to obtain te normalized histogram we take each value
#     # and then divide it by the total # of pixels
#     normalized_histogram = histogram[0]/vectorized_image.shape[0] 
#     return normalized_histogram

# # usually we should make sure that we are creating the correct
# # probablilty distribution. we can do this by checking that the values of
# # the histogram vector adds up to a total of '1'


# --------------------------------------------
#                 Equalize
# --------------------------------------------
def equalize( in_image_pixels ):
    # get image histogram
    histogram, bins = np.histogram(in_image_pixels.flatten(), 256, density=True)
    cdf = histogram.cumsum() # cumulative distribution function
    cdf = (256-1) * cdf / cdf[-1] # normalize

    # use linear interpolation of cdf to find new pixel values
    equalized_image = np.interp(in_image_pixels.flatten(), bins[:-1], cdf)

    eq_img = equalized_image.reshape(in_image_pixels.shape)
    return eq_img



def plot_histogram( hist ):
    # plot_histgram  Plots the length 256 numpy vector representing the normalized
    # histogram of a grayscale image.
    #
    # Syntax:
    #   plot_histogram( hist )
    #
    # Input:
    #   hist = The length 256 histogram vector..
    #
    # Output:
    #   none
    #
    # History:
    #   S. Newsam     10/23/2022   created



    # Import plotting functions from matplotlib.
    import matplotlib.pyplot as plt

    plt.bar( range(256), hist )

    plt.xlabel('intensity value');

    plt.ylabel('PMF'); 

    plt.show()
