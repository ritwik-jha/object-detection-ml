from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ExifTags, ImageColor, ImageFont
import boto3
import cv2
import random
import string

region = "ap-south-1"
bucket = "tkobdetectproject"
s3 = boto3.resource('s3')
rek = boto3.client('rekognition' , region )

root = Tk()
root.title('Image Detector')
root.geometry('1110x810')
root.resizable(0,0)
#root.configure(bg='grey')

def creating_s3_bucket():
    if region is None:
        s3_client = boto3.client('s3')
        s3_client.create_bucket(Bucket=bucket)
    else:
        s3_client = boto3.client('s3', region_name=region)
        location = {'LocationConstraint': region}
        s3_client.create_bucket(Bucket=bucket, CreateBucketConfiguration=location)

def load_image():
    root.filename = filedialog.askopenfilename(initialdir='C:/Users/Ritwik Jha/Desktop/Resources/PROJECTS/graphical/Object-Detector', title='Select Image', filetypes=(('png files','*.png'), ('jpg files','*.jpg')))
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
    image_label.grid(row=0, column=0, columnspan=4)

def remove_image():
    image_label.destroy()
    frame_1 = LabelFrame(root)
    frame_1.grid(row=0, column=0, padx=10, columnspan=4)
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
    op_win = Toplevel()
    global final_img
    final_img = ImageTk.PhotoImage(img)
    Label(op_win, image=final_img).grid(row=0, column=0)
    #img.show()


def rek_connection_ob_detect(): 
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

def expression_detect(response):
    #global img_la
    #global im1
    faces = []
    global display_im
    x = response['FaceDetails']
    op_win = Toplevel()
    for i in range(len(x)):
        y = x[i]
        box = y['BoundingBox']
        w = box['Width']
        h = box['Height']
        l = box['Left']
        t = box['Top']
        face = Image.open(image_loc)
        imgWidth, imgHeight = face.size
        left = imgWidth * l
        top = imgHeight * t
        width = imgWidth * w
        height = imgHeight * h
        cropped_face = face.crop((left, top, left+width, top+height))
        cropped_face = cropped_face.resize((300, 300), Image.ANTIALIAS)
        display_im = ImageTk.PhotoImage(cropped_face)
        
        img_la = Label(op_win, image=display_im)
        img_la.grid(row=0, column=0)
        age = y['AgeRange']
        age_string = 'Age: {} to {}'.format(age['Low'],age['High'])
        Label(op_win, text=age_string).grid(row=1, column=i, padx=10, 
        pady=10)
        Label(op_win, text='APPEARENCE:').grid(row=3, column=i, sticky=W)
        Label(op_win, text='Smile: {}'.format(y['Smile']['Value'])).grid(row=4, column=i)
        Label(op_win, text='Eyeglasses: {}'.format(y['Eyeglasses']['Value'])).grid(row=5, column=i)
        Label(op_win, text='Sunglasses: {}'.format(y['Sunglasses']['Value'])).grid(row=6, column=i)
        Label(op_win, text='Gender: {}'.format(y['Gender']['Value'])).grid(row=7, column=i)
        Label(op_win, text='Beard: {}'.format(y['Beard']['Value'])).grid(row=8, column=i)
        Label(op_win, text='EMOTIONS:').grid(row=9, column=i, sticky=W)
        for k in range(len(y['Emotions'])):
            if y['Emotions'][k]['Confidence'] >= 80:
                Label(op_win, text='{}'.format(y['Emotions'][k]['Type'])).grid(row=10+k, column=i)
    


def rek_connection_expression(): 
    s3.Bucket(bucket).upload_file(image_loc , 'image_to_detect.png')
    rek = boto3.client('rekognition' , region )
    response = rek.detect_faces(
    Image= {
        "S3Object": {
            "Bucket": bucket,
            "Name": "image_to_detect.png"
        }
    },
    Attributes= [
        "ALL"
    ]
    )
    expression_detect(response)

def celeb_detect(response):
    global celeb_image_processed
    celeb_image = Image.open(image_loc)
    draw = ImageDraw.Draw(celeb_image)
    imgWidth, imgHeight = celeb_image.size
    x = response['CelebrityFaces'][0]['Name']
    y = response['CelebrityFaces'][0]['Face']['BoundingBox']
    w = y['Width']
    h = y['Height']
    l = y['Left']
    t = y['Top']

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
    draw.rectangle([left,top, left + width, top + height], outline='#00FF00')
    celeb_image = celeb_image.resize((600, 600), Image.ANTIALIAS)
    celeb_image_processed = ImageTk.PhotoImage(celeb_image)
    op_win = Toplevel()
    Label(op_win, image=celeb_image_processed).grid(row=0, column=0)
    Label(op_win, text=x, font=20).grid(row=1, column=0, padx=20, pady=20)


    

