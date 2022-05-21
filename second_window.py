import tkinter as tk
from PIL import ImageTk, Image
import os

window = tk.Tk() 
window.title(u"523 Recognition Of Successful Shots On Targets (ROSOT)")
#window.resizable(800,600)
window.geometry("680x360")


#tk.Label(window, text="Πεδίο Βολής").grid(row=0)
#tk.Label(window, text="Ημερομηνία Βολής").grid(row=1)
#tk.Label(window, text="Μονάδα Βολής").grid(row=2)
tk.Label(window, text="Αριθμός Στόχων").grid(row=3)
#tk.Label(window, text="Απόσταση Βολής").grid(row=4)
#tk.Label(window, text="Είδος Όπλου").grid(row=5)
#tk.Label(window, text="Είδος Πυρομαχικών").grid(row=6)
#tk.Label(window, text="Είδος Βολής (ΒΚΒ ή ΚΡ)").grid(row=7)
#tk.Label(window, text="Θέση Βολής").grid(row=6)
#tk.Label(window, text="Ποσότητα Πυρομαχικών ανα Σκοπευτή").grid(row=7)
#tk.Label(window, text="Κατώτατο Όριο Επίδοσης Σκοπευτή").grid(row=8)
#tk.Label(window, text="Αξιωματικός Βολης").grid(row=8)
#tk.Label(window, text="Οπλουργός").grid(row=9)

#e1 = tk.Entry(window,width=50)
#e2 = tk.Entry(window,width=50)
#e3 = tk.Entry(window,width=50)
e4 = tk.Entry(window,width=50)
#e5 = tk.Entry(window,width=50)
#e6 = tk.Entry(window,width=50)
#e7 = tk.Entry(window,width=50)
#e8 = tk.Entry(window,width=50)
#e9 = tk.Entry(window,width=50)
#e10 = tk.Entry(window,width=50)
#e11 = tk.Entry(window,width=50)
#e12 = tk.Entry(window,width=50)
#e13 = tk.Entry(window,width=50)
#e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)
#e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
#e5.grid(row=4, column=1)
#e6.grid(row=5, column=1)
#e7.grid(row=6, column=1)
#e8.grid(row=5, column=1)
#e9.grid(row=6, column=1)
#e10.grid(row=7, column=1)
#e11.grid(row=8, column=1)
#e12.grid(row=8, column=1)
#e13.grid(row=9,column=1)


button1=tk.Button(window, text="Eπόμενο")
button1.place(x=580, y=300)

information_array=[]

def close_second_window(event):
	#file = open("informations.txt", "w", encoding='utf-8')
	#with open("informations.txt", "w", encoding='utf-8') as file:

	
		#file.write("Πεδίο Βολής: "+str((e1.get()))+"\n")
		#file.write("Ημερομηνία Βολής: "+str((e2.get()))+"\n")
		#file.write("Μονάδα Βολής: "+str((e3.get()))+"\n")
		#file.write("Αριθμός Στόχων: "+str((e4.get()))+"\n")
		#file.write("Απόσταση Βολής: "+str((e5.get()))+"\n")
		#file.write("Είδος Όπλου: "+str((e6.get()))+"\n")
		#file.write("Είδος Πυρομαχικών: "+str((e7.get()))+"\n")
		#file.write("Είδος Βολής (ΒΚΒ ή ΚΡ): "+str((e8.get()))+"\n")
		#file.write("Θέση Βολής: "+str((e9.get()))+"\n")
		#file.write("Ποσότητα Πυρομαχικών ανα Σκοπευτή: "+str((e10.get()))+"\n")
		#file.write("Κατώτατο Όριο Επίδοσης Σκοπευτή: "+str((e11.get()))+"\n")
		#file.write("Αξιωματικός Βολης: "+str((e12.get()))+"\n")
		#file.write("Οπλουργός: "+str((e13.get()))+"\n")
	
	
		#file.close()
	window.destroy()
	
	
	import third_window
	#window.destroy()
	#create_new_window('<Button-1>')

button1.bind('<Button-1>',close_second_window)


window.mainloop()