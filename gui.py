from tkinter import *
from tkinter import filedialog
import stats as S
import keywords as K

root = Tk()
root.geometry("800x600")
root.title('File Picker')
f1_content = ''
f2_content = ''
global f1
global f2

stats_widgets = []

"""
	The function will return statistics
	of the input file.
"""
def input():

	# destroy old stats_widgets
	for i in stats_widgets:
		i.destroy()
	
	# Displaying Stats of input file
	Stats = S.stats_of_file(f1_content)

	# Heading
	l = Label(root, text = "Stats") 
	l.config(font =("Courier", 14)) 

	# Stats
	T = Text(root, height = 9, width = 80) 
	T.insert(END, Stats)

	l.pack()
	T.pack()
	# add these widgets to 'stats_widgets'
	stats_widgets.append(l)
	stats_widgets.append(T)

"""
	The function will return lines from input file
	which contains words for keyword file.
"""
def keyword():
	K.get_input_lines(f1.name, f2.name)


def open1():
	global f1_content, f1
	filename = filedialog.askopenfile(initialdir="./", title="Select a file", filetypes=(("txt", "*.txt"), ("all", "*.*")))
	if filename:
		f1 = filename
		f1_content = filename.read()
		input()


def open2():
	global f2
	filename = filedialog.askopenfile(initialdir="./", title="Select a file", filetypes=(("txt", "*.txt"), ("all", "*.*")))
	if filename:
		f2 = filename
		keyword()


# Opening input file button
my_btn1 = Button(root, text="Open input file", command=open1, width=20, height=2).place(x=300, y=400)

# Opening keyword file button
my_btn2 = Button(root, text="Open keyword file", command=open2, width=20, height=2).place(x=300, y=500)

root.mainloop()