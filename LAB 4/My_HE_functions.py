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
            
#     return hist
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

#     #Equalize 
# #   Takes in as input a grayscale image 256 bits and returns the histogram
# #   equalized version.
    
#     #gets index sizes
#     mn=np.size(in_image_pixels)
# # equalize.m:7
#     m=mn*1
# # equalize.m:8
#     n=mn*2
# # equalize.m:9
#     #create a matrix for final processed image
#     finalImage=np.zeros(m,n)
# # equalize.m:12
#     #store probability values on a 256 vector
#     histogram=compute_histogram(in_image_pixels)
# # equalize.m:15
#     #get transformation vector that is size 256
#     transformation=histogram_transform(compute_histogram(in_image_pixels))
# # equalize.m:18
#     #plot calculated values to final image
#     for i in np.arange(1,m).reshape(-1):
#         for j in np.arange(1,n).reshape(-1):
#             finalImage[i,j]=transformation(in_image_pixels(i,j) + 1)
# # equalize.m:23
    
#     #calculate histogram of final transformed image
#     histogram2=compute_histogram(finalImage)
# # equalize.m:28
#     finalImage=np.uint8(finalImage)
# # equalize.m:30
#     #PLOT EVERYTHING
#     #figure
#     plt.subplot(2,2,1)
#     plot_histogram(histogram)
#     plt.subplot(2,2,2)
#     plot_histogram(histogram2)
#     plt.subplot(2,2,3)
#     plt.imshow(in_image_pixels)
#     plt.subplot(2,2,4)
#     plt.imshow(finalImage)
#     image=np.double(image)
# # equalize.m:40
#     finalImage=np.double(finalImage)
# # equalize.m:41
#     np.disp('Mean Origianl')
#     np.disp(np.mean(np.ravel(image)))
#     np.disp('Standard Deviation Origianl')
#     np.disp(np.std(np.ravel(image)))
#     np.disp('Mean Equalized')
#     np.disp(np.mean(np.ravel(finalImage)))
#     np.disp('Standard Deviation Equalized')
#     np.disp(np.std(np.ravel(finalImage)))
#     outputArg1=0
# # equalize.m:55
#     #PRINT MEAN AND STANDARD DEVIATION
    
#     return outputArg1



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
