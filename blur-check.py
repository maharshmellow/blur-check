import cv2

imageName = "blurry.jpg"
# read the image using opencv
image = cv2.imread(imageName)
# convert the image to grayscale
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# laplacian = second order derivative operator used to find edges
# deemphasize regions with slowly varying gray levels -> produces edges in image
# more blurry = less defined edges = lower variance
variance = cv2.Laplacian(grayImage, cv2.CV_64F).var()
print(variance)
