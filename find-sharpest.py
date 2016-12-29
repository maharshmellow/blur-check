import cv2

images = ["blurry.jpg", "sharp.jpg"]
maxVariance = 0
sharpestImage = ""
for imageName in images:
    image = cv2.imread(imageName)
    # convert the image to grayscale
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # laplacian = second order derivative operator used to find edges
    # deemphasize regions with slowly varying gray levels -> produces edges in image
    # more blurry = less defined edges = lower variance
    variance = cv2.Laplacian(grayImage, cv2.CV_64F).var()
    if variance > maxVariance:
        maxVariance = variance
        sharpestImage = imageName

print(sharpestImage)
