import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
from datetime import date
import random
import smtplib
import pywhatkit
import pyautogui
import datetime
import subprocess
import turtle
from turtle import *

engine = pyttsx3.init("sapi5")  # ms voice api
voice = engine.getProperty("voices")
print(voice[1].id)
engine.setProperty("voice", voice[2].id)

myvoice_assistant_name = "NOVA"

"""Personal Variables"""
name = "Insiya"
hobby = "Programming"
course = "Bachelor of Information Technology"
prog_lang = ["python", "javascript", "c++", "r"]
dob = "25 july 2003"

"""All current emails contact"""
emails_dict = {
    "my Gmail": "insiyaotmed409@gmail.com",
}

"""All current whatsapp contacts"""
whatsapp_dic = {
    "my number": "+91 8850542363",
}


# Python3 code to calculate age in years
def calculateAge(birthDate):
    today = date.today()
    age = (
        today.year
        - birthDate.year
        - ((today.month, today.day) < (birthDate.month, birthDate.day))
    )
    return age


fullname = "Insiya firoz haider rizvi"


"""Functions"""


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good morning mam")
    elif hour >= 12 and hour <= 17:
        speak("Good afternoon mam")
    elif hour >= 17 and hour <= 22:
        speak("Good evening mam")
    else:
        speak("Haven't you slept mam?")

    # speak(f"my name is {myvoice_assistant_name}, please enter the valid password")


