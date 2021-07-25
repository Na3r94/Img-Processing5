# import cv2
# import numpy as np
#
# image = cv2.imread('Joker.jpeg', cv2.IMREAD_GRAYSCALE)
#
# matris_level = int(input('Enter level of filter: '))
# n = matris_level
# matris = np.zeros((n,n))
#
# for i in range(n):
#     for j in range(n):
#         matris[i, j] = 1 / n ** 2
#
# result = np.zeros((1224, 2040), dtype='uint8')
#
# rows, cols = image.shape
# border = (n-1) / 2
# b = int(border)
# for i in range(b, rows-b):
#     for j in range(b, cols-b):
#         small_image = image[i-b:i+n-b, j-b:j+n-b]
#         besco = np.multiply(small_image, matris)
#         out = np.sum(besco)
#         result[i, j] = out
#
# cv2.imshow('output', result)
# cv2.imwrite('temp.jpg', result)
# cv2.waitKey()

a = 25//4
print(a)