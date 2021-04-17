from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ExifTags, ImageColor, ImageFont
import boto3
import cv2

region = "ap-south-1"
bucket = "tkobdetectproject"
s3 = boto3.resource('s3')
rek = boto3.client('rekognition' , region )

root = Tk()
root.title('Image Detector')
root.geometry('1110x810')
root.resizable(0,0)

def load_image():
    root.filename = filedialog.askopenfilename(initialdir='/', title='Select Image', filetypes=(('png files','*.png'), ('jpg files','*.jpg')))
    global image_loc
    image_loc = root.filename
    global image
    global img
    img = Image.open(root.filename)
    img = img.resize((1100, 600), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(img)
    global image_label
    image_label = Label(root, image=image)
    frame_1.destroy()
    image_label.grid(row=0, column=0, columnspan=5)

def remove_image():
    image_label.destroy()
    frame_1 = LabelFrame(root)
    frame_1.grid(row=0, column=0, padx=10, columnspan=5)
    Label(frame_1, text='Put Your Image').grid(row=0, column=0, columnspan=5, padx=500, pady=300)

def object_detect(response):
    imgWidth, imgHeight = img.size
    draw = ImageDraw.Draw(img)
    x = response['Labels']
    for i in range(len(x)):
        y = x[i]['Instances']
        for j in range(len(y)):
            w = y[j]['BoundingBox']['Width']
            h = y[j]['BoundingBox']['Height']
            l = y[j]['BoundingBox']['Left']
            t = y[j]['BoundingBox']['Top']

            left = imgWidth * l
            top = imgHeight * t
            width = imgWidth * w
            height = imgHeight * h

            points = (
                    (left,top),
                    (left + width, top),
                    (left + width, top + height),
                    (left , top + height),
                    (left, top)
                    )
            name = response['Labels'][i]['Name']
            accuracy = response['Labels'][i]['Instances'][j]['Confidence']
            font = ImageFont.truetype('C:/Users/Ritwik Jha/anaconda3/Lib/site-packages/jupyterthemes/fonts/serif/ptserif/pt-serif-regular.ttf', 15)
            draw.rectangle([left,top, left + width, top + height], outline='#00FF00')
            #draw.text(((points[2][0]+points[3][0])/2,(points[2][1]+points[3][1])/2), response['Labels'][i]['Name'], fill=(0,0,0))
            draw.text((left+20,top+20), '{0}'.format(name), fill=(0,0,0), font=font)
    img.show()


def rek_connection(): 
    s3.Bucket(bucket).upload_file(image_loc , 'image_to_detect.png')
    rek = boto3.client('rekognition' , region )
    response = rek.detect_labels(
            Image={
                'S3Object': {
                'Bucket': bucket,
                'Name': 'image_to_detect.png',
                }
            },
                MaxLabels=50,
                MinConfidence=0
    )
    object_detect(response)


    




frame_1 = LabelFrame(root)
frame_1.grid(row=0, column=0, padx=10, columnspan=5)

Label(frame_1, text='Put Your Image').grid(row=0, column=0, columnspan=5, padx=500, pady=300)

load_button = Button(root, text='Load Image', command=load_image, padx=20, pady=20)
load_button.grid(row=1, column=0, pady=20)

clear_image_button = Button(root, text='Remove Image', command=remove_image, padx=20, pady=20)
clear_image_button.grid(row=1, column=4)

ob_detect_button = Button(root, text='Object Detection', command=rek_connection, padx=20, pady=20)
ob_detect_button.grid(row=2, column=0, pady=10)

face_ana_button = Button(root, text='Expression Analysis', command=rek_connection, padx=20, pady=20)
face_ana_button.grid(row=2, column=1, pady=10)

celeb_recog_button = Button(root, text='Celebrity Recognition', command=rek_connection, padx=20, pady=20)
celeb_recog_button.grid(row=2, column=2, pady=10)

text_in_image_button = Button(root, text='Extract Text', command=rek_connection, padx=20, pady=20)
text_in_image_button.grid(row=2, column=3, pady=10)

face_comp_button = Button(root, text='Face Comparison', command=rek_connection, padx=20, pady=20)
face_comp_button.grid(row=2, column=4, pady=10)

root.mainloop()