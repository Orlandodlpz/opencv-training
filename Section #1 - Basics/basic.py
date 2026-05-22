import cv2 as cv

img = cv.imread('Photos/boston.jpg')
cv.imshow('Boston', img)

# Converting an image to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# Edge Cascade
# canny = cv.Canny(img, 200, 275)
# cv.imshow('Canny Edges', canny)

# Dilating the image
# dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# Eroding
# eroded = cv.erode(canny, (3,3), iterations=3)
# cv.imshow('Eroded', eroded)

# Resize
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

# Cropping
cropped = img[50:300, 200:500]
cv.imshow('Cropped', cropped)

cv.waitKey(0)