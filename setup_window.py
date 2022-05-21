import PIL
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.filedialog
import cv2
import numpy as np
from array import *
import math
import random

mywidth =800

lines = []
with open('test_image.txt') as f:
	lines = f.readlines()
f.close()
img = Image.open(lines[0])
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('resized.jpg')

WIDTH, HEIGHT = 900,700
topx, topy, botx, boty = 0, 0, 0, 0
rect_id = None
path = "resized.jpg"


def get_mouse_posn(event):
	global topy, topx

	topx, topy = event.x, event.y

def update_sel_rect(event):
	global rect_id
	global topy, topx, botx, boty

	botx, boty = event.x, event.y
	canvas.coords(rect_id, topx, topy, botx, boty)	# Update selection rect.
	#print("height",abs(topy-boty))
	#print("width",abs(topx-botx))


def check_result():
	image_u = []
	with open('test_image.txt') as f:
		image_u = f.readlines()
	f.close()
	image = cv2.imread(str(image_u[0]))

	gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	
	with open('threshold.txt') as f:
		data = f.readline()
		threshold = int(data.strip())
	f.close()	
	
	thresh=threshold
	ret,thresh_img=cv2.threshold(gray,thresh,255,cv2.THRESH_BINARY)
	
	contours,hierarchy=cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	img_contours=np.zeros(image.shape)
	cv2.drawContours(img_contours,contours,-1,(0,255,0),3)
	
	#sorted_contours= sorted(contours,key=lambda ctr:cv2.boundingRect(ctr))
	sorted_contours= sorted(contours,key=lambda ctr:cv2.contourArea(ctr), reverse = True)
	
	with open("apotelesmata_xw.txt") as file_in:
		lines = []
		for line in file_in:
			lines.append(line)
	file_in.close()
	given_h=0
	given_w = 0
	given_h = int(lines[0])
	given_w = int(lines [1])
		
	print("********",given_h,given_w)	
	
	idx = 0
	image_array =[]
	overlap_x =[]
	overlap_w =[]
	overlap_idx = 0
	see_f=0
	for c in sorted_contours:
	    #koftis gia > apo stoxous user
		
		x,y,w,h = cv2.boundingRect(c)	

		width_pc= given_w * 0.4
		height_pc = given_h * 0.4
		
		overlap = True 
		if w>given_w-width_pc and h>given_h-height_pc and w<given_w+width_pc and h<given_h+height_pc :	 #(prev_x >=x or x>= prev_xw or prev_x >= xw or xw>= prev_xw):
			if(overlap_idx == 0):
				
				overlap_idx = 0  #dummy command
			else:
				
				for k in range(len(overlap_x)):
					#if not(overlap_x[k]<x and x<overlap_x[k]+overlap_w[k] and overlap_x[k]<x+w and x+w<overlap_x[k]+overlap_w[k]) and x!=overlap_x[k]:
					if not((overlap_x[k]>x and x +w >overlap_x[k] + overlap_w[k]) or ( x+w >overlap_x[k] and x< overlap_x[k]+overlap_w[k]) or (overlap_x[k] == x and overlap_x[k]+overlap_w[k] == x+w)):
						print("mpika mesa ")
						overlap = False
					else:
						overlap = True
						break
				if overlap == True: continue
				
			new_img=image[y:y+h,x:x+w]
			#cv2.imshow("Canny Edge",new_img)
			sc2 =cv2.resize(new_img,(700,700))
			cv2.imshow("Targets detected",sc2)
			cv2.waitKey(0)
			overlap_x.append(x)
			overlap_w.append(w)
			overlap_idx+=1
			image_array.append(new_img)
	print(overlap_x, overlap_w)
	cv2.waitKey(0)	

		
		
#eggrafi apotelesmatwn sto txt meta apo rescale
def clicked():
	print("CLICKED")
	file= open("apotelesmata_xw.txt","w")
	img = Image.open(lines[0])
	wpercent = (float(img.size[0])/mywidth)
	hsize=int((float(img.size[1])*float(wpercent)))
	total_height = int(abs(topy-boty)*wpercent)
	total_width = int(abs(topx-botx)*wpercent)
	x = str(total_height)
	y = str(total_width)
	file.write(x)
	file.write("\n")
	file.write(y)
	file.close() #to change file access modes
	print("TELOS CLICKED")
window = tk.Tk()
window.title("Επιλογή στόχου")
window.geometry('%sx%s' % (WIDTH, HEIGHT))



def close_setup_window():
	global current_window
	b1.destroy()
	b2.destroy()
	b3.destroy()
	window.destroy()
	import second_window
	


img = ImageTk.PhotoImage(Image.open(path))
canvas = tk.Canvas(window, width=img.width(), height=img.height(),
				   borderwidth=0, highlightthickness=0)
canvas.pack(expand=True)
canvas.img = img  # Keep reference in case this code is put into a function.
canvas.create_image(0, 0, image=img, anchor=tk.NW)

# Create selection rectangle (invisible since corner points are equal).
rect_id = canvas.create_rectangle(topx, topy, topx, topy,
								  dash=(2,2), fill='', outline='red')

b2 = tk.Button(window, text = "'Ελεγχος αποτελεσμάτων",command = check_result)
b2.place(x=350, y=640,width=250)

b1 = tk.Button(window, text = "Αποθήκευση", command=clicked)
b1.place(x=20, y=640,width=250)
b1.config( height = 1, width = 2 )


b3 = tk.Button(window, text = "Συνέχεια", command=close_setup_window)
b3.place(x=650, y=640,width=250)
b3.config( height = 1, width = 2 )


canvas.bind('<Button-1>', get_mouse_posn)
canvas.bind('<B1-Motion>', update_sel_rect)


window.mainloop()