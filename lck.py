import ctypes
import pyttsx3

#text-to-speech initialization
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

#fn for audio output using tts
def speak(text):
    engine.say(text)
    engine.runAndWait()

def executeLk():
     speak("locking the device")
     ctypes.windll.user32.LockWorkStation()