#-＊-coding: utf8 -*-
'''
用matplotlib显示图像
'''
import cv2
from matplotlib import pyplot as plt
#opencv的图像格式是BGR
bgr = cv2.imread('images/robben.jpg')
#用numpy的索引方法将BGR转为RGB，这种方法比用opencv的split再merge方便
rgb=bgr[:,:,::-1] 
'''
画两个子图分别显示BGR和RGB图像
与opencv相反matplotlib可以正确显示RGB
但不能正确显示BGR
'''
f,(ax1,ax2)=plt.subplots(1, 2)
ax1.set_title("BGR")
ax1.imshow(bgr)
ax2.set_title("RGB")
ax2.imshow(rgb)
#取消坐标
plt.setp([a.get_xticklabels() for a in (ax1,ax2)], visible=False)
plt.setp([a.get_yticklabels() for a in (ax1,ax2)], visible=False)
plt.show()
