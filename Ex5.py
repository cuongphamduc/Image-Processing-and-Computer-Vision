"""
5. Warping and Estimation

Exercise 5

Write a function perspectiveTransform(f, x1, y1, x2, y2, x3, y3, x4, y4, width, height) that warps a quadrilateral with
vertices at (x1,y1), (x2,y2), (x3,y3) and (x4,y4) to a new image of given width and height.

"""

import cv2
import numpy as np


def perspectiveTransform(f, x1, y1, x2, y2, x3, y3, x4, y4, width, height):
    src_rect = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]]).astype(np.float32)
    dst_rect = np.array([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]]).astype(np.float32)

    warp_mat = cv2.getPerspectiveTransform(src_rect, dst_rect)
    warp_dst = cv2.warpPerspective(f, warp_mat, (width, height))

    return warp_dst


src = cv2.imread('images/flyeronground.png')

x1, y1, x2, y2, x3, y3, x4, y4 = 571, 185, 820, 170, 594, 588, 348, 556
(tl, tr, br, bl) = ((x1, y1), (x2, y2), (x3, y3), (x4, y4))

widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
maxWidth = max(int(widthA), int(widthB))

heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
maxHeight = max(int(heightA), int(heightB))

dst = perspectiveTransform(src, x1, y1, x2, y2, x3, y3, x4, y4, maxWidth, maxHeight)

cv2.imshow('Source image', src)
cv2.imshow('Warp', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
