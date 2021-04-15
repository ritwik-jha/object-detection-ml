from tkinter import *

root = Tk()
root.title('Calculator')


# text field
e = Entry(root, width=30)

#placing the text field
e.grid(row=0, column=0, columnspan=3, pady=10)

def first_num(number):
    number = e.get() + str(number)
    e.delete(0, END)
    e.insert(0, number)

def clear():
    e.delete(0, END)

# creating buttons
button_cls = Button(root, text='clear', padx=78, pady=20, command=clear)

button_7 = Button(root, text='7', padx=20, pady=20, command= lambda: first_num(7))
button_8 = Button(root, text='8', padx=20, pady=20, command= lambda: first_num(8))
button_9 = Button(root, text='9', padx=20, pady=20, command= lambda: first_num(9))

button_4 = Button(root, text='4', padx=20, pady=20, command= lambda: first_num(4))
button_5 = Button(root, text='5', padx=20, pady=20, command= lambda: first_num(5))
button_6 = Button(root, text='6', padx=20, pady=20, command= lambda: first_num(6))

button_1 = Button(root, text='1', padx=20, pady=20, command= lambda: first_num(1))
button_2 = Button(root, text='2', padx=20, pady=20, command= lambda: first_num(2))
button_3 = Button(root, text='3', padx=20, pady=20, command= lambda: first_num(3))

button_add = Button(root, text='+', padx=20, pady=20)
button_equals = Button(root, text='=', padx=49, pady=20)

#placing buttons
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_add.grid(row=4, column=0)
button_equals.grid(row=4, column=1, columnspan=2)
button_cls.grid(row=5, column=0, columnspan=3)

root.mainloop()