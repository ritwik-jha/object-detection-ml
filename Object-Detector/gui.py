from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title('Image Detector')
root.geometry('1115x750')

def load_image():
    root.filename = filedialog.askopenfilename(initialdir='/', title='Select Image', filetypes=(('png files','*.png'), ('jpg files','*.jpg')))
    global image
    image = ImageTk.PhotoImage(Image.open(root.filename))
    Label(root, image=root.filename).grid(row=2, column=0)

frame_1 = LabelFrame(root)
frame_1.grid(row=0, column=0, padx=10)

Label(frame_1, text='Put Your Image').grid(row=0, column=0, columnspan=3, padx=500, pady=300)

load_button = Button(root, text='Load Image', command=load_image, padx=20, pady=20)
load_button.grid(row=1, column=0, pady=20)

root.mainloop()