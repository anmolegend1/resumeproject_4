from tkinter import *
root = Tk()
root.title('Anmolegend_1 ')
def click():
    mylabel=Label(root,text="Thanks for clicking").pack()


mybutton=Button(root,text="Click me",padx=50,pady=10,command=click).pack()

root.mainloop()