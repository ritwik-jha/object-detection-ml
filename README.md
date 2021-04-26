# IMAGE OBJECT DETECTOR

## Description
Object Detector is an desktop app made using python tkinter framework and aws rekognition service at backend. This app is a frontend for aws rek. We have used the aws rek api to
integrate this app with aws machine learning machinery. 

This app provides us the following features:
1. Object Detection
2. Facial Expression Analysis
3. Celebrity Recognition
4. Text Extract

## Usage
To use this app the user needs an aws account and [aws cli](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) software installed. 

Now the user has to login to the aws account from aws cli.
```bash
aws cli configure
```
After this the user needs to enter their credentials. 

Now we are all set to use the app.

To run the app we first need to clone this repositiory:
```bash
git clone <link_to_this_repo>
```
In the cloned directory:
```bash
python gui.py
```

This will launch the application 
![image](https://user-images.githubusercontent.com/59885389/116109267-41126680-a6d2-11eb-8d0d-fc88ebe65132.png)

## Demo
First we load the image and then press the desired button.
### Object Detection 


