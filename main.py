import cv2
import numpy as np
from matplotlib import pyplot as plt

foto1 = cv2.imread("Dizi.jpg", 0)
[x, y] = foto1.shape

hist = [0] * 256

for i in range(x):
    for j in range(y):
        deger = foto1[i, j]
        hist[deger] = hist[deger] + 1
plt.figure(2)
plt.plot(hist)
plt.show()
