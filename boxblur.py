# console application to pixelate image for cross stitching
# allows for user input to personalise pixelation experience
# this logic can be extended to a gui in the future for ease of use

# --- PACKAGES --- #

import subprocess, platform                  # necessary for clearing console
#import fcntl, termios, struct
import numpy as np
#simport pandas as pd
import cv2
import os.path                               # checks if image file exists
from matplotlib import pyplot as plt
from math import *
from PIL import Image                        # crops image
#from sklearn.cluster import KMeans           # kmeans for colour separation


# --- FUNCTIONS --- #

def clear_console():
    if (platform.system() == "Windows"):
        subprocess.Popen("cls", shell = True).communicate() 
    else: # Linux and Mac
        print("\033c", end = "")
        
# no clue what this does lol    `
def terminal_size():
    th, tw, hp, wp = struct.unpack('HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th
        
def welcome_screen():
    # check size of console
    clear_console()
    #print(terminal_size())
    print("############################################################")
    print("##                                                        ##")
    print("##                                                        ##")    
    print("##                                                        ##")
    print("##                                                        ##")
    print("##                                                        ##")
    print("##                                                        ##")
    print("##                                                        ##")
    print("##                                                        ##")
    print("##                                                        ##")
    print("##                                                        ##")
    print("##                                                        ##")
    print("##                                                        ##")
    print("##                                                        ##")
    print("##                                                        ##")
    print("############################################################")                                            

def import_img():
# input:
# output: 
# description: uses previous input from user to load 
    while True:
        name = input("Please enter the name of the original image: ")
        if os.path.isfile(name):             # checking file exists
            bgr_img = cv2.imread(name)       # import image
            b,g,r = cv2.split(bgr_img)       # get b,g,r
            rgb_img = cv2.merge([r,g,b])     # switch to rgb
            clear_console()
            break
        else:
            clear_console()
            print("Specified file does not exist.")
            continue

    return rgb_img

def define_dim(image):
# input:
# output:
# description: allows the user to input the desired dimensions of their cross-stitching. this might be defined by the size of their cross-stitching sheet(?). as each pixel needs to be square, this function checks the size of the original image and trims the sides if required

    # determining the shape of the input image
    img_height = image.shape[0]
    img_width = image.shape[1]
    
    # check if at least a 2x2 image
    if (img_height < 2 or img_height < 2):
        input("Your image is only " + str(img_height) + " pixels by " + str(img_width) + " pixels. Pixelation of this image is trivial. Press enter to exit.")
        exit() # exiting from the application. application needs to be relaunched with a suitable image (*** perhaps could edit this??)
    else:
        while True:
            desired_height = int(input("Please enter the desired height of your pixelated image: ")) # todo: add instruction for what height to input
            if (desired_height > img_height):
                print("Your desired height is greater than your image height. Please input a value less than or equal to " + str(img_height))
                continue
            else:
                break
        while True:
            desired_width = int(input("Please enter the desired width of your pixelated image: ")) # todo: add instruction
            if (desired_width > img_width):
                print("Your desired width is greater than your image width. Please input a value less than or equal to " + str(img_width))
                continue
            else:
                break
                
    # defining the number of pixels (from original image) that would be contained in one pixel (in the modified image)
    # recall that these two values need to be equal before pixelisation as each pixel is required to be a square
    dim_pixel_height = floor(img_height/desired_height)
    dim_pixel_width = floor(img_width/desired_width)
    
    if (dim_pixel_height != dim_pixel_width):
        while True:
            img_option = input("Your desired length and width do not fully align with the provided image. Would you like to trim edges (T) or add a buffer (B)?")
            if (img_option == "T"):
                
                # determining what the new pixel dimension will be - the smaller value becomes the pixel dimension
                if (dim_pixel_height < dim_pixel_width):
                    dim_pixel = dim_pixel_height 
                else: 
                    dim_pixel = dim_pixel_width
                    
                # determining how much needs to be trimmed from height and width
                height_trim = img_height - (dim_pixel * desired_height)
                width_trim = img_width - (dim_pixel * desired_width)
                
                # breaking down trimming into left/right and top/bottom
                top_trim_dim = floor(height_trim/2) # we prefer less to be taken from the top and left (hence the floor)
                bottom_trim_dim = top_trim_dim + (dim_pixel * desired_height)
                left_trim_dim = floor(width_trim/2)
                right_trim_dim = left_trim_dim + (dim_pixel * desired_width)
                    
                # cropping image accordingly --- NUMPY has NO TRIM!!
                im1 = image[left_trim_dim:right_trim_dim, top_trim_dim:bottom_trim_dim, :]
                break
            elif (img_option == "B"):
                # buffer
                break
            else:
                continue
                
    #return im1 # returns the resized image

    # this doesnt belong here !!!!!!!!!!!!!!!!!!!1
    mod_height = im1.shape[0]
    mod_width = im1.shape[1]
    
    out_height = int(mod_height/dim_pixel)
    out_width = int(mod_width/dim_pixel)

    final = np.zeros([out_height, out_width, 3]) # should this be zeros ??

    for bigy in range(out_height):
        for bigx in range(out_width):
            # this small for loop loops through the individual pixels in the image to collect them
            for lily in range(bigy * dim_pixel, (bigy + 1) * dim_pixel):
                    for lilx in range(bigx * dim_pixel, (bigx + 1) * dim_pixel):
                        # square each element's RGB and then append them to the list of RGB within the bigger cell
                        final[bigy][bigx][0] += (im1[lily][lilx][0])**2 # how can i do this in 1 line # for some reason, np.square wasn't working here (?)
                        final[bigy][bigx][1] += (im1[lily][lilx][1])**2
                        final[bigy][bigx][2] += (im1[lily][lilx][2])**2

            #take the square root of each pixel in the pixelated image
            final[bigy][bigx] = np.round(np.sqrt((final[bigy][bigx])/dim_pixel**2))

    final = (final.astype(np.uint8)) # wouldn't plot correctly without this
    
    #fig, ax = plt.subplots()
    
    plt.imshow(final)
    plt.xticks(np.arange(-0.5,out_width-0.5, 1))
    plt.yticks(np.arange(-0.5,out_height -0.5, 1))
    #plt.xticks([]), plt.yticks([])   # to hide tick values on X and Y axis
    #plt.gcs().axes.get_yaxis().set_visible(False)
    #plt.axis('off')
    plt.grid(which = 'major', axis = 'both', linestyle = '-', color = 'k', linewidth = 1)

    
    plt.savefig("output_img.jpg", bbox_inches = 'tight', pad_inches = 0, dpi = 400)
    plt.show()
    cv2.waitKey(0)
    
    return im1
                
def average_col():
# input:
# output:
# description: perform averaging function on each part of the array
# calculating the size of each smaller square (for the for loop)
    out_width = int(img_width/dim_pixel)
    out_height = int(img_height/dim_pixel)

    final = np.zeros([out_height, out_width, 3]) # should this be zeros ??

    for bigy in range(out_height):
        for bigx in range(out_width):
            # this small for loop loops through the individual pixels in the image to collect them
            for lily in range(bigy * dim_pixel, (bigy + 1) * dim_pixel):
                    for lilx in range(bigx * dim_pixel, (bigx + 1) * dim_pixel):
                        # square each element's RGB and then append them to the list of RGB within the bigger cell
                        final[bigy][bigx][0] += (rgb_img[lily][lilx][0])**2 # how can i do this in 1 line # for some reason, np.square wasn't working here (?)
                        final[bigy][bigx][1] += (rgb_img[lily][lilx][1])**2
                        final[bigy][bigx][2] += (rgb_img[lily][lilx][2])**2

            #take the square root of each pixel in the pixelated image
            final[bigy][bigx] = np.round(np.sqrt((final[bigy][bigx])/dim_pixel**2))

    final = (final.astype(np.uint8)) # wouldn't plot correctly without this
    
    
# def mid_pixel_sampling

    
def k_means(img):
    img = img.reshape((img.shape[1]*img.shape[0], 3))
    
    kmeans = KMeans(n_clusters = 10)
    s = kmeans.fit(img)
    
    labels = kmeans.labels_
    print(labels)
    labels = list(labels)
    
    centroid = kmeans.cluster_centers_
    print(centroid)
    
    percent = []
    for i in range(len(centroid)):
        j = labels.count(i)
        j = j/(len(labels))
        percent.append(j)
    print(percent)
    
    plt.pie(percent,colors = np.array(centroid/255), labels = np.arange(len(centroid)))
    plt.show()
    cv2.waitKey(0)
    
# def elbow
    
def print_img():
    plt.imshow(final)
    plt.xticks([]), plt.yticks([])   # to hide tick values on X and Y axi/s
    plt.savefig("output_img.jpg", bbox_inches = 'tight', pad_inches = 0, dpi = 400)
    plt.show()
    cv2.waitKey(0)

# --- MAIN FUNCTION --- #

def main():
# main function
    welcome_screen()
    rgb = import_img() # import image
    redef = define_dim(rgb) # trim as needed
    #average_col() # perform averaging function on each part of the array
    #k_means(redef)
    #print_img()
    
    # check 
    # function to combine it again
    # plot image

if __name__ == '__main__':
    main()
