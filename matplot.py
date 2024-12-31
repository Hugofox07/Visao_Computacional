#importando as bibliotecas do opencv
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#lendo a imagem na cor cinza
img = cv.imread("imagens/cafe.jpg",0)

#Usando a bibliote do matlib
plt.imshow(img, cmap = "gray", interpolation = "bicubic")
# to hide tick values on X and Y axis
plt.xticks([]), plt.yticks([])
# cria uma linha na imagem
#plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()