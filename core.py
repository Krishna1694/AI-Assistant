import ollama
import re
import datetime
from audio import listen
from speech import speak
from web_commands import web_commands

# Function to query OpenHermes for intelligent responses
def query_ollama_stream(prompt):
    buffer = ""

    try:
        for chunk in ollama.chat(
            model="openhermes",
            messages=[{"role": "user", "content": prompt}],
            stream=True
        ):
            content = chunk.get("message", {}).get("content", "")
            if content:
                print(content, end="", flush=True)
                buffer += content

                # Detect complete sentence/clause
                sentences = re.split(r'(?<=[.?!;])\s+', buffer)
                for sent in sentences[:-1]:
                    if sent.strip():
                        speak(sent.strip())
                buffer = sentences[-1]  # keep last unfinished part

        # Speak any remaining content
        if buffer.strip():
            speak(buffer.strip())

    except KeyboardInterrupt:
        print("\n[Interrupted]")
        if buffer.strip():
            speak(buffer.strip())

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
        speak("Entering sleep mode")
        enter_sleep_mode()
    elif "exit" in command or "stop" in command or "shutdown" in command:
        speak("Shutting down. Goodbye sir!")
        exit()
    else:
        # If no specific command, query OpenHermes for a general response
        query_ollama_stream(command)


# Sleep mode and entering sleep mode (not currently operational, need editing listen)
def sleep_mode():
    speak("Are you still there sir?")
    response = listen()
    if "no" in response:
        enter_sleep_mode()
        return ""
    elif "yes" in response:
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
    return ""

# Main loop for continuous listening
def on_use():
    command = listen()
    if command:
        handle_command(command)

