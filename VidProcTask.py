import cv2
import numpy as np
import os

def partA():
    add=os.path.abspath('').split('\\')[:-1]
    add.append('Videos\\RoseBloom.mp4')
    filename='\\'.join(add)
    cap=cv2.VideoCapture(filename)
    n=1
    while(True):
        ret, frame = cap.read()
        
        if ret == True:
            if n == 126:
                    add=os.path.abspath('').split('\\')[:-1]
                    add.append('Generated')
                    add='\\'.join(add)

                    cv2.imwrite(os.path.join(add,'frame_as_6.jpg'),frame)
                break
            n=n+1
    
        else: 
            break
     
    cap.release()

def partB():
    add=os.path.abspath('').split('\\')[:-1]
    add.append('Generated\\frame_as_6.jpg')
    add='\\'.join(add)
    img=cv2.imread(add)
    
	for x in range(0,img.shape[0]):
    	for y in range(0,img.shape[1]):
        	img[x][y][0]=img[x][y][1]=0
    
    add=os.path.abspath('').split('\\')[:-1]
    add.append('Generated')
    add='\\'.join(add)

    cv2.imwrite(os.path.join(add,'frame_as_6_red.jpg'),img)

    
partA()
partB()