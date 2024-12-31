import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('imagens/cafe.jpg',cv.IMREAD_GRAYSCALE)

plt.imshow(img, cmap='gray', interpolation='bicubic')
# to hide tick values on X and Y axis
plt.xticks([]), plt.yticks([])
# criação de linha na imagem
plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()
# Salvando a imagem
plt.imsave('imagens/cafe.png',img)
