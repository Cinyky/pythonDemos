# -*- coding:utf-8 -*-


import cv2

img = cv2.imread('shareapp.png',0)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite('ss.png',img)
cv2.destroyAllWindows()