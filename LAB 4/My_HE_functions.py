# MyHEFunctions.py

# Import numpy
import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

def histogram_transform(histogram):
    #Histogram Transform
#   Takes in a histogram as input and returns a transformation vector 256
#   bit
    
    #create empty space to store values
    transformation=np.zeros(1,256)
# histogram_transform.m:7
    
    for i in np.arange(1,256).reshape(-1):
        for j in np.arange(1,i).reshape(-1):
            transformation[i]=transformation(i) + histogram(j)
# histogram_transform.m:12
    
    
    #Multiply by total number of values
    for k in np.arange(1,256).reshape(-1):
        transformation[k]=round(np.dot(transformation(k),(255)))
# histogram_transform.m:18
    
    return transformation
    



#def compute_histogram( image_pixels ):
def compute_histogram(image_pixels):

    #Compute Histogram
#   Takes in grayscale image and outputs a vector histogram of size 256
    
    m,n=np.shape(image_pixels)

    
    prob=np.zeros(shape=(1,256))
# compute_histogram.m:10
    
    for i in np.arange(1,m).reshape(-1):
        for j in np.arange(1,n).reshape(-1):
            prob[image_pixels[i,j] + 1] = prob(image_pixels(i, j) + 1) +1
# compute_histogram.m:15
    
    
    for f in np.arange(1,256).reshape(-1):
        prob[f]=((prob(f)) / (np.dot(m,n)))
# compute_histogram.m:20
    
    histogram=np.copy(prob)
# compute_histogram.m:23
    return histogram



def equalize( in_image_pixels ):

#def equalize(image=None,*args,**kwargs):

    #Equalize 
#   Takes in as input a grayscale image 256 bits and returns the histogram
#   equalized version.
    
    #gets index sizes
    mn=np.size(in_image_pixels)
# equalize.m:7
    m=mn(1)
# equalize.m:8
    n=mn(2)
# equalize.m:9
    #create a matrix for final processed image
    finalImage=np.zeros(m,n)
# equalize.m:12
    #store probability values on a 256 vector
    histogram=compute_histogram(in_image_pixels)
# equalize.m:15
    #get transformation vector that is size 256
    transformation=histogram_transform(compute_histogram(in_image_pixels))
# equalize.m:18
    #plot calculated values to final image
    for i in np.arange(1,m).reshape(-1):
        for j in np.arange(1,n).reshape(-1):
            finalImage[i,j]=transformation(in_image_pixels(i,j) + 1)
# equalize.m:23
    
    #calculate histogram of final transformed image
    histogram2=compute_histogram(finalImage)
# equalize.m:28
    finalImage=np.uint8(finalImage)
# equalize.m:30
    #PLOT EVERYTHING
    #figure
    plt.subplot(2,2,1)
    plot_histogram(histogram)
    plt.subplot(2,2,2)
    plot_histogram(histogram2)
    plt.subplot(2,2,3)
    plt.imshow(in_image_pixels)
    plt.subplot(2,2,4)
    plt.imshow(finalImage)
    image=np.double(image)
# equalize.m:40
    finalImage=np.double(finalImage)
# equalize.m:41
    np.disp('Mean Origianl')
    np.disp(np.mean(np.ravel(image)))
    np.disp('Standard Deviation Origianl')
    np.disp(np.std(np.ravel(image)))
    np.disp('Mean Equalized')
    np.disp(np.mean(np.ravel(finalImage)))
    np.disp('Standard Deviation Equalized')
    np.disp(np.std(np.ravel(finalImage)))
    outputArg1=0
# equalize.m:55
    #PRINT MEAN AND STANDARD DEVIATION
    
    return outputArg1



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
