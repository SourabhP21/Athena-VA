import os
import pyttsx3
import speech_recognition as sr

#text-to-speech initialization
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

#fn for audio output using tts
def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeInp():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         audio = r.listen(source)
         r.pause_threshold = 1
         
    try:
        inp=r.recognize_google(audio)
        
    except sr.UnknownValueError:
        speak("I Could not understand the Audio.")
        inp="None"
    except sr.RequestError as e:
         speak("Something went Wrong.")
         inp="None"
    return inp

def executeNtOp(inp):
    if "write a note" in inp or "take note" in inp:
        speak("What should i write")
        note = takeInp()
        file = open('vanotes.txt', 'w')
        file.write(note)
        file.close()
        outst="Note Taken"
         
    elif "show note" in inp:
        speak("Showing Notes")
        file = open("vanotes.txt", "r")
        outst=file.read(6)
        file.close()

        
    elif "delete note" in inp:
        if os.path.exists("vanotes.txt"):
            os.remove("vanotes.txt")
            outst="your notes are deleted"
        else:
            outst="you dont have any existing notes"
    
    return outst