import cv2 as cv
import numpy as np

img = cv.imread('imagens/uno.png')

 #Pixels values
inputs_points = np.float32([[225,265], [507,205], [295,701], [591,639]])
print(inputs_points)

#Output image size
width = 400
height = int(width * 1.414) # for A4

#Desire points values in the output image
converted_points = np.float32([[0, 0],[width, 0],[0, height], [width, height]])

#Perspective transformation
matrix = cv.getPerspectiveTransform(inputs_points, converted_points)
img_output = cv.warpPerspective(img, matrix, (width, height))


cv.imshow('Original',img)
cv.imshow('Warp perspective', img_output)
cv.imwrite('imagens/output.jpg',img_output)

cv.waitKey(0)
cv.destroyAllWindows()