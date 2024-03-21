from tkinter import *


#intialize tkinter
application=Tk()

#Window size
application.geometry('1020x630')

#prevent from maximizing
application.resizable(False,False)

#window title
application.title('My Restraunt- Invoicing System')

#Window Background color
application.config(bg='#1C2833')

#top panel
top_panel=Frame(application, bd=1, relief=FLAT)
top_panel.pack(side=TOP)

#title tag
title_tag=Label(top_panel, text= 'Invoicing System',fg='#EAEDED',font=('Quick Argani',32),bg='#1C2833',width=27)
title_tag.grid(row=0,column=0)

#left panel
left_panel=Frame(application,bd=1,relief=FLAT)
left_panel.pack(side=LEFT)

#cost panel
cost_panel=Frame(left_panel,bd=1,relief=FLAT)
cost_panel.pack(side=BOTTOM)

#food panel
food_panel = LabelFrame(left_panel,text='Food',font=('Quick Argani',21,'bold'),bd=1,relief=FLAT,fg='#58D68D')
food_panel.pack(side=LEFT)

#drink panel
drink_panel = LabelFrame(left_panel,text='drink',font=('Quick Argani',21,'bold'),bd=1,relief=FLAT,fg='#7D3C98')
drink_panel.pack(side=LEFT)

#desert panel
desert_panel = LabelFrame(left_panel,text='desert',font=('Quick Argani',21,'bold'),bd=1,relief=FLAT,fg='#D4AC0D')
desert_panel.pack(side=LEFT)

#right panel
right_panel=Frame(application,bd=1,relief=FLAT)
right_panel.pack(side=RIGHT)

#calculator panel
calculator_panel=Frame(right_panel,bd=1,relief=FLAT,bg='#EAEDED')
calculator_panel.pack()

#invoice panel
invoice_panel=Frame(right_panel,bd=1,relief=FLAT,bg='#EAEDED')
invoice_panel.pack()

#button panel
button_panel=Frame(right_panel,bd=1,relief=FLAT,bg='#EAEDED')
button_panel.pack()

#product list
food_list=['chicken','lamb','salmon','hake','kebabs','pizza1','pizza2','pizza3']
drink_list=['lemonade','soda','juice','cola','wine1','wine2','beer1','beer2']
dessert_list=['ice cream','fruit','brownies','pudding','cheesecake','cake1','cake2','waffle']

#create food item
food_box=[]
food_text=[]
food_variables=[]
counter=0
for food in food_list:
    #create checkbutton
    food_variables.append('')
    food_variables[counter]=IntVar()
    food=Checkbutton(food_panel,
                     text=food.title(),
                     font=('Quick Argani',15,'bold'),
                     onvalue=1,
                     offvalue=0,
                     variable= food_variables[counter])
    food.grid(row=counter,
              column=0,
              sticky=W)

    #create input boxes
    food_box.append('')
    food_text.append('')
    food_box[counter]= Entry(food_panel,font= ('Quick Argani',15,'bold'),bd=1,width=6,
                             state=DISABLED,textvariable=food_text[counter])
    food_box[counter].grid(row=counter,column=1)
    counter+=1

#create drink item

drink_variables=[]
counter=0
for drink in drink_list:
    drink_variables.append('')
    drink_variables[counter]=IntVar()
    drink=Checkbutton(drink_panel,text=drink.title(),font=('Quick Argani',15,'bold'),onvalue=1,offvalue=0)
    drink.grid(row=counter,column=0,sticky=W)
    counter+=1

#create dessert item

dessert_variables=[]
counter=0
for dessert in dessert_list:
    dessert_variables.append('')
    dessert_variables[counter]=IntVar()
    dessert=Checkbutton(desert_panel,text=dessert.title(),font=('Quick Argani',15,'bold'),onvalue=1,offvalue=0)
    dessert.grid(row=counter,column=0,sticky=W)
    counter+=1


#prevent from closing
application.mainloop()