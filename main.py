#import move
import cv2
from lane import getLaneCurve
import webcam
 

def main():
 
    img = webcam.getImg()
    curveVal= getLaneCurve(img,2)
    turn = ''
    sen = 1.3  # SENSITIVITY
    maxVAl= 80 # MAX SPEED
    if curveVal>maxVAl:curveVal = maxVAl
    if curveVal<-maxVAl: curveVal =-maxVAl
    #print(curveVal)
    if curveVal>0:
        sen =1.7
        turn = 'right'
        if curveVal<0.05: 
            curveVal=0
            turn = ''
            
    else:
        turn = 'left'
        if curveVal>-0.08: 
            curveVal=0
            turn = ''
    #move.move(50,'forward',turn,abs(curveVal*sen))
    print(turn, curveVal)
    cv2.waitKey(1)
     
 
if __name__ == '__main__':
    #move.setup()
    while True:
        main()