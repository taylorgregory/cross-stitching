# console application to pixelate image for cross stitching
# allows for user input to personalise pixelation experience

# --- PACKAGES --- #

import numpy as np
import cv2
from matplotlib import pyplot as plt
from math import *

# --- FUNCTIONS --- #

def import_img():
# input:
# output: 
# description: uses previous input from user to load 
    name = input("Please enter the name of the original image: ")
    bgr_img = cv2.imread(name)       # import image
    b,g,r = cv2.split(bgr_img)       # get b,g,r
    rgb_img = cv2.merge([r,g,b])     # switch to rgb
    return rgb_img

def define_dim(image):
# input:
# output:
# description: allows the user to input the desired dimensions of their cross-stitching. this might be defined by the size of their cross-stitching sheet(?). as each pixel needs to be square, this function checks the size of the original image and trims the sides if required

    # determining the shape of the input image
    img_height = image.shape[0]
    img_width = image.shape[1]
    
    # check if at least a 2x2 image
    
    # determining the shape of the output image
    desired_height = input("Please enter the desired height of your pixelated image: ")
    desired_width = input("Please enter the desired height of your pixelated image: ")
    
    # check if desired width is less than
    
    # check is desired 
    
    # checking if a slight trim of edges is necessary
    
    # trim or buffer?
    
def average_col():
# perform averaging function on each part of the array
    print(hey)
    
def
    
def combine_averaged():

# --- MAIN FUNCTION --- #

def main():
# main function
    rgb = import_img() # import image
    define_dim(rgb) # trim as needed
    average_col() # perform averaging function on each part of the array
    
    # check 
    # function to combine it again
    # plot image
    
if __name__ == "__main__": # this line is unnecessary in python 3?
    main()
    

    
    

# --- MISCELLANEOUS GARBAGE --- #

# specifying that we want the final image to be a 6 x 8 image
pixel_dim = 70

# checking if it is a multiple, if not, we trim from all edges

# calculating the size of each smaller square (for the for loop)
out_width = int(img_width/pixel_dim)
out_height = int(img_height/pixel_dim)

final = np.zeros([out_height, out_width, 3]) # should this be zeros ??

for bigy in range(out_height):
	for bigx in range(out_width):
		# this small for loop loops through the individual pixels in the image to collect them
		for lily in range(bigy * pixel_dim, (bigy + 1) * pixel_dim):
				for lilx in range(bigx * pixel_dim, (bigx + 1) * pixel_dim):
					# square each element's RGB and then append them to the list of RGB within the bigger cell
					final[bigy][bigx][0] += (rgb_img[lily][lilx][0])**2 # how can i do this in 1 line # for some reason, np.square wasn't working here (?)
					final[bigy][bigx][1] += (rgb_img[lily][lilx][1])**2
					final[bigy][bigx][2] += (rgb_img[lily][lilx][2])**2

		#take the square root of each pixel in the pixelated image
		final[bigy][bigx] = np.round(np.sqrt((final[bigy][bigx])/pixel_dim**2))

final = (final.astype(np.uint8)) # wouldn't plot correctly without this

plt.imshow(final)
plt.xticks([]), plt.yticks([])   # to hide tick values on X and Y axis
plt.savefig("output_img.jpg", bbox_inches = 'tight', pad_inches = 0, dpi = 400)
plt.show()
cv2.waitKey(0)
