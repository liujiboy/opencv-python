# -*- coding: utf-8 -*-
'''
播放视频，需要安装合适的解码器，例如ffmpeg和gstreamer
'''
import cv2
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
cap = cv2.VideoCapture('videos/test.avi')
while(True):
    #ret是布尔值表示是否读取成功
    #frame是读取到的图像
    ret, frame = cap.read()
    if ret==True:
        #可以对frame进行处理后再显示，例如
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
