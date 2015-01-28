# -*- coding: utf-8 -*-
'''
从默认（第一个）摄像设备获取图像并显示
'''
import cv2
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
#打开图像设备
cap = cv2.VideoCapture(0)
while(True):
    #获取图像
    ret, frame = cap.read()
    #0表示将图像绕x轴翻转，1将图像绕y轴翻转，-1表示同时绕x和y轴翻转
    #想想为什么要翻转
    frame = cv2.flip(frame,1)
    #显示图像
    cv2.imshow('frame',frame)
    #图像只显示一秒，如果同时按下q键则程序退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#释放摄像设备
cap.release()
cv2.destroyAllWindows()