def takecommand():
    """To take microphone input from user and return it as a string"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said {query}")
        # speak(query)
    except Exception as e:
        # print(e)
        x = "I cannot hear you proper, please speak louder"
        speak(x)
        return "None"
    return query


def sendEmail(to, email_content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("faizkhan.netpersonal.7@gmail.com", "cgfi mihk dgrs sztk")
    server.sendmail("faizkhan.netpersonal.7@gmail.com", to, email_content)
    server.close()


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


def doraemon():

    # function for position
    def my_goto(x, y):
        penup()
        goto(x, y)
        pendown()

    # Function for drawing eyes
    def eyes():
        fillcolor("#ffffff")
        begin_fill()
        tracer(False)
        a = 2.5
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                lt(3)
                fd(a)
            else:
                a += 0.05
                lt(3)
                fd(a)
        tracer(True)
        end_fill()

    # Function for drawing whisker
    def whisker():
        my_goto(-32, 135)
        seth(165)
        fd(60)
        my_goto(-32, 125)
        seth(180)
        fd(60)
        my_goto(-32, 115)
        seth(195)
        fd(60)
        my_goto(37, 135)
        seth(15)
        fd(60)
        my_goto(37, 125)
        seth(0)
        fd(60)
        my_goto(37, 115)
        seth(-13)
        fd(60)

    # Function for drawing mouth
    def mouth():
        my_goto(5, 148)
        seth(270)
        fd(100)
        seth(0)
        circle(120, 50)
        seth(230)
        circle(-120, 100)

    # Function for drawing band
    def band():
        fillcolor("#e70010")
        begin_fill()
        seth(0)
        fd(200)
        circle(-5, 90)
        fd(10)
        circle(-5, 90)
        fd(207)
        circle(-5, 90)
        fd(10)
        circle(-5, 90)
        end_fill()

    # Function for drawing nose
    def nose():
        my_goto(-10, 158)
        seth(315)
        fillcolor("#e70010")
        begin_fill()
        circle(20)
        end_fill()

    # Functin for drawing black eyes
    def black_eyes():
        seth(0)
        my_goto(-20, 195)
        fillcolor("#000000")
        begin_fill()
        circle(13)
        end_fill()

        pensize(6)
        my_goto(20, 205)
        seth(75)
        circle(-10, 150)
        pensize(3)

        # for drawing the white circle inside
        my_goto(-17, 200)
        seth(0)
        fillcolor("#ffffff")
        begin_fill()
        circle(5)
        end_fill()
        my_goto(0, 0)

    # Function for drawing face
    def face():
        fd(183)
        lt(45)
        fillcolor("#ffffff")
        begin_fill()
        circle(120, 100)
        seth(180)
        fd(121)
        pendown()
        seth(215)
        circle(120, 100)
        end_fill()
        my_goto(63.56, 218.24)
        seth(90)
        eyes()
        seth(180)
        penup()
        fd(60)
        pendown()
        seth(90)
        eyes()
        penup()
        seth(180)
        fd(64)

    # Function for drawing head
    def head():
        penup()
        circle(150, 40)
        pendown()
        fillcolor("#00a0de")
        begin_fill()
        circle(150, 280)
        end_fill()

    # Combining all functions to one
    def Doremon():
        head()
        band()
        face()
        nose()
        mouth()
        whisker()

        # For drawing the body outline
        my_goto(0, 0)
        seth(0)
        penup()
        circle(150, 50)
        pendown()
        seth(30)
        fd(40)
        seth(70)
        circle(-30, 270)

        # For filling the body color
        fillcolor("#00a0de")
        begin_fill()
        seth(230)
        fd(80)
        seth(90)
        circle(1000, 1)
        seth(-89)
        circle(-1000, 10)

        seth(180)
        fd(70)
        seth(90)
        circle(30, 180)
        seth(180)
        fd(70)

        seth(100)
        circle(-1000, 9)
        seth(-86)
        circle(1000, 2)
        seth(230)
        fd(40)

        circle(-30, 230)
        seth(45)
        fd(81)
        seth(0)
        fd(203)
        circle(5, 90)
        fd(10)
        circle(5, 90)
        fd(7)
        seth(40)
        circle(150, 10)
        seth(30)
        fd(40)
        end_fill()

        # For filling right palm color
        seth(70)
        fillcolor("#ffffff")
        begin_fill()
        circle(-30)
        end_fill()

        # For filling left foot color
        my_goto(103.74, -182.59)
        seth(0)
        fillcolor("#ffffff")
        begin_fill()
        fd(15)
        circle(-15, 180)
        fd(90)
        circle(-15, 180)
        fd(10)
        end_fill()

        # For filling right foot color
        my_goto(-96.26, -182.59)
        seth(180)
        fillcolor("#ffffff")
        begin_fill()
        fd(15)
        circle(15, 180)
        fd(90)
        circle(15, 180)
        fd(10)
        end_fill()

        # For filling left palm color
        my_goto(-184.67, -61.59)
        seth(70)
        fillcolor("#ffffff")
        begin_fill()
        circle(-30)
        end_fill()

        # For drawing the inner body circle
        my_goto(-103.42, 15.09)
        seth(0)
        fd(38)
        seth(230)
        begin_fill()
        circle(90, 260)
        end_fill()

        # For drawing the semicircle
        my_goto(5, -40)
        seth(0)
        fd(70)
        seth(-90)
        circle(-70, 180)
        seth(0)
        fd(70)

        # For drawing the bell
        my_goto(-103.42, 15.09)
        fd(90)
        seth(70)
        fillcolor("#ffd200")
        begin_fill()
        circle(-20)
        end_fill()
        seth(170)
        fillcolor("#ffd200")
        begin_fill()
        circle(-2, 180)
        seth(10)
        circle(-100, 22)
        circle(-2, 180)
        seth(170)
        circle(100, 22)
        end_fill()
        goto(-13.42, 15.09)
        seth(250)
        circle(20, 110)
        seth(90)
        fd(15)
        dot(10)
        my_goto(0, 150)

        black_eyes()

    # Window control
    screensize(800, 600, "#f0f0f0")
    screen = Screen()
    screen.setup(width=1.0, height=1.0)

    # Setting teh pen size
    pensize(3)

    # Setting the speed
    speed(20)
    Doremon()
    my_goto(250, -230)
    write("by INSIYA RIZVI 💓", font=("Arial", 15))
    mainloop()


def heartshape():

    # Creating a turtle object(pen)
    pen = turtle.Turtle()

    # Defining a method to draw curve
    def curve():
        for i in range(200):

            # Defining step by step curve motion
            pen.right(1)
            pen.forward(1)

    # Defining method to draw a full heart
    def heart():

        # Set the fill color to red
        pen.fillcolor("red")

        # Start filling the color
        pen.begin_fill()

        # Draw the left line
        pen.left(140)
        pen.forward(113)

        # Draw the left curve
        curve()
        pen.left(120)

        # Draw the right curve
        curve()

        # Draw the right line
        pen.forward(112)

        # Ending the filling of the color
        pen.end_fill()

    # Defining method to write text
    def txt():

        # Move turtle to air
        pen.up()

        # Move turtle to a given position
        pen.setpos(-68, 95)

        # Move the turtle to the ground
        pen.down()

        # Set the text color to lightgreen
        pen.color("lightgreen")

        # Write the specified text in
        # specified font style and size
        pen.write("Insiya Rizvi", font=("Verdana", 12, "bold"))

    # Draw a heart
    heart()

    # Write text
    txt()

    # To hide turtle
    pen.ht()


if __name__ == "__main__":
    wishme()
    # query = takecommand()
    # if "9067" in query:
    speak(f"Hello {name} mam Please tell me how may i help you")

    while True:
        query = takecommand().lower()

        """Logics for executing tasks"""

        def basiconvo():

            # Personal Details

            if "my name" in query:
                speak(f"mam, your name is {name}")
            elif "do you like mountain dew" in query:
                speak("yes i like mountain dew")
            elif "my full name" in query:
                speak(f"your full name is {fullname}")
            elif "my age" in query:
                speak(f"mam, you are {calculateAge(date(2002, 11, 12))} years old")
            elif "about me" in query:
                speak(
                    f"{fullname} is a student and a learning {hobby} who was born on {dob}, and is currently persuing {course} \
                    she has a knowledge of programming languages like {prog_lang}, but mainly work on {prog_lang[0]} and has created \
                        many projects using those languages"
                )

            elif "how are you" in query:
                speak("i'm fine mam, what about you")
            elif "who created you" in query:
                speak("i was created by insiya")
            elif "what is your name" in query:
                speak(f"my name is {myvoice_assistant_name}")
            elif "who are you" in query:
                speak(f"I am {myvoice_assistant_name}, a virtual assistant")
            elif "i am fine" in query:  # W
                speak("i'm glad you are fine")

            elif "nope" in query:  # need work
                speak("Okay mam")
            elif "can you sing" in query:  # W
                speak("no, i am a bad singer")
            elif "how old are you" in query or "what is your age" in query:  # W
                speak("i am 1 years old")
            elif "how many languages" in query:
                speak("as of now i can only speak english")
            elif "humans" in query:
                speak("yes i love humans")
            elif "are you a robot" in query:
                speak("i am your virtual assistant")
            elif "correct" in query:
                speak("see, i knew it")
            elif "not fine" in query:
                speak("oh, i hope you feel better, is there anything i can do?")
            elif (
                "can you be my girlfriend" in query
                or "can you be my boyfriend" in query
            ):
                speak("sorry, i am already taken")
            elif "love me" in query:
                speak("ofcourse i do")
            elif "where are you from" in query:
                speak("i am from your imagination")
            elif "is love" in query:
                speak("it is the 7th sense that destroy all other senses")
            elif "favourite colour" in query:
                speak("my favourite color is blue because i love the sky")
            elif "jarvis" in query:
                speak("yes mam, what can i do for you")
            elif "thank you" in query:
                speak("my pleasure mam")
            elif "job" in query:
                speak("thank you mam!")

        # calling the basic conversation
        basiconvo()

        if "wikipedia" in query:
            try:
                speak("searching wikipedia...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=1)
                speak("According to wikipedia")
                print(result)
                speak(result)
            except:
                speak("Sorry! i couldn't find it for some reason")

        elif "open youtube" in query:
            speak("opening youtube")
            # webbrowser.open("https://www.youtube.com/")
            urL = "https://www.youtube.com"
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register(
                "chrome", None, webbrowser.BackgroundBrowser(chrome_path)
            )
            webbrowser.get("chrome").open_new_tab(urL)

        elif "close chrome" in query:
            speak("closing chrome browser")
            os.system("taskkill /im firefox.exe /f")
            os.system("taskkill /im chrome.exe /f")

        elif "open google" in query:
            speak("opening google")
            # webbrowser.open("http://google.com")
            urL = "https://www.google.com"
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register(
                "chrome", None, webbrowser.BackgroundBrowser(chrome_path)
            )
            webbrowser.get("chrome").open_new_tab(urL)

        elif "open github" in query:
            speak("opening github")
            urL = "https://github.com/"
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register(
                "chrome", None, webbrowser.BackgroundBrowser(chrome_path)
            )
            webbrowser.get("chrome").open_new_tab(urL)

        elif "open vs code" in query:
            vs_path = (
                "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            )
            speak("opening vs code")
            os.startfile(vs_path)

        elif "make a note" in query:
            speak("what would you like me to write down?")
            notewrite = takecommand()
            note(notewrite)

            speak("I've made a note of that.")

        elif "play music" in query:
            try:
                music_dir = "C:\\Users\\User\\OneDrive\\Documents\\Faiz Khan Program\\Jarvis\\mymusic"
                songs = os.listdir(music_dir)
                print(songs)
                random = os.startfile(os.path.join(music_dir, songs[0]))
            except Exception as e:
                speak("Sorry mam, unable to play music")

        elif "test auto search" in query:
            """Need works"""
            import pyautogui
            import time

            speak("testing it")
            # print(pyautogui.position())

            pyautogui.click(498, 744, 1, 1, "left")
            pyautogui.click(497, 449, 1, 1, "left", duration=1)
            pyautogui.leftClick(601, 417, duration=1)

            speak("What do you wish to type mam?")
            input_query_insearchbar = takecommand()

            pyautogui.typewrite(input_query_insearchbar, interval=1)

            pyautogui.press("enter")

        elif "open chat" in query:
            import pyautogui
            import time

            pyautogui.click(498, 744, 1, 1, "left")
            pyautogui.click(497, 449, 1, 1, "left", duration=1)
            pyautogui.click(783, 640, 1, 1, "left", duration=1)

        elif "google search" in query:
            speak("what do you wish to search mam")
            ques = takecommand()
            speak(f"searching {ques} on google")
            pywhatkit.search(ques)

        elif "send an email" in query:
            try:
                speak("who do you wish to send an email to, mam?")
                mail_name = takecommand()
                if mail_name in emails_dict.keys():
                    speak("okay, What should i say?")
                    email_content = takecommand()
                    to = emails_dict.get(mail_name)
                    sendEmail(to, email_content)
                    speak("email has been sent!")
                else:
                    speak("sorry! This email is not available in my memory")
            except Exception as e:
                print(e)
                speak("sorry, i wasn't able to send the email")

        elif (
            "open whatsapp" in query or "open Whatsapp" in query
        ):  # need to change pyauto gui position
            speak("Roger that! mam")

            pyautogui.click(466, 752, 1, 1, "left")
            # pyautogui.click(697, 434, 1, 1, 'left', duration=1)

            # pyautogui.click(727, 631, 1, 1, 'left', duration=1)

        elif "whatsapp message" in query:  # need works
            try:
                speak("who do you wish to message mam?")
                whatsapp_name = takecommand()
                if whatsapp_name in whatsapp_dic.keys():
                    test = whatsapp_dic.get(whatsapp_name)
                    from datetime import timedelta, time

                    # import time
                    speak("okay, what should i say?")
                    my_message = takecommand()
                    # time.sleep(3)
                    time1 = datetime.datetime.now()
                    minu = 2
                    t = time(time1.hour, time1.minute)
                    # result = datetime.datetime.combine(date.today(), t) + timedelta(minutes=minu)
                    x = time1.strftime("%I")
                    print("\n")
                    speak(
                        f"seonding message by {x} o'oclock and {time1.minute + minu} minutes"
                    )
                    print(
                        f"sending message by {x} o'oclock and {time1.minute + minu} minutes"
                    )

                    pywhatkit.sendwhatmsg(
                        test, my_message, time1.hour, time1.minute + minu
                    )
                    speak("Message has been sent!")
            except:
                speak("Sorry mam, i was not able to send the message")

        elif "spam message" in query:
            """need works here"""
            import time

            try:
                # speak('Who do you want to spam mam?')
                # spamname = takecommand()
                # if spamname in whatsapp_dic.keys():
                speak("okay, and what will be the spam message?")
                spammsg = takecommand()
                # spammsg = input('enter: ')
                speak("ok, how many times to you want to spam it?")
                num_ofspam = takecommand()

                # message = input("Enter the message: ")
                # num_value = input("Enter num of times: ")
                # speak('roger that!')
                abc = int(num_ofspam)

                # pyautogui.click(612, 745, 1, 1, 'left')
                # pyautogui.click(697, 434, 1, 1, 'left', duration=1)

                # pyautogui.click(727, 631, 1, 1, 'left', duration=1)

                # pyautogui.click(289, 253, 1, 1, 'left', duration=7)

                # pyautogui.click(610, 693, 1, 'left', duration=1)
                speak(f"Sending spam messages")
                time.sleep(15)

                for i in range(abc):
                    pyautogui.typewrite(spammsg)
                    pyautogui.press("Enter")

                speak("spam messages has been sent!")
            except Exception as e:
                # print(e)
                speak("sorry! unable to send spam messages")

        elif "search on youtube" in query:
            speak("what topic do you want to search for on youtube?")
            topic = takecommand()
            speak(f"okay, playing a random video on the topic {topic}")
            pywhatkit.playonyt(topic)

        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")

        elif "the date" in query:
            date1 = date.today()
            print(date1)
            speak(date1)

        elif "sleep" in query:
            speak("Ok then, i am going to sleep, bye")
            quit()

        elif "joke" in query:
            import pyjokes

            speak(pyjokes.get_joke())

        elif "make doraemon" in query:
            doraemon()

        elif "make a heart" in query:
            heartshape()

        elif "close current window" in query:
            speak("Closing the current window mam!")
            pyautogui.click(1332, 20, 1, 1, "left")

        elif "lock window" in query:
            speak("Locking the window mam")
            import ctypes

            # Define the Windows API function
            user32 = ctypes.windll.user32
            LockWorkStation = user32.LockWorkStation

            # Call the LockWorkStation function to lock the PC
            LockWorkStation()

        elif "shutdown" in query or "shut down" in query:
            speak("mam, are you sure you want to shut down ?")
            surety = takecommand()
            if surety == "yes" or "yeah" in query:
                os.system("shutdown /s /t 1")
            else:
                speak("shut down cancelled")

    # else:
    #     speak("I'm sorry, You entered the wrong password")
    #     quit()
