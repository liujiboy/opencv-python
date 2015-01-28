# -*- coding: utf-8 -*-
'''
从摄像头读数据转存到视频
'''
import cv2
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
cap = cv2.VideoCapture(0)
#读一帧确定帧率（fps），帧宽度和高度
#cap.get()可以获得视频的属性
#例如某些摄像头可以用cap.get(cv2.cv.CV_CAP_PROP_FPS)来确定帧率
#cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)获取帧的宽度
#cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)获取帧的宽度
start=cv2.getTickCount()
ret,frame=cap.read()
end=cv2.getTickCount()
fps=cv2.getTickFrequency()/(end-start)
height=frame.shape[0]
width=frame.shape[1]
#cv2.cv.CV_FOURCC指定输出视频的编码方式，从fourcc.org可以查询目前已有的编码方式
#编码方式的选择取决于是否安装了对应的视频编码程序
#常用的编码包括DIVX, XVID, MJPG, X264, WMV1, WMV2
#Windows推荐选择DIVX
#linux和mac推荐选择XVID
out = cv2.VideoWriter('output/capture.avi', cv2.cv.CV_FOURCC('X', 'V', 'I', 'D'), fps, (width,height))
while(True):
    ret, frame = cap.read()
    print 
    if ret==True:
        frame = cv2.flip(frame,1)
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
