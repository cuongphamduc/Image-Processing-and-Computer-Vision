"""
5. Warping and Estimation

Exercise 4

Write a function affineTransform(f, x1, y1, x2, y2, x3, y3, width, height) that warps the parallelogram defined by the
three points (x1,y1), (x2,y2) and (x3,y3) onto a new image of given width and height. Here we assume that the
coordinates are given with respect to the graphical axis (x from left to right, y from top to bottom).

"""

import cv2
import numpy as np


def affineTransform(f, x1, y1, x2, y2, x3, y3, width, height):
    srcTri = np.array([[x1, y1], [x2, y2], [x3, y3]]).astype(np.float32)
    dstTri = np.array([[0, 0], [width - 1, 0], [0, height - 1]]).astype(np.float32)

    warp_mat = cv2.getAffineTransform(srcTri, dstTri)
    warp_dst = cv2.warpAffine(f, warp_mat, (width, height))

    return warp_dst


src = cv2.imread('images/cameraman.png')

x1, y1, x2, y2, x3, y3 = 0, 0, 200, 50, 50, 100
x4, y4 = x1 + (x3 - x2), y1 + (y3 - y2)
(tl, tr, br, bl) = ((x1, y1), (x2, y2), (x3, y3), (x4, y4))

widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
maxWidth = max(int(widthA), int(widthB))

heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
maxHeight = max(int(heightA), int(heightB))

dst = affineTransform(src, x1, y1, x2, y2, x3, y3, maxWidth, maxHeight)

cv2.imshow('Source image', src)
cv2.imshow('Warp', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
