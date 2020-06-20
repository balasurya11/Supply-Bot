###############################################################################
## Author: Team Supply Bot
## Edition: eYRC 2019-20
## Instructions: Do Not modify the basic skeletal structure of given APIs!!!
###############################################################################


######################
## Essential libraries
######################
import cv2
import numpy as np
import os
import math
import csv






############################################
## Build your algorithm in this function
## ip_image: is the array of the input image
## imshow helps you view that you have loaded
## the corresponding image
############################################
def process(ip_image):
    ###########################
    ## Your Code goes here
    
    
    blurred=cv2.medianBlur(ip_image,3)
    grey=cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
    
    # Appyling Hough Circles to the grey image
    circles=cv2.HoughCircles(grey[:430,],cv2.HOUGH_GRADIENT,1,100,param1=150,param2=10,minRadius=3,maxRadius=7)
    circles=np.int16(np.around(circles,2))
    img_hsv=cv2.cvtColor(ip_image,cv2.COLOR_BGR2HSV)

    # Three circles should be detected. Two coins and the centre white circle which should be used as reference to find the angle.The centre circle is seperated, since the centre circle is comparitively near to the centre of image.
    # The remaining two circles are classified as red or green based on their hsv values
    for item in circles[0]:
        x,y,r=item
        if item[0] in range(280,375) and item[1] in range(160,275):
            centre=[x,y,r]
        else:
            if img_hsv[y][x][0] in range(20,50):
                green=[x,y,r]
            elif img_hsv[y][x][0] in range(160,190):
                red=[x,y,r]
            
    a,b,c=red,centre,green

    # Finding the angle between the coins
    def angle3pt(a, b, c):
        ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
        if ang<0: ang=ang+360
        if ang>180: return 360-ang
        else: return ang
    angle=np.round(angle3pt(a,b,c),2)

    x,y,r=red
    ip_image=cv2.circle(ip_image,(x,y),r,(255,0,0),thickness=2)

    x,y,r=green
    ip_image=cv2.circle(ip_image,(x,y),r,(255,0,0),thickness=2)
    ip_image=cv2.putText(ip_image,f'Angle:{angle}', (20,20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
    ###########################
    op_image = ip_image
    return op_image

    
####################################################################
## The main program which provides read in input of one image at a
## time to process function in which you will code your generalized
## output computing code
## Modify the image name as per instruction
####################################################################
def main():
    ################################################################
    ## variable declarations
    ################################################################
    i = 1
    ## reading in video 
    cap = cv2.VideoCapture(0) #if you have a webcam on your system, then change 0 to 1
    ## getting the frames per second value of input video
    fps = cap.get(cv2.CAP_PROP_FPS)
    ## setting the video counter to frame sequence
    cap.set(3, 640)
    cap.set(4, 480)
    ## reading in the frame
    ret, frame = cap.read()
    ## verifying frame has content
    print(frame.shape)
    ret, frame = cap.read()
    ## display to see if the frame is correct
    cv2.imshow("window", frame)
    cv2.waitKey(int(1000/fps));

    ## calling the algorithm function
    op_image = process(frame)
    cv2.imwrite("SB#4674_task3I.jpg",op_image)


    

############################################################################################
## main function
############################################################################################
if __name__ == '__main__':
    main()
