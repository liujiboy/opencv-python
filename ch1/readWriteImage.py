# -*- coding: utf-8 -*-
'''
read and write image
'''
import cv2

#cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
#cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
#cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
img = cv2.imread('images/robben.jpg',cv2.IMREAD_COLOR)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('saved/robben.png',img)
    cv2.destroyAllWindows()