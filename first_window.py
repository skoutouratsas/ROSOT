import tkinter as tk
from PIL import ImageTk, Image
import os

window = tk.Tk() 
window.title(u"523 Recognition Of Successful Shots On Targets (ROSOT)")
window.resizable(0,0)
#file = open("informations.txt", "w+")
file = open("onomata.txt", "w+")
file = open("apotelesmata.txt", "w+")
file = open("telika_apotelesmata.txt", "w+")
'''
bg = tk.PhotoImage(file = "parallagi.png")
  
# Show image using label
label1 = tk.Label( window, image = bg)
label1.place(x = 0, y = 0)

'''
img3 = ImageTk.PhotoImage(Image.open("parallagi2.png"))
panel3 = tk.Label(window, image = img3)


'''
'''

'''
def RBGAImage(path):
	return Image.open(path).convert("RGBA")

ena = RBGAImage("test.png")
duo = RBGAImage("taxiarxia.png")
tria = RBGAImage("onomata.png")
tessera = RBGAImage("peziko.png")
simaia = RBGAImage("simaia.png")

ena.paste(duo, (10, 50), duo)

#facepic = ImageTk.PhotoImage(duo)

ena.save('ena.png',"PNG")
temp=RBGAImage("ena.png")
temp.paste(tria, (245,0), tria)

temp.save('ena.png',"PNG")
temp=RBGAImage("ena.png")
temp.paste(tessera, (665,58), tessera)

temp.save('ena.png',"PNG")
temp=RBGAImage("ena.png")
temp.paste(simaia, (340 ,120), simaia)


facepic = ImageTk.PhotoImage(temp)

label1 = tk.Label(image=facepic)
label1.grid(row = 0, column = 0)

#button.place(x=430, y=100, in_=wi)

'''
'''
panel3.pack()
button.pack()
panel4.pack()
'''

panel3.pack()

def close_first_window(event):
	global current_window
	panel3.destroy()
	button1.destroy()
	button2.destroy()
	window.destroy()
	import second_window
	

	
def close_first_window2(event):
	global current_window
	panel3.destroy()
	button1.destroy()
	button2.destroy()
	window.destroy()
	import setup_window_init


button1=tk.Button(window, text="ΒΟΛΗ")
button1.place(x=500, y=270)

button2=tk.Button(window, text="ΡΥΘΜΙΣΗ ΒΟΛΗΣ")
button2.place(x=470, y=220)

button1.bind('<Button-1>',close_first_window)

button2.bind('<Button-1>',close_first_window2)





#window2.mainloop()
window.mainloop()