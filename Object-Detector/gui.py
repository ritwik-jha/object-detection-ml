from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import boto3
import cv2

region = "ap-south-1"
bucket = "tkobdetectproject"
s3 = boto3.resource('s3')
rek = boto3.client('rekognition' , region )

root = Tk()
root.title('Image Detector')
root.geometry('1110x725')

def load_image():
    root.filename = filedialog.askopenfilename(initialdir='/', title='Select Image', filetypes=(('png files','*.png'), ('jpg files','*.jpg')))
    global image_loc
    image_loc = root.filename
    global image
    img = Image.open(root.filename)
    img = img.resize((1100, 600), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(img)
    global image_label
    image_label = Label(root, image=image)
    frame_1.destroy()
    image_label.grid(row=0, column=0, columnspan=3)

def remove_image():
    image_label.destroy()
    frame_1 = LabelFrame(root)
    frame_1.grid(row=0, column=0, padx=10, columnspan=3)
    Label(frame_1, text='Put Your Image').grid(row=0, column=0, columnspan=3, padx=500, pady=300)


def object_detection(): 
    s3.Bucket(bucket).upload_file(image_loc , 'image_to_detect.png')
    rek = boto3.client('rekognition' , region )
    response = rek.detect_labels(
            Image={
                'S3Object': {
                'Bucket': bucket,
                'Name': 'image_to_detect.png',
                }
            },
                MaxLabels=10,
                MinConfidence=60
    )
    for i in range(5):
        print ( response['Labels'][i]['Name'] )




frame_1 = LabelFrame(root)
frame_1.grid(row=0, column=0, padx=10, columnspan=3)

Label(frame_1, text='Put Your Image').grid(row=0, column=0, columnspan=3, padx=500, pady=300)

load_button = Button(root, text='Load Image', command=load_image, padx=20, pady=20)
load_button.grid(row=1, column=0, pady=20)

submit_button = Button(root, text='Submit', command=object_detection, padx=20, pady=20)
submit_button.grid(row=1, column=1)

clear_image_button = Button(root, text='Remove Image', command=remove_image, padx=20, pady=20)
clear_image_button.grid(row=1, column=2)

root.mainloop()