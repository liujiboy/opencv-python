# -*- coding: utf-8 -*-
'''
读写图像
'''
import cv2
'''
imread的第二个参数可以是如下的值
cv2.IMREAD_COLOR ：只加载RGB值，alpha值将被忽略
cv2.IMREAD_GRAYSCALE：加载灰度图
cv2.IMREAD_UNCHANGED：原样加载，包含RGB和alpha值
'''
img = cv2.imread('images/robben.jpg',cv2.IMREAD_COLOR)
#显示图像窗口，窗口名称为image
cv2.imshow('image',img)
#waitKey(n)表示n毫秒后自动关闭窗口，0表示一直等待直到按下键盘，k是按下的键盘值
k = cv2.waitKey(0) 
# ESC键的值为27，对于64位系统用k& 0xFF确保只比较后8位（mac是64位系统）
if k&0xFF == 27:         
    cv2.destroyAllWindows()
    #ord('s')返回s的键值 
elif k& 0xFF == ord('s'): 
    cv2.imwrite('saved/robben.png',img)
    cv2.destroyAllWindows()