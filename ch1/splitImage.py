# -*- coding: utf-8 -*-
'''
split image into r,g,b channels
'''
import cv2
bgr=cv2.imread("images/robben.jpg")
b,g,r=cv2.split(bgr)
rgb=cv2.merge([r,g,b]) #create rgb image
#cv2.imshow能够正确显示BGR图像
cv2.imshow("rbg image",rgb)
cv2.imshow("bgr image",bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
