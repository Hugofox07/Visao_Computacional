import cv2 as cv
import numpy as np

img = cv.imread('imagens/cafe.jpg') 
print(img.shape)

# redefinindo o tamanho da imagem
imgResize = cv.resize(img,(1000,500))
print(imgResize.shape)

       #imgCroppeing
imgCropeed = img [0:200,200:500]
print(imgCropeed.shape)
   # mostrando a imagem 
cv.imshow('Image', img)
cv.imshow('Image Resize', imgResize)
cv.imshow('Image Croppeing', imgCropeed)
cv.waitKey(0)
cv.destroyAllWindows()
