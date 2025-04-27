import requests
import pyttsx3
import datetime
import webbrowser
import whisper
import numpy as np
import sounddevice as sd

# Initialize speech engines
engine = pyttsx3.init()
whisper_model = whisper.load_model("small")  

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
    speak("How can I help you?")

# Listen for voice input
def listen(timeout=5):
    print("🎙️ Listening...")
    try:
        # Record audio
        samplerate = 16000  # 16 kHz is ideal
        duration = timeout
        recording = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='float32')
        sd.wait()

        # Prepare audio
        audio_data = np.squeeze(recording)

        # Transcribe with Whisper
        result = whisper_model.transcribe(audio_data, fp16=False, language="en")
        text = result["text"].strip()
        
        if text:
            print(f"🧑 You: {text}")
            return text.lower()
        else:
            speak("Didn't catch anything.")
            return ""

    except Exception as e:
        speak(f"Error during listening: {e}")
        return ""

# Sleep mode and entering sleep mode
def sleep_mode():
    speak("Shall I enter sleep mode sir?")
    response = listen()
    if "yes" in response:
        enter_sleep_mode()
        return ""
    elif "no" in response:
        speak("Okay, I'm still here sir.")
        return listen()
    else:
        speak("Seems you are away sir.")
        speak("Entering sleep mode.")
        enter_sleep_mode()
        return ""

def enter_sleep_mode():
    input("Press enter to wake me up sir!")
    speak("I'm up sir")
    on_use()

# Handle websites like Google and YouTube
def web_commands(site):
    speak(f"What would you like to do with {site.capitalize()}?")
    response = listen()

    if response.startswith("search for"):
        search = response.replace("search for", "", 1).strip()
        if search:
            encoded_query = search.replace(" ", "+")
            if site == "google":
                webbrowser.open(f"https://www.google.com/search?q={encoded_query}")
                speak(f"Searching Google for {search}")
            elif site == "youtube":
                webbrowser.open(f"https://www.youtube.com/results?search_query={encoded_query}")
                speak(f"Searching YouTube for {search}")
        else:
            speak("I didn't catch what to search. Opening homepage instead.")
            open_homepage(site)
    else:
        open_homepage(site)

# Open default homepage of websites
def open_homepage(site):
    if site == "google":
        webbrowser.open("https://www.google.com")
        speak("Opening Google homepage.")
    elif site == "youtube":
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube homepage.")

# Function to query OpenHermes for intelligent responses
def query_openhermes(prompt):
    
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            "model": "openhermes",
            "prompt": prompt,
            "stream": False
        }
    )
    
    response_text = response.json().get("response", "")
    
    return response_text

# Handle basic commands like time, date, and shutdown
def handle_command(command):
    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")
    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif "open google" in command:
        web_commands("google")
    elif "open youtube" in command:
        web_commands("youtube")
    elif "sleep" in command:
        enter_sleep_mode()
    elif "exit" in command or "stop" in command or "shutdown" in command:
        speak("Shutting down. Goodbye sir!")
        exit()
    else:
        # If no specific command, query OpenHermes for a general response
        response = query_openhermes(command)
        speak(response)

# Main loop for continuous listening
def on_use():
    while True:
        command = listen()
        if command:
            handle_command(command)

# Starting point
if __name__ == "__main__":
    greet()
    on_use()
