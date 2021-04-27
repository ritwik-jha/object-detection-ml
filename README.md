# IMAGE OBJECT DETECTOR

## Description
Object Detector is an desktop app made using python tkinter framework and aws rekognition service at backend. This app is a frontend for aws rek. We have used the aws rek api to
integrate this app with aws machine learning machinery. 

This app provides us the following features:
1. Object Detection
2. Facial Expression Analysis
3. Celebrity Recognition
4. Text Extract

The app uses AWS Rekognition Service at backend. The uploaded image is first stored in a S3 bucket from where rek retrieves the image processes it and returns us the output in json format. The app then processes the json output to give the desired output on the image. 

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
![image](https://user-images.githubusercontent.com/59885389/116110621-7ff4ec00-a6d3-11eb-8316-100094ca0d59.png)

Output:

![image](https://user-images.githubusercontent.com/59885389/116110999-d82bee00-a6d3-11eb-83f3-784094af4a51.png)


### Facial Expression Analysis
![image](https://user-images.githubusercontent.com/59885389/116111329-2b9e3c00-a6d4-11eb-9897-c332d4f7eeae.png)

Output:

![image](https://user-images.githubusercontent.com/59885389/116111435-453f8380-a6d4-11eb-98bb-01598e6fc85d.png)

### Celebrity Recognition
![image](https://user-images.githubusercontent.com/59885389/116111580-6a33f680-a6d4-11eb-9582-1c4189e3b8b3.png)

Output:

![image](https://user-images.githubusercontent.com/59885389/116111705-8899f200-a6d4-11eb-9533-e4b15d70cec3.png)

### Text Extract
![image](https://user-images.githubusercontent.com/59885389/116112003-c860d980-a6d4-11eb-9973-ac0954cb6f81.png)

Output:

![image](https://user-images.githubusercontent.com/59885389/116112066-d7e02280-a6d4-11eb-936d-d48b0bfb6a9b.png)





