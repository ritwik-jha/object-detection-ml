from tkinter import *

root = Tk()
root.title('myFirstApp')

def evil():
    x = e.get()
    e.delete(0, END)
    e.insert(0, 'fuck you '+ x)

def clear():
    e.delete(0, END)

e = Entry(root, width=20)
e.insert(0, 'enter your name')

button_1 = Button(root, text='submit',padx=20, pady=20, command=evil)
button_submit = Button(root, text='clear',padx=20, pady=20, command=clear)

e.grid(row=0, column=0, columnspan=2)
button_1.grid(row=1, column=0)
button_submit.grid(row=1, column=1)

root.mainloop()