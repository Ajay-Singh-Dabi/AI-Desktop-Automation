import os
import smtplib
import webbrowser

from datetime import datetime
import pyttsx3
import datetime
import pywhatkit as kit
import speech_recognition as sr
import wikipedia
import operator
import pytesseract
import pyjokes
import cv2
from bs4 import BeautifulSoup
from PIL import Image
import requests

"""
First getting the voices provided
by the Microsoft inbuilt 
"""
runner = pyttsx3.init('sapi5')
voices = runner.getProperty('voices')
runner.setProperty('voice', voices[0].id)

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.11 Safari/537.3'}


def shutdown():
    os.system("shutdown /s /t 0")


def restart():
    os.system("shutdown /r /t 0")


def starting_password():
    speak("Password")
    password = "python"
    user = take_command().lower()

    if user == password:
        speak("Online Successful")
    else:
        shutdown()


def speak(audio):
    runner.say(audio)
    runner.runAndWait()


def take_command():
    # lis = sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("Listening...")
    #     lis.pause_threshold = 1
    #     lis.adjust_for_ambient_noise(source)
    #     audio = lis.listen(source)

    # try:
    #     print("Recognizing...")
    #     message = lis.recognize_google(audio, language='en-in')
    #     print(f"User said: {message}\n")

    # except Exception as e:
    #     print("Say that again please...")
    #     return "None"
    # return message
    message = str(input("Enter the Message: "))
    return message


def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        'x' : operator.mul,
        'divided' :operator.__truediv__,
        'Mod' : operator.mod,
        'mod' : operator.mod,
        '^' : operator.xor,
        }[op]


def evaluate(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)


def calculator():
    speak("What should i calculate")
    str = take_command().lower()
    print(str)
    ans = (evaluate(*(str.split())))
    speak(ans)


def starting_wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir!")

    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("What Can i Help you with")

def secure():
    img = Image.open("C:/Users/OMEN/Documents/MINI_PROJECT/car.jpg")
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

    rs = pytesseract.image_to_string(img)
    print(rs)

    with open('code1.txt', mode='w') as file:
       file.write(rs)
       print("Done with image to text.")


def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    print(location)
    speak(location)
    print(time)
    speak(time)
    print(info)
    print(info)
    print(weather + "Â° Celcius" )
    speak(weather +"Â° Celcius")



if __name__ == '__main__':
    starting_password()
    starting_wish()
    while True:

        message = take_command().lower()

        if 'calculate' in message:
            calculator()

        elif 'tell me a joke' in message:
            joke=pyjokes.get_joke()
            print(joke)
            speak(joke)
        
        
        elif 'study mode' in message:
            host_path = 'C:/Windows/System32/drivers/etc/hosts'
            redirect = "127.0.0.1"

            websites = ["facebook.com",
                        "www.facebook.com",
                        "www.instagram.com",
                        "https://www.youtube.com/c/BBKiVines"]

            while True:
                with open(host_path, "r+") as f:
                    content = f.read()
                    for sites in websites:
                         if sites not in content:
                             f.write(redirect + " " + sites + "\n")
                break

            speak("Sir your study mode is on do you want me disable your browsers too")
            command = take_command().lower()
            if 'yes' or 'sure' in command:
                os.system("taskkill /im chrome.exe /f")
                os.system("taskkill /im opera.exe /f")
            speak("Browsers Closed")
                
        
        elif 'exit study' in message:
            host_path = 'C:/Windows/System32/drivers/etc/hosts'

            websites = ["facebook.com",
                        "www.facebook.com",
                        "www.instagram.com",
                        "https://www.youtube.com/c/BBKiVines"]
    
            while True:
                with open(host_path, "r+") as f:
                    content = f.readlines()
                    f.seek(0)
                    for line in content:
                        if not any(site in line for site in websites):
                            f.write(line)
                    f.truncate()
                break
            speak("sir study mode deactivated you are good to go")

        elif 'play music' in message:
            music_dir = "D:\\some app\\Songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))
        
        elif 'security mode' in message:
            secure()

        elif 'open face reader' in message:
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
            cap = cv2.VideoCapture(0)
            while 1:
                ret, img = cap.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_color = img[y:y+h, x:x+w]
                    eyes = eye_cascade.detectMultiScale(roi_gray)
                    for (ex,ey,ew,eh) in eyes:
                        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
                        cv2.imshow('img',img)
                        k = cv2.waitKey(30) & 0xff
                        if k == 27:
                            break
            cap.release()
            cv2.destroyAllWindows()

        elif 'weather update' in message:
            speak("Enter the name of city")
            city = input("Enter the Name of City -> ")
            city = city+" weather"
            weather(city)
            print("")

        elif 'send whatsapp message' in message:
            speak("What should I send")
            cm=take_command().lower()
            speak("Whome should I send the message")
            cm2=take_command().lower()
            if 'ajay' in cm2:
                num = "phone number with country code"
            kit.sendwhatmsg(num,cm, 10, 9)


        elif 'youtube' in message:
            webbrowser.open("youtube.com")

        elif 'open google' in message:
            speak("what should i search")
            cm = take_command().lower()
            webbrowser.open(f"{cm}")

        elif 'open quora' in message:
            webbrowser.open("quora.com")

        elif 'open stackoverflow' in message:
            webbrowser.open("stackoverflow.com")

        elif 'open cricbuzz' in message:
            webbrowser.open("cricbuzz.com")

        elif 'open facebook' in message:
            webbrowser.open("facebook.com")

        

        elif 'the time' in message:
            start_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {start_time}")

        elif 'open pycharm' in message:
            py_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.2\\bin\\pycharm64.exe"
            os.startfile(py_path)

        
        elif 'email to ajay' in message:
            def send_email(receiver, mess):
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.ehlo()
                with open("pass.txt", "r+") as f:
                    password = f.readline()

                server.login('sender email', f"{password}")
                server.sendmail('sender email', receiver, mess)
                server.close()
            
            try:
                speak("What should I say?")
                content = take_command().lower()
                to = "receiver email"
                send_email(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send the Email")

        
        elif 'wikipedia' in message:
            speak('Searching Wikipedia')
            message = message.replace("Wikipedia", "")
            result = wikipedia.summary(message, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        
        
        elif 'sleep' in message:
            speak("thank you sir until next time")
            break





