import cv2 as cv

img1 = cv.imread('vessel1.png')
img2 = cv.imread('vessel2.png')


img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 40, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

img1_bg = cv.bitwise_and(img1, img1, mask=mask_inv)

img2_fg = cv.bitwise_and(img2, img2, mask=mask)

final = cv.add(img1_bg, img2_fg)

cv.imshow('Retina', img1)
cv.imshow('Vessels', img2)
cv.imshow('Mask', mask)
cv.imshow('Final Overlay', final)

cv.waitKey(0)
cv.destroyAllWindows()
