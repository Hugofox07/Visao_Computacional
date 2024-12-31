import cv2 as cv
import numpy as np

#show the image
img = cv.imread('imagens/cafe.jpg',)
#show the image em gray 
imgGray = cv.imread('imagens/cafe.jpg',0)
kernel = np.ones((5,5),np.uint8)
#show image em blur
imgBlur =  cv.GaussianBlur(imgGray, (7,7),0)
#show image em preto e branco
imgCanny = cv.Canny(imgGray, 150,200)
#show image em dilate
imgDialation = cv.dilate(imgCanny,kernel, iterations=5)
#show image em eroded
imgErode = cv.erode(imgDialation, kernel, iterations=1)
#Show the image and name the windows
cv.imshow('Image', img)
cv.imshow('Gray Image', imgGray)
cv.imshow('Blur Image', imgBlur)
cv.imshow('Canny Image', imgCanny)
cv.imshow('Dialation Image', imgDialation)
cv.imshow('Erode Image',imgErode)
#wait time
cv.waitKey(0)
cv.destroyAllWindows()