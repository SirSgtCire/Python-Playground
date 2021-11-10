# Importing the OpenCV library
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Script Header
print("OpenCV Tutorial: https://www.geeksforgeeks.org/opencv-python-tutorial/")

# Script Variables
ImagePath = r"Images/StarryNight.jpg"


# Reading the image using imread() function
StarryNightImage = cv2.imread(ImagePath, cv2.IMREAD_COLOR)

# Extracting the height and width of an image
h, w = StarryNightImage.shape[:2]
# Displaying the height and width
print("Height = {},  Width = {}".format(h, w))

# Extracting RGB values.
# Here we have randomly chosen a pixel
# by passing in 100, 100 for height and width.
(B, G, R) = StarryNightImage[100, 100]

# Displaying the pixel values
print("R = {}, G = {}, B = {}".format(R, G, B))

# We can also pass the channel to extract
# the value for a specific channel
B = StarryNightImage[100, 100, 0]
print("B = {}".format(B))

# We will calculate the region of interest
# by slicing the pixels of the image
roi = StarryNightImage[100 : 500, 200 : 700]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

# resize() function takes 2 parameters,
# the image and the dimensions
resize = cv2.resize(StarryNightImage, (800, 800))
cv2.imshow("RESIZE", resize)
cv2.waitKey(0)

# Calculating the ratio
ratio = 800 / w

# Creating a tuple containing width and height
dim = (800, int(h * ratio))

# Resizing the image
resize_aspect = cv2.resize(StarryNightImage, dim)
cv2.imshow("RESIZE_ASPECT", resize_aspect)
cv2.waitKey(0)

# Calculating the center of the image
center = (w // 2, h // 2)

# Generating a rotation matrix
matrix = cv2.getRotationMatrix2D(center, -45, 1.0)
cv2.imshow("MATRIX", matrix)
cv2.waitKey(0)

# Performing the affine transformation
rotated = cv2.warpAffine(StarryNightImage, matrix, (w, h))
cv2.imshow("ROTATED", rotated)
cv2.waitKey(0)

# We are copying the original image,
# as it is an in-place operation.
StarryNightCopy1 = StarryNightImage.copy()

# Using the rectangle() function to create a rectangle.
rectangle = cv2.rectangle(StarryNightCopy1, (1500, 900), (600, 400), (255, 0, 0), 2)
cv2.imshow("RECTANGLE", rectangle)
cv2.waitKey(0)

# Copying the original image
StarryNightCopy2 = StarryNightImage.copy()

# Adding the text using putText() function
text = cv2.putText(StarryNightCopy2, "OpenCV Demo", (500, 550),
                   cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)
cv2.imshow("TEXT", text)
cv2.waitKey(0)

# Using cv2.imread() method
# Using 0 to read image in grayscale mode
graiscale = cv2.imread(ImagePath, 0)

# Displaying the image
cv2.imshow("GRAISCALE", graiscale)
cv2.waitKey(0)

# path to input images are specified and
# images are loaded with imread command
TempleImage = cv2.imread("Images/Temple.jpg")
StarsImage = cv2.imread("Images/Stars.jpg")

# cv2.addWeighted is applied over the
# image inputs with applied parameters
weightedSum = cv2.addWeighted(TempleImage, 0.5, StarsImage, 0.4, 0)

# the window showing output image
# with the weighted sum
cv2.imshow("WEIGHTED_IMAGE", weightedSum)
cv2.waitKey(0)

# path to input images are specified and
# images are loaded with imread command
WhiteStarImage = cv2.imread("Images/WhiteStar.jpg")
WhiteDiamondImage = cv2.imread("Images/WhiteDiamond.jpg")

# cv2.subtract is applied over the
# image inputs with applied parameters
sub = cv2.subtract(WhiteStarImage, WhiteDiamondImage)

# the window showing output image
# with the subtracted image
cv2.imshow("SUBTRACTED_IMAGE", sub)
cv2.waitKey(0)

# path to input images are specified and
# images are loaded with imread command
HalfAndHalfImage = cv2.imread("Images/HalfAndHalf.jpg")
WhiteOvalImage = cv2.imread("Images/WhiteOval.jpg")

# cv2.bitwise_and is applied over the
# image inputs with applied parameters
dest_and = cv2.bitwise_and(HalfAndHalfImage, WhiteOvalImage, mask = None)

# the window showing output image
# with the Bitwise AND operation
# on the input images
cv2.imshow("BITWISE_AND", dest_and)
cv2.waitKey(0)

# cv2.bitwise_or is applied over the
# image inputs with applied parameters
dest_or = cv2.bitwise_or(HalfAndHalfImage, WhiteOvalImage, mask = None)

# the window showing output image
# with the Bitwise OR operation
# on the input images
cv2.imshow("BITWISE_OR", dest_or)
cv2.waitKey(0)

# cv2.bitwise_xor is applied over the
# image inputs with applied parameters
dest_xor = cv2.bitwise_xor(HalfAndHalfImage, WhiteOvalImage, mask = None)

# the window showing output image
# with the Bitwise XOR operation
# on the input images
cv2.imshow("BITWISE_XOR", dest_xor)
cv2.waitKey(0)

# cv2.bitwise_not is applied over the
# image input with applied parameters
dest_not1 = cv2.bitwise_not(HalfAndHalfImage, mask = None)
dest_not2 = cv2.bitwise_not(WhiteOvalImage, mask = None)

# the windows showing output image
# with the Bitwise NOT operation
# on the 1st and 2nd input image
cv2.imshow('Bitwise NOT on image 1', dest_not1)
cv2.waitKey(0)
cv2.imshow('Bitwise NOT on image 2', dest_not2)
cv2.waitKey(0)

# resizing an image using cv2
# and plotting out the resized images
CherryTomatoesImage = cv2.imread("Images/CherryTomatoes.jpg", 1)

# Perform various resizing methods
TomatoHalf = cv2.resize(CherryTomatoesImage, (0, 0), fx = 0.1, fy = 0.1)
TomatoBigger = cv2.resize(CherryTomatoesImage, (1050, 1610))
TomatoStretchNear = cv2.resize(CherryTomatoesImage, (780, 540),
               interpolation = cv2.INTER_NEAREST)

# Display plotted images together in one image
Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
images =[CherryTomatoesImage, TomatoHalf, TomatoBigger, TomatoStretchNear]
for i in range(len(Titles)):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])
plt.show()

"""
STOP! You MUST continue from this exact point:
https://www.geeksforgeeks.org/image-processing-in-python-scaling-rotating-shifting-and-edge-detection/
"""

# De-allocate any associated memory usage
cv2.destroyAllWindows()
