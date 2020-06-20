'''
For image processing only OpenCV is allowed!
PART A- To find the RGB value of the center pixel of the given images
PART B- Setting Blue and Green Channels to zero in the given image
PART C- Add Alpha Channel in the given image
PART D- Convert to Grayscale without using inbuilt BGR2GRAY command

'''
import cv2
import numpy as np
import os
import pandas as pd

def partA():

    df=pd.DataFrame()

    def imgval(filename):
        add=os.path.abspath('').split('\\')[:-1]
        add.append('Images\\'+filename)
        add='\\'.join(add)
        img=cv2.imread(add)
        lst1=list(img.shape)
        shape=img.shape
        midx=round(shape[0]/2)
        midy=round(shape[1]/2)
        lst2=list(img[midx,midy])
        lst1.extend(lst2)
        lst1.insert(0,filename)
        return pd.DataFrame(lst1).T


    df=df.append(imgval('bird.jpg'),ignore_index=True)
    df=df.append(imgval('cat.jpg'),ignore_index=True)
    df=df.append(imgval('flowers.jpg'),ignore_index=True)
    df=df.append(imgval('horse.jpg'),ignore_index=True)

    # Relative Pathing
    
    add=os.path.abspath('').split('\\')[:-1]
    add.append('Generated')
    add='\\'.join(add)

    df.to_csv(os.path.join(add,'stats.csv'),header=False,index=False)

def partB():
    
    add=os.path.abspath('').split('\\')[:-1]
    add.append('Images\\'+'cat.jpg')
    filename='\\'.join(add)
    
    img=cv2.imread(filename)
	for x in range(0,img.shape[0]):
    	for y in range(0,img.shape[1]):
        	img[x][y][0]=img[x][y][1]=0
	
     # Relative Pathing
    
    add=os.path.abspath('').split('\\')[:-1]
    add.append('Generated')
    add='\\'.join(add)

    cv2.imwrite(os.path.join(add,'cat_red.jpg'),img)

def partC():
    
    add=os.path.abspath('').split('\\')[:-1]
    add.append('Images\\'+'flowers.jpg')
    filename='\\'.join(add)
    
    img=cv2.imread(filename)
	img2=np.ones((img.shape[0],img.shape[1],4))*0.5
	for x in range(0,img.shape[0]):
    	for y in range(0,img.shape[1]):
       		for z in range(0,img.shape[2]):
            	img2[x][y][z]=img[x][y][z]
                
    add=os.path.abspath('').split('\\')[:-1]
    add.append('Generated')
    add='\\'.join(add)
	cv2.imwrite(os.path.join(add,'flowers_alpha.png'),img)

def partD():
    add=os.path.abspath('').split('\\')[:-1]
    add.append('Images\\'+'horse.jpg')
    filename='\\'.join(add)
    
    img=cv2.imread(add)
    
	for x in range(0,img.shape[0]):
    	for y in range(0,img.shape[1]):
        	img[x][y]= (0.11*img[x][y][0])+(0.59*img[x][y][1])+(0.3*img[x][y][2])
    
    add=os.path.abspath('').split('\\')[:-1]
    add.append('Generated')
    add='\\'.join(add)
    
	cv2.imwrite(os.path.join(add,'horse_gray.jpg'),img)

partA()
partB()
partC()
partD()