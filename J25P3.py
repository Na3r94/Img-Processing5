import cv2
import numpy as np


image = cv2.imread('building.tif', cv2.IMREAD_GRAYSCALE)

mask1 = ([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
mask2 = ([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
result = np.zeros((600, 600), dtype='uint8')

# print(mask)
print(image.shape)

rows, cols = image.shape
def con(mask):
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            small_image = image[i-1:i+2, j-1:j+2]
            besco = np.multiply(small_image, mask)
            out = np.sum(besco)
            if out <= 0:
                out = 0
            if out >= 255:
                out = 255
            result[i, j] = out

    cv2.imshow('output', result)
    cv2.waitKey()

con(mask1)
con(mask2)