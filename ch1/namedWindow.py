# -*- coding: utf-8 -*-
'''
创建可改变大小的图像显示窗口
'''
import cv2
img=cv2.imread("images/robben.jpg")
'''
namedWindow的第二个参数取值如下：
cv2.WINDOW_AUTOSIZE：默认值，自动缩放，窗口大小与图片大小相同
cv2.WINDOW_NORMAL：窗口可以缩放
'''
#创建名为“image”的窗口但不显示
cv2.namedWindow('image', cv2.WINDOW_NORMAL) 
#imshow显示名称为“image”的窗口
cv2.imshow('image',img) 
cv2.waitKey(0)
cv2.destroyAllWindows()