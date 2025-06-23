import pyttsx3
import datetime

# Initialize speech engines
engine = pyttsx3.init()

# Function to speak
def speak(text):
    print(f"🗣️ Zion: {text}")
    engine.say(text)
    engine.runAndWait()

# Greet the user based on the current time
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")
    speak("I'm up and functioning...")