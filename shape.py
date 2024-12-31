import cv2 as cv 
import numpy as np

foto = cv.imread('imagens/cafe.jpg')
print(foto)

#Drawing shapes, line, rectangulo, circulo
cv.line(foto, (0,0),(300,300),(0,255,0),3)
cv.rectangle(foto,(200,200),(300,300),(255,0,0),3)
cv.circle(foto,(400,50),40,(255,255,0),5)
#write text in image
cv.putText(foto,'Deus e bom',(500,300),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)
#Mostrando a foto
cv.imshow('Line Img', foto)
cv.waitKey()
cv.destroyAllWindows()