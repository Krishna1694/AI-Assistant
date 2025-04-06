import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile
import tempfile
import os
import time
import pyttsx3
from datetime import datetime
import noisereduce as nr

model = whisper.load_model("tiny")
engine = pyttsx3.init()

def speak(text):
    print("🤖", text)
    engine.say(text)
    engine.runAndWait()

def greet():
    speak("Welcome back sir. LUMOS is now online.")

def record(duration=5, fs=16000):
    speak("Ready")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    audio = audio.flatten()  # Needed for noisereduce
    reduced_audio = nr.reduce_noise(y=audio, sr=fs)
    return reduced_audio, fs

def transcribe(audio, fs):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        scipy.io.wavfile.write(f.name, fs, audio)
        temp_path = f.name

    result = model.transcribe(temp_path)
    os.remove(temp_path)
    return result["text"].lower()

def handle_command(command):
    command = command.lower()

    if "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")

    elif "date" in command:
        today = datetime.now().strftime("%B %d, %Y")
        speak(f"Today is {today}")

    elif "open google" in command:
        os.system("start https://google.com")
        speak("Opening Google")

    elif "open youtube" in command:
        os.system("start https://youtube.com")
        speak("Opening YouTube")

    elif "exit" in command or "stop" in command or "shutdown" in command:
        speak("Sure, see you soon sir!")
        exit()

    else:
        speak("I didn't get that.")



# Program starts from here
# 👋 Initial greeting
greet()

# 🌀 Continuous loop with command handling
while True:
    audio, fs = record(duration=5)
    command = transcribe(audio, fs)

    if command.strip():
        print("🗣️ You said:", command)
        handle_command(command)
    else:
        print("🤖 Didn't catch anything.")

