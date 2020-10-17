from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("800x600")
root.title('File Picker')
f1=''
f2=''

'''
Use global f1 as input file and read @dummy
'''
def input():
    pass

'''
Use global f2 as keyword file and read @dummy
'''
def keyword():
    pass

def open1():
    global f1
    filename = filedialog.askopenfilename(initialdir="./", title="Select a file", filetypes=(("txt", "*.txt"), ("all", "*.*")))
    if filename:
        f1 = filename
        input()

def open2():
    global f2
    filename = filedialog.askopenfilename(initialdir="./", title="Select a file", filetypes=(("txt", "*.txt"), ("all", "*.*")))
    if filename:
        f2 = filename
        keyword()

my_btn1 = Button(root, text="Open input file", command=open1, width=20, height=2).place(x=300, y=400)

my_btn2 = Button(root, text="Open keyword file", command=open2, width=20, height=2).place(x=300, y=500)

root.mainloop()