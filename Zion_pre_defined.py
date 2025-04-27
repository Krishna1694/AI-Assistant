import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech engine
engine = pyttsx3.init()

# Greet the user based on the current time.
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")
    speak("How can I help you?")

# Handle websites
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

# Handle default website home pages
def open_homepage(site):
    if site == "google":
        webbrowser.open("https://www.google.com")
        speak("Opening Google homepage.")
    elif site == "youtube":
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube homepage.")

# Sleep mode permission 
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
    
# Enters sleep mode
def enter_sleep_mode():
    input("Press enter to wake me up sir!")
    speak("I'm up sir")
    on_use()

# Function to speak
def speak(text):
    print(f"🗣️ Zion: {text}")
    engine.say(text)
    engine.runAndWait()

# Function to listen
def listen(timeout=10):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=timeout)
        except sr.WaitTimeoutError:
            return sleep_mode()
        except Exception as e:
            speak("Something went wrong while listening.")
            print(f"Error: {e}")
            return ""

    try:
        command = recognizer.recognize_google(audio)
        print(f"🧑 You: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

# Handle commands
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
        speak("I didn't understand that command.")

# Starting point
def on_use():
    while True:
        command = listen()
        if command:
            handle_command(command)

# Main loop
if __name__ == "__main__":
    greet()
    on_use()
