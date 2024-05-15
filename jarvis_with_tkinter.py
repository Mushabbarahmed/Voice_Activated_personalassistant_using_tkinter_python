from tkinter import *
from PIL import Image, ImageTk
# from tkinter.ttk import *
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
from pygame import mixer
import re


def ms(s1, stopper):
    # print("music")
    mixer.init()
    mixer.music.load(s1)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am  yor asssisstant - make easy for you. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.energy_threshold
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        speak(f"you have ask {query}")
        value.set(query)
        entry.update()
    except Exception as e:
        # a=0 +b
        # print(e)
        A = ("sorry,Say that again please...")
        speak(A)
        print(A)
        value.set(A)
        entry.update()
        # a=break
        return "None"

    return query


def alarm():
    mixer.init()
    mixer.music.load("eyes.mp3")
    mixer.music.play()

    while True:
        a = takeCommand()
        # a = input("enter if you want to stop")
        if a == "stop":
            mixer.music.stop()
            break


def assistant():
    wishMe()
    # takeCommand()
    var.set("Listening.")
    b1.update()
    b = 0
    while b < 3:
        import time

        value1.set("PLEASE WAIT")
        var.set("Listening...")
        b1.update()
        print(b)

        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        # if 'wikipedia' in query:
        #     speak('Searching Wikipedia...')
        #     query = query.replace("wikipedia", "")
        #     results = wikipedia.summary(query, sentences=2)
        #     speak("According to Wikipedia")
        #     print(results)
        #     speak(results)

        if 'youtube' in query:
            webbrowser.open("youtube.com")
            var.set("CLICK ASSISSTANT")
            value1.set("close")
            b1.update()
            break

        elif 'addname' in query:
            ms("addyoursound.mp3", "stop")
            break

        
        elif 'alarm' in query:
            # strTime = datetime.datetime.now().strftime("%H:%M:%S")
            # speak(f"The current time is {strTime}")
            try:
                path = re.compile(r'\d{2}:\d{2}')
                matches = path.finditer(query)
                for match in matches:
                    print(" ")
                h = str(match)
                time1 = h[40:45]
                # print(time1)
            except Exception as e:
                path = re.compile(r'\d{1}:\d{2}')
                matches = path.finditer(query)
                for match in matches:
                    print(" ")
                h = str(match)
                time1 = h[40:44]
                # print(time1)
            finally:
                if "p.m" in query:
                    ti = int(time1.split(":")[0]) + 12
                    tim = str(ti)
                    time2 = tim + ":" + time1.split(":")[1] + ":00"
                    print(time2)
                else:
                    time2 = "0" + time1 + ":00"
                    print(time2)

                def alarm():

                    mixer.init()
                    mixer.music.load("eyes.mp3")
                    mixer.music.play()

                    while True:
                        a = takeCommand()
                        print("enter if you want to stop")
                        if a == "stop":
                            mixer.music.stop()
                            break
                        # snooze()

            while True:

                time = datetime.datetime.now().strftime("%H:%M:%S")
                # print(time)
                if time2 == time:
                    alarm()
                    var.set("CLICK ASSISSTANT")
                    value1.set("close")
                    b1.update()
            break
        elif 'open google' in query:
            webbrowser.open("google.com")
            var.set("CLICK ASSISSTANT")
            value1.set("close")
            b1.update()
            break
        
        
        # elif 'open stackoverflow' in query:
        #     webbrowser.open("stackoverflow.com")
        #
        #
        # elif 'play music' in query:
        #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            var.set("CLICK ASSISSTANT")
            value1.set("close")
            b1.update()
            break

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        # elif b==1:

        try:
            b += 1
        except Exception as t:
            print(t)
        finally:
            var.set("CLICK ASSISSTANT")
            value1.set("close")
            b1.update()
        # finally:


# def stop():
#     if(b1['state']==NORMAL):
#         b1["state"]=DISABLED
#         b2["text"]="enable"
#     elif(b1['state']==DISABLED):
#         b1["state"]=NORMAL
#         b2["text"]="disable"
root = Tk()
root.title("ASSISSTANT -MAKE EASY FOR YOU")
image1 = Image.open("img.png")
photo1 = ImageTk.PhotoImage(image1)
root.wm_iconphoto(False, photo1)
root.geometry("400x400")
root.minsize(400, 400)
root.maxsize(400, 400)
image = Image.open("j.png")
# re = image.resize((401, 400), Image.ANTIALIAS)
re = image.resize((401, 400), Image.BILINEAR)
photo1 = ImageTk.PhotoImage(re)

pic2 = Label(image=photo1)
pic2.place(x=0, y=0)
image1 = Image.open("img.png")
re = image1.resize((100, 100), Image.BILINEAR)
photo11 = ImageTk.PhotoImage(re)
# pic1=Label(image=photo11)
# pic1.place(x=150,y=281)
var = StringVar()
var.set("CLICK ASSSISSTANT")
b1 = Button(root, textvariable=var, command=assistant, padx=80, pady=10, bg="black", fg="white",
            font="comicsansms,36,bold")
b1.pack(pady=10)
b2 = Button(root, image=photo11, command=assistant, padx=100, pady=100)
b2.place(x=150, y=290)
Label(text="YOU ASKED:").pack()
value = StringVar()
value.set("")
entry = Entry(text=value)
entry.pack()
value1 = StringVar()
value1.set(" close")
b3 = Button(root, textvariable=value1, command=root.destroy)
b3.pack()
# b2=Button(text="disable",command=stop)
# b2.pack()

root.mainloop()
