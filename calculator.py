from tkinter import *

root = Tk()
root.title('Calculator')


# text field
e = Entry(root, width=40)

#placing the text field
e.grid(row=0, column=0, columnspan=4, pady=10, padx=5)

def first_num(number):
    number = e.get() + str(number)
    e.delete(0, END)
    e.insert(0, number)

def clear():
    e.delete(0, END)

def add_op():
    global first_entry
    global mode
    mode = 'add'
    first_entry = e.get()
    e.delete(0, END)

def sub_op():
    global first_entry
    global mode
    mode = 'sub'
    first_entry = e.get()
    e.delete(0, END)

def mul_op():
    global first_entry
    global mode
    mode = 'mul'
    first_entry = e.get()
    e.delete(0, END)

def divide_op():
    global first_entry
    global mode
    mode = 'div'
    first_entry = e.get()
    e.delete(0, END)

def equals():
    second_number = int(e.get())
    global first_entry = int(first_entry)
    e.delete(0, END)
    if mode == 'add':
        e.insert(0, first_entry+second_number)
    elif mode == 'sub':
        e.insert(0, first_entry-second_number)
    elif mode == 'mul':
        e.insert(0, first_entry*second_number)
    elif mode == 'div':
        e.insert(0, first_entry/second_number)
    else:
        e.insert(0, 'error')

# creating buttons
button_cls = Button(root, text='clear', padx=106, pady=20, command=clear)

button_7 = Button(root, text='7', padx=20, pady=20, command= lambda: first_num(7))
button_8 = Button(root, text='8', padx=20, pady=20, command= lambda: first_num(8))
button_9 = Button(root, text='9', padx=20, pady=20, command= lambda: first_num(9))

button_4 = Button(root, text='4', padx=20, pady=20, command= lambda: first_num(4))
button_5 = Button(root, text='5', padx=20, pady=20, command= lambda: first_num(5))
button_6 = Button(root, text='6', padx=20, pady=20, command= lambda: first_num(6))

button_1 = Button(root, text='1', padx=20, pady=20, command= lambda: first_num(1))
button_2 = Button(root, text='2', padx=20, pady=20, command= lambda: first_num(2))
button_3 = Button(root, text='3', padx=20, pady=20, command= lambda: first_num(3))

button_add = Button(root, text='+', padx=20, pady=20, command=add_op)
button_sub = Button(root, text='-', padx=20, pady=20, command=sub_op)
button_mul = Button(root, text='*', padx=20, pady=20, command=mul_op)
button_div = Button(root, text='/', padx=20, pady=20, command=divide_op)
button_equals = Button(root, text='=', padx=82, pady=20, command=equals)

#placing buttons
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_sub.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_mul.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_div.grid(row=3, column=3)

button_add.grid(row=4, column=0)
button_equals.grid(row=4, column=1, columnspan=3)
button_cls.grid(row=5, column=0, columnspan=4)

root.mainloop()