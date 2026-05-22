import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/boston.jpg')
# cv.imshow('Boston', img)

# plt.imshow(img)
# plt.show()

# # BGR ---> Grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# # BGR ---> HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# # BGR ---> LAB
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

# BGR ---> RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)