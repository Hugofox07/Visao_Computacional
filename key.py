#Importando as bibliotecas
import cv2 as cv
import numpy as np

#criando a variavel img e mostrando a imagem na cor gray
img = cv.imread("imagens/cafe.jpg", 0)
cv.imshow("imagem", img)

#Esperando a tecla k ser apertada ou a tecla s para salvar a imagem
k = cv.waitKey()
if k ==27:
  cv.destroyAllWindows()
elif k == ord("s"):
  # salvando a imagem na cor cinza
  cv.imwrite("cafegray.jpg", img)
  cv.destroyAllWindows()