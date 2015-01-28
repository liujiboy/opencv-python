# -*- coding: utf-8 -*-
'''
将图像分割为r、g、b通道
'''
import cv2
bgr=cv2.imread("images/robben.jpg")
#分割图像为多个通道
b,g,r=cv2.split(bgr) 
#将通道重新合并
rgb=cv2.merge([r,g,b])
#imshow不能正确显示RGB图像
cv2.imshow("rbg image",rgb) 
#imshow可以正确显示BGR图像
cv2.imshow("bgr image",bgr) 
cv2.waitKey(0)
cv2.destroyAllWindows()