def rek_connection_celeb(): 
    s3.Bucket(bucket).upload_file(image_loc , 'image_to_detect.png')
    rek = boto3.client('rekognition' , region )
    response = rek.recognize_celebrities(
    Image= {
        "S3Object": {
            "Bucket": bucket,
            "Name": "image_to_detect.png"
        }
    },
    )
    celeb_detect(response)

def text_detect(response):
    op_win = Toplevel()
    #op_win.geometry('300x300')
    for i in range(len(response['TextDetections'])):
        if response['TextDetections'][i]['Type'] == 'WORD':
            Label(op_win, text=response['TextDetections'][i]['DetectedText'], font=20).grid(row=i, column=0)

def rek_connection_text():
    s3.Bucket(bucket).upload_file(image_loc , 'image_to_detect.png')
    rek = boto3.client('rekognition' , region )
    response = rek.detect_text(
    Image= {
        "S3Object": {
            "Bucket": bucket,
            "Name": "image_to_detect.png"
        }
    },
    )
    text_detect(response)

def comp_image_load(number):
    global face_comp_image_loc
    face_comp_image_loc = {}
    global image_1
    global image_label
    root.filename = filedialog.askopenfilename(initialdir='C:/Users/Ritwik Jha/Desktop/Resources/PROJECTS/graphical/Object-Detector', 
    title='Select Image', filetypes=(('png files','*.png'), ('jpg files','*.jpg')))
    if number == 1:
        face_comp_image_loc['first_image_loc'] = root.filename
        first_img = Image.open(face_comp_image_loc['first_image_loc'])
        first_img = first_img.resize((400, 400), Image.ANTIALIAS)
        image_1 = ImageTk.PhotoImage(first_img)
        image_label_1 = Label(new_win, image=image_1)
        #image_frame_1.destroy()
        image_label_1.grid(row=0, column=0)
    
    elif number == 2:
        face_comp_image_loc['second_image_loc'] = root.filename
        second_img = Image.open(face_comp_image_loc['second_image_loc'])
        second_img = second_img.resize((400, 400), Image.ANTIALIAS)
        image_2 = ImageTk.PhotoImage(second_img)
        image_label_2 = Label(new_win, image=image_2)
        #image_frame_2.destroy()
        image_label_2.grid(row=2, column=1)
def face_comp():
    #root.destroy()
    global new_win
    new_win = Toplevel()
    new_win.title('Face Comparison')
    new_win.geometry('1210x800')
    global image_frame_1
    img_frame_1 = LabelFrame(new_win)
    img_frame_1.grid(row=0, column=0, padx=5, pady=10)
    global image_frame_2
    img_frame_2 = LabelFrame(new_win)
    img_frame_2.grid(row=0, column=1, padx=5, pady=10)
    Label(img_frame_1, text='Put Your Image').grid(row=0, column=0, padx=250, pady=250)
    Label(img_frame_2, text='Put Your Image').grid(row=0, column=0, padx=250, pady=250)
    Button(new_win, text='Load First Image', command= lambda: comp_image_load(1), padx=5, pady=5).grid(row=1, column=0, padx=10, pady=10)
    Button(new_win, text='Load Second Image', command= lambda: comp_image_load(2), padx=5, pady=5).grid(row=1, column=1, padx= 10, pady=10)
    #new_win.mainloop()


creating_s3_bucket()
frame_1 = LabelFrame(root)
frame_1.grid(row=0, column=0, padx=10, columnspan=4)

Label(frame_1, text='Put Your Image').grid(row=0, column=0, columnspan=5, padx=500, pady=300)

load_button = Button(root, text='Load Image', command=load_image, padx=20, pady=20)
load_button.grid(row=1, column=0, pady=20)

clear_image_button = Button(root, text='Remove Image', command=remove_image, padx=20, pady=20)
clear_image_button.grid(row=1, column=3)

ob_detect_button = Button(root, text='Object Detection', command=rek_connection_ob_detect, padx=20, pady=20)
ob_detect_button.grid(row=2, column=0, pady=10)

face_ana_button = Button(root, text='Expression Analysis', command=rek_connection_expression, padx=20, pady=20)
face_ana_button.grid(row=2, column=1, pady=10)

celeb_recog_button = Button(root, text='Celebrity Recognition', command=rek_connection_celeb, padx=20, pady=20)
celeb_recog_button.grid(row=2, column=2, pady=10)

text_in_image_button = Button(root, text='Extract Text', command=rek_connection_text, padx=20, pady=20)
text_in_image_button.grid(row=2, column=3, pady=10)

#face_comp_button = Button(root, text='Face Comparison', command=face_comp, padx=20, pady=20)
#face_comp_button.grid(row=2, column=4, pady=10)

root.mainloop()