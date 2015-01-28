#-＊-coding: utf8 -*-
'''
display image using matplotlib
'''
import cv2
from matplotlib import pyplot as plt

bgr = cv2.imread('images/robben.jpg') #image format of opencv is BGR
rgb=bgr[:,:,::-1] #using numpy indexing to convert bgr to rgb
f,(ax1,ax2)=plt.subplots(1, 2)
ax1.set_title("BGR")
ax1.imshow(bgr)
ax2.set_title("RGB")
ax2.imshow(rgb)
# axis off
plt.setp([a.get_xticklabels() for a in (ax1,ax2)], visible=False)
plt.setp([a.get_yticklabels() for a in (ax1,ax2)], visible=False)
plt.show()
