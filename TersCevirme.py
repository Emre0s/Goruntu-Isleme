import cv2
import numpy as np
from matplotlib import pyplot as np

foto1 = cv2.imread("resim.png", 0)
[x, y] = foto1.shape

deger = 0
for i in range(x):
    for j in range(y):
        if foto1[i, j] > deger:
            deger = foto1[i, j]

for i in range(x):
    for j in range(y):
        foto1[i, j] = deger - foto1[i, j]

cv2.imshow("tersfoto", foto1)
cv2.waitKey()
