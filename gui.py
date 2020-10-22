from tkinter import *
from tkinter import filedialog
import stats as S
import keywords as K
import hist 

root = Tk()
root.geometry("800x600")
root.title('File Picker')
f1_content = ''
f2_content = ''
global f1
global f2

stats_widgets = []
stats_widgets_k = []

# for displaying histogram
def plot_histogram():
	hist.main(f1.name)


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

	hist_btn = Button(root, text="Plot Histogram", command=plot_histogram, width=18, height=2).place(x=300, y=400)

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
	for i in stats_widgets_k:
		i.destroy()

	input_lines = K.get_input_lines(f1.name, f2.name)

	# Heading
	l_k = Label(root, text = "Sentences with keywords") 
	l_k.config(font =("Courier", 14)) 

	# Lines
	T_k = Text(root, height = 5, width = 80) 
	T_k.insert(END, input_lines)

	l_k.pack()
	T_k.pack()
	
	# add these widgets to 'stats_widgets_k'
	stats_widgets_k.append(l_k)
	stats_widgets_k.append(T_k)
	stats_widgets.append(l_k)
	stats_widgets.append(T_k)

def open1():
	global f1_content, f1
	filename = filedialog.askopenfile(initialdir="./testfiles", title="Select a file", filetypes=(("txt", "*.txt"), ("all", "*.*")))
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
my_btn1 = Button(root, text="Open input file", command=open1, width=18, height=2).place(x=300, y=450)

#for message
msg='For refresh, click again on the OPEN INPUT FILE button and select the required file'
messageVar = Message(root, text = msg, relief = RAISED, width = 1000) 
messageVar.config(bg='white') 
messageVar.pack( ) 

# Opening keyword file button
my_btn2 = Button(root, text="Open keyword file", command=open2, width=18, height=2).place(x=300, y=500)

root.mainloop()