import cv2
import numpy as np
from matplotlib import pyplot as plt
foto1 = cv2.imread("Dizi.jpg",0)
CM = (np.max(foto1) - np.min(foto1))/(np.max(foto1) + np.min(foto1))
yeni = CM*foto1
plt.show()
hist_gray = cv2.calcHist([foto1], [0],None,[256],[0,256])
plt.figure(2)
plt.plot(hist_gray)
plt.show()

