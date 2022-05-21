import tkinter as tk
from PIL import ImageTk, Image
import tkinter.filedialog
import cv2
import numpy as np
from array import *
from tkinter import *
import math
import random
import os

window = tk.Tk() 
window.title(u"523 Recognition Of Successful Shots On Targets (ROSOT) - Ρυθμίσεις")
window.geometry("680x200")


text_widget = tk.Text(window)
text_widget.insert('insert',"200")
text_widget.pack(anchor = "w", padx = 10, pady = 10)
input = text_widget.get("1.0",'end-1c')




labelText = tk.StringVar()
labelText.set("Δεν επιλέχθηκε φωτογραφία")
case_name_entry = tk.Entry(window, textvariable=labelText)




def select_image():
	#label1.configure(text="msg will change every sec")
	# lab1_datum_in = tkinter.Label(window, textvariable=datum_in_text)
	# labelText.delete(0, END)
	# labelText.set("Επιτυχής επιλογή φωτογραφίας")
	# labelText.set("Επιτυχής επιλογή φωτογραφίας")
	global current_window
	file= open("threshold.txt","w")
	file.write(input)
	file.close()

	file1=tkinter.filedialog.askopenfilename()
	file= open("test_image.txt","w")
	file.write(str(file1))
	file.close() #to change file access modes
	
def setup_continue():
	global current_window
	file= open("threshold.txt","w")
	file.write(input)
	file.close()
	button1.destroy()
	button2.destroy()
	button3.destroy()
	window.destroy()
	import setup_window
	
def setup_cancel():
	global current_window
	print("alright")
	button1.destroy()
	button2.destroy()
	button3.destroy()
	window.destroy()
	import first_window
	
button1=tk.Button(window, text="Επιλογή Φωτογραφίας",command= select_image)
button1.place(x=20, y=30,width=250)

text_widget.place(x = 400,y = 60,height=25,width=250)

button2=tk.Button(window, text="Συνέχεια", command= setup_continue)
button2.place(x=400, y=150,width=250)

button3=tk.Button(window, text="Πίσω", command = setup_cancel)
button3.place(x=20, y=150,width=250)

#button3.bind('<Button-1>',setup_cancel)

#button2.bind('<Button-1>',setup_continue)

window.mainloop()
