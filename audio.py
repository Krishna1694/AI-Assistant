import numpy as np
import sounddevice as sd
import whisper
from config import SAMPLERATE, RECORD_DURATION
from speech import speak
from utils import play_chime

# Initialize Whisper model
whisper_model = whisper.load_model("small")

# Listen for voice input
def listen(timeout=RECORD_DURATION):
    print("🎙️ Listening...")
    try:
        # Record audio
        recording = sd.rec(int(SAMPLERATE * timeout), samplerate=SAMPLERATE, channels=1, dtype='float32')
        sd.wait()

        # Prepare audio
        audio_data = np.squeeze(recording)

        # Transcribe with Whisper
        result = whisper_model.transcribe(audio_data, fp16=False, language="en")
        text = result["text"].strip()
        
        if text:
            print(f"🧑 You: {text}")
            play_chime(2) 
            return text.lower()
        else:
            speak("Didn't catch anything.")
            return ""

    except Exception as e:
        speak(f"Error during listening: {e}")
        return ""