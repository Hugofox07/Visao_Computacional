import cv2 as cv 
import numpy as np
img = cv.imread("imagens/cafe.jpg") # abre a imagem no original

cv.imshow("Image", img)
cv.waitKey()
cv.destroyAllWindows()