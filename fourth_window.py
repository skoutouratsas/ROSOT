import tkinter as tk
from PIL import ImageTk, Image
import os

window = tk.Tk() 
window.title(u"523 Recognition Of Successful Shots On Targets (ROSOT)")
#window.resizable(800,600)
window.geometry("680x360")
f=open("information_array.txt","r")

seires=f.readlines()
temp3=seires[3].split(":")
print("oleee"+temp3[1])

#tk.Label(window, text="Αριθμός Γραμμής Βολής").grid(row=0)
#tk.Label(window, text="Όνομα Σκοπευτή Πρώτου Στόχου").grid(row=1)
#tk.Label(window, text="Όνομα Σκοπευτή Δεύτερου Στόχου").grid(row=2)
#tk.Label(window, text="Όνομα Σκοπευτή Τρίτου Στόχου").grid(row=3)

'''
tk.Label(window, text="Τέταρτος Στόχος").grid(row=3)
tk.Label(window, text="Πέμπτος Στόχος").grid(row=4)
tk.Label(window, text="Έκτος Στόχος").grid(row=5)
tk.Label(window, text="Έβδομος Στόχος").grid(row=6)
tk.Label(window, text="Όγδοος Στόχος").grid(row=7)
'''
array=[]
array2=[]
counter_lines=0
for i in range(5):
	counter_lines+=1
	temp_str="Όνομα Σκοπευτή "+str(counter_lines)+"ου Στόχου"
	temp=tk.Label(window, text=temp_str).grid(row=(counter_lines+1))
	temp2 = tk.Entry(window,width=50)
	temp2.grid(row=(counter_lines+1),column=1)
	array.append(temp)
	array2.append(temp2)


#e1 = tk.Entry(window,width=50)
#e2 = tk.Entry(window,width=50)
#e3 = tk.Entry(window,width=50)
#e4 = tk.Entry(window,width=50)
'''

e5 = tk.Entry(window,width=50)
e6 = tk.Entry(window,width=50)
e7 = tk.Entry(window,width=50)
e8 = tk.Entry(window,width=50)
e9 = tk.Entry(window,width=50)
e10 = tk.Entry(window,width=50)
e11 = tk.Entry(window,width=50)
e12 = tk.Entry(window,width=50)
e13 = tk.Entry(window,width=50)
'''
#e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)
#e3.grid(row=2, column=1)
#e4.grid(row=3, column=1)
'''
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)
e8.grid(row=7, column=1)
e9.grid(row=8, column=1)
e10.grid(row=9, column=1)
e11.grid(row=10, column=1)
e12.grid(row=11, column=1)
e13.grid(row=12,column=1)
'''

button1=tk.Button(window, text="Eπόμενο")
button1.place(x=580, y=300)

information_array=[]

def close_second_window(event):
	file = open("onomata.txt", "w+")
	#file.write(str((e1.get()))+"\n")
	for i in range(5):
		temp=array2[i].get()
		file.write(str((temp))+"\n")
	
	#file.write(str((e3.get()))+"\n")
	#file.write(str((e4.get()))+"\n")


	'''
	information_array.append(e4.get())
	information_array.append(e5.get())
	information_array.append(e6.get())
	information_array.append(e7.get())
	information_array.append(e8.get())
	information_array.append(e9.get())
	information_array.append(e10.get())
	information_array.append(e11.get())
	information_array.append(e12.get())
	information_array.append(e13.get())
	'''
	
	file.close()
	window.destroy()
	
	
	import third_window
	#window.destroy()
	#create_new_window('<Button-1>')

button1.bind('<Button-1>',close_second_window)


window.mainloop()