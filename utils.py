import pygame
import time
from config import CHIME_PATH_1, CHIME_PATH_2

pygame.mixer.init()

# Play chime sound
def play_chime(type):
    try:
        # Load and play the sound
        if type == 1:
            pygame.mixer.music.load(CHIME_PATH_1)
            pygame.mixer.music.play()
            time.sleep(0.5)
        elif type == 2:
            pygame.mixer.music.load(CHIME_PATH_2)
            pygame.mixer.music.play()
            time.sleep(0.5)
        else:
            print("Invalid chimes option")
    except Exception as e:
        print(f"⚠️ Error playing chime: {e}")
