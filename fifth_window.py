import tkinter as tk
from PIL import ImageTk, Image
import tkinter.filedialog
import cv2
import numpy as np
from array import *
import math

image = cv2.imread("IMG_8907.jpg")
#image=~image

#image = cv2.resize(image,(1024,1024))
#converting to gray scale
directory= r'C_Ubuntu'
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#applying canny edge detection
#edged = cv2.Canny(image,220, 250)
#script_dir=os.path.dirname('/mnt/c/Ubuntu')
#os.chdir(script_dir)
height=gray.shape[0]
width= gray.shape[1]
width_cutoff=height//2

s1=image[width_cutoff:,:]
s2=image[:width_cutoff:,:]
new_img=cv2.resize(s1,(640,640))


cv2.imshow("s1",new_img)


new_img=cv2.resize(s2,(640,640))


cv2.imshow("s2",new_img)
cv2.waitKey(0)


gray=cv2.cvtColor(s2,cv2.COLOR_BGR2GRAY)
thresh=180
ret,thresh_img=cv2.threshold(gray,thresh,255,cv2.THRESH_BINARY)
new_img=cv2.resize(thresh_img,(640,640))


cv2.imshow("thresh",new_img)
cv2.waitKey(0)
ole,contours,hierarchy=cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

img_contours=np.zeros(image.shape)
cv2.drawContours(img_contours,contours,-1,(0,255,0),3)


#print(script_dir)
#finding contours

sorted_contours= sorted(contours,key=lambda ctr:cv2.boundingRect(ctr)[1])

idx = 0
image_array =[]
for c in sorted_contours:

	x,y,w,h = cv2.boundingRect(c)
	#w>19 and h>37 and w<80 and h<80
	if h>300 and w>300 :
		idx+=1
		new_img=image[y:y+h,x:x+w]
		
		#cropping images
		#cv2.imshow("Canny Edge",new_img)
		
		cv2.imshow("palia",new_img)
		image_array.append(new_img)
		cv2.waitKey(0)

		
		#cv2.waitKey(0)
		print(idx)
		#cv2.imwrite("cropped/"+str(idx) + '.png', new_img)
#cv2.imshow("Original Image",image)
#edged=cv2.resize(edged,(1980,1024))
#cv2.imshow("Canny Edge",image_array[0])
#cv2.waitKey(0)
#print('>> Objects Cropped Successfully!')
#print(">> Check out 'cropped' Directory")

#for i in range(len(image_array)):
	#cv2.imshow("nea",image_array[i])
	
	#cv2.waitKey(0)

image = cv2.imread("IMG_8910.jpg")
#image=~image

#image = cv2.resize(image,(1024,1024))
#converting to gray scale
directory= r'C_Ubuntu'
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#applying canny edge detection
#edged = cv2.Canny(image,220, 250)
#script_dir=os.path.dirname('/mnt/c/Ubuntu')
#os.chdir(script_dir)
thresh=180
ret,thresh_img=cv2.threshold(gray,thresh,255,cv2.THRESH_BINARY)
new_img=cv2.resize(thresh_img,(640,640))


cv2.imshow("thresh",new_img)
cv2.waitKey(0)
ole,contours,hierarchy=cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

img_contours=np.zeros(image.shape)
cv2.drawContours(img_contours,contours,-1,(0,255,0),3)

cv2.imshow("palia",img_contours)
cv2.waitKey(0)
#print(script_dir)
#finding contours

sorted_contours= sorted(contours,key=lambda ctr:cv2.boundingRect(ctr)[1])

idx = 0
image_array =[]
for c in sorted_contours:

	x,y,w,h = cv2.boundingRect(c)
	#w>19 and h>37 and w<80 and h<80
	if w>400 and h>500 :
		idx+=1
		new_img=image[y:y+h,x:x+w]
		
		#cropping images
		#cv2.imshow("Canny Edge",new_img)
		
		cv2.imshow("palia",new_img)
		image_array.append(new_img)
		cv2.waitKey(0)

		
		#cv2.waitKey(0)
		print(idx)
		#cv2.imwrite("cropped/"+str(idx) + '.png', new_img)
#cv2.imshow("Original Image",image)
#edged=cv2.resize(edged,(1980,1024))
#cv2.imshow("Canny Edge",image_array[0])
#cv2.waitKey(0)
#print('>> Objects Cropped Successfully!')
#print(">> Check out 'cropped' Directory")

#for i in range(len(image_array)):
	#cv2.imshow("nea",image_array[i])
	
	#cv2.waitKey(0)
