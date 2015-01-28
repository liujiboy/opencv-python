# -*- coding: utf-8 -*-
'''
This time we create a VideoWriter object. 
We should specify the output file name (eg: output.avi). 
Then we should specify the FourCC code (details in next paragraph). 
Then number of frames per second (fps) and frame size should be passed. 
And last one is isColor flag. If it is True, encoder expect color frame, otherwise it works with grayscale frame.
FourCC is a 4-byte code used to specify the video codec. 
The list of available codes can be found in fourcc.org. 
It is platform dependent. Following codecs works fine for me.
In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable. MJPG results in high size video. X264 gives very small size video)
In Windows: DIVX (More to be tested and added)
In OSX : (I don’t have access to OSX. Can some one fill this?)
FourCC code is passed as cv2.VideoWriter_fourcc('M','J','P','G') or cv2.VideoWriter_fourcc(*'MJPG) for MJPG.

'''
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', cv2.cv.CV_FOURCC('X', 'V', 'I', 'D'), 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()