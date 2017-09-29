from gtts import gTTS
import random
import os
import win32com.client as wincl
import playsound

def speek(rand,n,mixer):
    
    speak = wincl.Dispatch("SAPI.SpVoice")                 
    speak.Speak(random.choice(rand))

def wifi():
    REMOTE_SERVER = "www.google.com"
    def is_connected():
        try:
            host = socket.gethostbyname(REMOTE_SERVER)
            s = socket.create_connection((host, 80), 2)
            return True
        except:
            pass
        return False