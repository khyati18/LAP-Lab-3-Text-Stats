from tkinter import *
from tkinter import filedialog
import stats as S

root = Tk()
root.geometry("800x600")
root.title('File Picker')
f1_content = ''
f2_content = ''

"""
	The function will return statistics
	of the input file.
"""
def input():
	
	# Displaying Stats of input file
	Stats = S.stats_of_file(f1_content)

	# Heading
	l = Label(root, text = "Stats") 
	l.config(font =("Courier", 14)) 

	# Stats
	T = Text(root, height = 5, width = 52) 
	T.insert(END, Stats)

	l.pack()
	T.pack()

"""
	The function will return lines from input file
	which contains words for keyword file.
"""
def keyword():

    pass

def open1():
    global f1_content
    filename = filedialog.askopenfile(initialdir="./", title="Select a file", filetypes=(("txt", "*.txt"), ("all", "*.*")))
    if filename:
    	f1_content = ""
    	for i in filename:
    		f1_content += i
    	input()

def open2():
    global f2_content
    filename = filedialog.askopenfile(initialdir="./", title="Select a file", filetypes=(("txt", "*.txt"), ("all", "*.*")))
    if filename:
    	f2_content = filename
    	keyword()

# Opening input file button
my_btn1 = Button(root, text="Open input file", command=open1, width=20, height=2).place(x=300, y=400)

# Opening keyword file button
my_btn2 = Button(root, text="Open keyword file", command=open2, width=20, height=2).place(x=300, y=500)

root.mainloop()