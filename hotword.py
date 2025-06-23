import pvporcupine
import pyaudio
import struct
from config import HOTWORD
from speech import greet
from utils import play_chime
from core import on_use




# Hotword detection class (Full pack)
class HotwordDetector:
    def __init__(self, keyword=HOTWORD):
        self.porcupine = pvporcupine.create(keywords=[keyword])
        self.audio_interface = pyaudio.PyAudio()
        self.audio_stream = self.audio_interface.open(
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_length
        )

    def listen(self):
        try:
            
            lfh_prompt = False
            while True:
                if not lfh_prompt:
                    print("🎤 Listening for hotword...")
                    lfh_prompt = True
                audio_data = self.audio_stream.read(self.porcupine.frame_length, exception_on_overflow=False)
                audio_data = struct.unpack_from("h" * self.porcupine.frame_length, audio_data)
                result = self.porcupine.process(audio_data)

                if result >= 0:
                    print("✅ Hotword detected!")
                    play_chime(1)
                    on_use()
                    lfh_prompt = False

        except KeyboardInterrupt:
            print("\n🛑 Stopped by user.")
        finally:
            self.cleanup()

    def cleanup(self):
        if self.audio_stream:
            self.audio_stream.close()
        if self.audio_interface:
            self.audio_interface.terminate()
        if self.porcupine:
            self.porcupine.delete()


# Starting point
if __name__ == "__main__":
    greet()
    detector = HotwordDetector(keyword=HOTWORD)
    detector.listen()
