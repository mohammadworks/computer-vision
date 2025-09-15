import cv2 as cv


image = cv.imread('bookpage.jpg')
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
threshold3 = cv.adaptiveThreshold(image_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 215, 1.5 )

cv.imshow('original', image)
cv.imshow('threshold adaptive', threshold3)

cv.waitKey(0)
cv.destroyAllWindows()