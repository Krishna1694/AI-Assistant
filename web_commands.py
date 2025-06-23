import webbrowser
from speech import speak
from config import GOOGLE_URL, YOUTUBE_URL
from audio import listen

# Handle websites like Google and YouTube
def web_commands(site):
    speak(f"What would you like to do with {site.capitalize()}?")
    response = listen()

    if response.startswith("search for"):
        search = response.replace("search for", "", 1).strip()
        if search:
            encoded_query = search.replace(" ", "+")
            if site == "google":
                webbrowser.open(f"{GOOGLE_URL}/search?q={encoded_query}")
                speak(f"Searching Google for {search}")
            elif site == "youtube":
                webbrowser.open(f"{YOUTUBE_URL}/results?search_query={encoded_query}")
                speak(f"Searching YouTube for {search}")
        else:
            speak("I didn't catch what to search. Opening homepage instead.")
            open_homepage(site)
    else:
        open_homepage(site)

# Open default homepage of websites
def open_homepage(site):
    if site == "google":
        webbrowser.open(GOOGLE_URL)
        speak("Opening Google homepage.")
    elif site == "youtube":
        webbrowser.open(YOUTUBE_URL)
        speak("Opening YouTube homepage.")
