from tkinter import *
root=Tk()
e=Entry(root,width=50)
e.pack()

def click():
    mylabel =Label(root,text="Hello " + e.get()).pack()

button = Button(root, text="Enter Your name", command=click).pack()
root.mainloop()