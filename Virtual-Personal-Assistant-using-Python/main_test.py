import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text
import os
import subprocess as sp
import requests
# from functions.online_ops import (
#     find_my_ip,
#     get_latest_news,
#     get_random_advice,
#     get_random_joke,
#     get_trending_movies,
#     get_weather_report,
#     play_on_youtube,
#     search_on_google,
#     search_on_wikipedia,
#     send_email,
#     send_whatsapp_message,
# )
# from functions.os_ops import (
#     open_calculator,
#     open_camera,
#     open_cmd,
#     open_notepad,
#     open_discord,
# )
from pprint import pprint

USERNAME = config("USER")
BOTNAME = config("BOTNAME")

paths = {
    "notepad": "c:\Windows\system32\notepad.exe",
    "discord": "c:\\Users\Paul\\AppData\\Local\\Discord\\app-1.0.9034\\Discord.exe",
    "calculator": "c:\Windows\system32\win32calc.exe",
}

engine = pyttsx3.init("sapi5")

# Set Rate
engine.setProperty("rate", 190)

# Set Volume
engine.setProperty("volume", 1.0)

# Set Voice (Female)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()


def greet_user():
    # Greets user according to the time
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")


def open_camera():
    sp.run("start microsoft.windows.camera:", shell=True)


def open_notepad():
    os.startfile(paths["notepad"])


def open_discord():
    os.startfile(paths["discord"])


def open_cmd():
    os.system("start cmd")


def open_calculator():
    sp.Popen(paths["calculator"])


def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")
        if not "exit" in query or "stop" in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak("Have a good day sir!")
            exit()
    except Exception:
        speak("Sorry, I could not understand. Could you please say that again?")
        query = "None"
    return query


if __name__ == "__main__":
    greet_user()
    while True:
        query = take_user_input().lower()
        print(query)

        if "open notepad" in query:
            open_notepad()

        elif "open discord" in query:
            open_discord()

        elif "open command prompt" in query or "open cmd" in query:
            open_cmd()

        elif "open camera" in query:
            open_camera()

         


# speak("Hello Korn 10000000")
# greet_user()

# take_user_input()

# try:
#     print(Hello)
# except:
#     print("Something went wrong")
# else:
#     print("Nothing went wrong")
