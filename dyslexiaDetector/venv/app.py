from flask import Flask
import os
from flask import request
import PdfToDoc

app = Flask(__name__)

@app.route("/")
def homePage():
    # do your things here
    print("/")
    #os.system('')
    return "Welcome to the Dyslexia Detector app,You will be redirected soon..."
#1.Eye tracking with feeded video .
@app.route("/EyeTracking")
def eyeTracking1():
    # do your things here
    print("/")
    os.system('EyeTracking.py')
    return "Eyetracking completed!! Click on back to go to homepage"

#2.Eye tracking with web cam
@app.route("/webcamTracking")
def webcamTracking():
    print("/webcam")
    # do your things here
    os.system('webcamTracking.py')
    return "It works!"

#3.This will change the speech part to text.
@app.route("/speechToText")
def speechToText():
    print("/stt")
    os.system('SpeechToText.py')
    return "It works!"
#4.This will be converting pdf to document with given fonts.
@app.route("/BooksConverter", methods = ['POST', 'GET'])
def BooksConverter():
    print("/PDF TO DOC")
    result=""
    if request.method == 'POST':
        result = request.form
        result = result.get('browse')
        print(result)

    PdfToDoc.PdfToDoc(result)
    print("it works")
    return "it works"


if __name__ == "__main__":
    app.run()


