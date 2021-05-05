import cv2
import utlis
 
cap = cv2.VideoCapture('vid1.mp4')
 
def getImg(display= False,size=[480,240]):
    intialTrackBarVals = [102, 80, 20, 214 ]
    utlis.initializeTrackbars(intialTrackBarVals)
    _, img = cap.read()
    img = cv2.resize(img,(480,240))
    if display:
        cv2.imshow('IMG',img)
    return img
 
if __name__ == '__main__':
    while True:
        img = getImg(True)
