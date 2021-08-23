import json
import urllib

#text-to-speech initialization
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)


#fn for audio output using tts
def speak(text):
    engine.say(text)
    engine.runAndWait()

def executeNs():
    try:
        jsonObj = urllib.request.urlopen('https://newsapi.org/v2/top-headlines?' 'country=us&' 'apiKey=')
        data = json.load(jsonObj)
        i = 1
                 
        speak('here are some top news from the times of india')
        var.set('''=== TIMES OF INDIA ==='''+ '\n')
        window.update()
                 
        for item in data['articles']:                     
            var.set(str(i) + '. ' + item['title'] + '\n')
            window.update()
            var.set(item['description'] + '\n')
            window.update()
            speak(str(i) + '. ' + item['title'] + '\n')
            i += 1

    except Exception as e:
        var.set(str(e))
        window.update()