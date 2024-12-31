import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
#capture frame-by-frame
    ret, frame = cap.read()
#our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
 
# display the resulting frame
    cv.imshow('frame',gray)
    if cv.waitKey(1)  & 0xFF == ord('q'):
       break

#when everything done, release the capture
cap.release()
cv.destroyAllWindows()



