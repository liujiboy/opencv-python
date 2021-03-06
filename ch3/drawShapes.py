# -*- coding: utf-8 -*-
'''
绘制图形
cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]]) → None
cv2.line(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) → None
cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]]) → None
cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) → None
cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]) → None
具体函数参考http://docs.opencv.org/modules/core/doc/drawing_functions.html
'''
import numpy as np
import cv2
#创建512x512的黑白图像
img = np.zeros((512,512,3), np.uint8)
#画图形
cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.circle(img,(447,63), 63, (0,0,255), -1)
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.cv.CV_AA)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()