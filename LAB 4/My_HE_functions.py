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


# --------------------------------------------
#                 Plot Hist
# --------------------------------------------
def plot_histogram( hist ):

    # Import plotting functions from matplotlib.
    import matplotlib.pyplot as plt

    plt.bar( range(256), hist )

    plt.xlabel('intensity value');

    plt.ylabel('PMF'); 

    plt.show()
