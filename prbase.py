import pyaudio
import speech_recognition as sr
import pyttsx3
import baseui
import time
import wish
import requests
import datetime
import subprocess
import json
import urllib

from weather import executeWeatherFn
from pquery import executePQueryFn
from openppt import executeOpenPpt
from gsearch import executeSrch
from playM import executePlay
from wiki import executeWiki
from mailserv import executeSendMail
from tym import executeTym
from mycd import executeCd
from jk import executeJk
from flydt import executeFyd
from fact import executeFt
from vaccd import executeVx
from stk import executeStk
from lck import executeLk
from note import executeNtOp
from wolCal import executeWCal
from wolQuery import executeWQ
from day import executeDay
#from nws import executeNs

from OpenWbs import executeOp 
from prdb import inLogDb,inFLogDb,inNLogDb


#text-to-speech initialization
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)


#fn for audio output using tts
def speak(text):
    engine.say(text)
    engine.runAndWait()

#fn for audio input utilizing google speech recognition
def takeInp():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         baseui.var.set("Say something!")
         baseui.window.update()
         audio = r.listen(source)
         r.pause_threshold = 1
         baseui.var.set("Processing...")
         baseui.window.update()
         WIT_AI_KEY = ""
    try:
        baseui.var.set("You said " + r.recognize_google(audio))
        time.sleep(0.4)
        baseui.window.update()
        inp=r.recognize_google(audio)
        
    except sr.UnknownValueError:
        speak("I Could not understand the Audio.")
        inp="None"
    
    except sr.RequestError as e:
         baseui.var.set("Could not request results from Google Speech Recognition service; {0}".format(e))
         baseui.window.update()
         speak("Something went Wrong.")
         inp="None"
    return inp


def begin():

    speak(wish.wishMe())

    baseui.btn2['state'] = 'disabled'
    baseui.btn1.configure(bg = '#F39C12')
    baseui.btn1.config(text="STARTED")
    baseui.var.set("Initializing...")
    baseui.window.update()

    while True:
        inp = takeInp().lower()
        try:
            headers = {
                    'authorization': 'Bearer ' + ''
                    }
            complete_url =  'https://api.wit.ai/message?v=20210602&q='+inp
            response = requests.get(complete_url,headers=headers) 
            obj=response.json()
            x=obj["intents"][0]
            intent=x["name"]
        except:
            pass

        if intent=="query_to_system" or ("how are you" in inp):
            out=executePQueryFn()
            baseui.var.set(out)
            baseui.window.update()
            speak(out)
            id=1
            query=inp
            rv="personal query"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)

        elif intent=="weather_query" or ("weather" in inp):
            out=executeWeatherFn()
            baseui.var.set(out)
            baseui.window.update()
            speak(out)
            id=2
            query=inp
            rv="weather"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)

        elif intent=="open application" or ("powerpoint presentation" in inp or "powerpoint" in inp or "presentation" in inp):
            out=executeOpenPpt()
            baseui.var.set(out)
            baseui.window.update()
            speak(out)
            id=3
            query=inp
            rv="open ppt"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)
                    
        elif intent=="search_google" or ('search' in inp):
            out=executeSrch(inp)
            baseui.var.set(out)
            baseui.window.update()
            speak(out)
            id=4
            query=inp
            rv="gsearch"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)
                    
        elif intent=="play_on_youtube" or ('play' in inp):
            out=executePlay(inp)
            baseui.var.set(out)
            baseui.window.update()
            speak(out)
            id=5
            query=inp
            rv="play music"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)

        elif intent=="search_on_wikipedia" or ('wikipedia' in inp):
            speak("Searching Wikipedia")
            out=executeWiki(inp)
            baseui.var.set(out)
            baseui.window.update()
            speak(out)
            id=6
            query=inp
            rv="wikisearch"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)

        elif intent=="open_google_site" or ('open youtube' in inp or 'open google' in inp or 'open stackoverflow' in inp or 'open stack overflow' in inp):
            out=executeOp(inp)
            baseui.var.set(out)
            baseui.window.update()
            speak(out)
            id=7
            query=inp
            rv="wikisearch"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)

        elif intent=="send_mail" or ('send a mail' in inp):
            speak("What should I say?")
            content = takeInp()
            speak("Please enter recipient email address")
            to = input() 
            out=executeSendMail(to, content)
            baseui.var.set(out)
            baseui.window.update()
            speak(out)
            id=8
            query=inp
            rv="mail"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)

        elif intent=="time" or ('the time' in inp):
            out=executeTym()
            baseui.var.set(out)
            baseui.window.update()
            speak(out)
            id=9
            query=inp
            rv="time"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)

        elif intent=="open_code_directory" or ('open my code' in inp):
            out=executeCd()
            baseui.var.set(out)
            baseui.window.update()
            speak(out)
            id=10
            query=inp
            rv="myCode"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)

        elif intent=="joke" or ('joke' in inp):
            out=executeJk()
            baseui.var.set(out)
            baseui.window.update()
            speak(out)
            id=11
            query=inp
            rv="Joke"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)

        elif intent=="news" or ('news' in inp):
            try:
                jsonObj = urllib.request.urlopen('https://newsapi.org/v2/top-headlines?' 'country=us&' 'apiKey=')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                baseui.var.set('''=== TIMES OF INDIA ==='''+ '\n')
                baseui.window.update()
                 
                for item in data['articles']:                     
                    baseui.var.set(str(i) + '. ' + item['title'] + '\n')
                    baseui.window.update()
                    baseui.var.set(item['description'] + '\n')
                    baseui.window.update()
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1

            except Exception as e:
                baseui.var.set(str(e))
                baseui.window.update()

            id=12
            query=inp
            rv="News"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)

        elif intent=="flight_details" or ("flight details" in inp):
            out=executeFyd()
            baseui.var.set(out)
            baseui.window.update()
            speak(out)
            id=13
            query=inp
            rv="Flight Detail"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)

        elif intent=="fact" or ("fact" in inp):
            out=executeFt()
            baseui.var.set(out)
            baseui.window.update()
            speak(out)
            id=14
            query=inp
            rv="Fact"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)

        elif intent=="vacc_status" or ("vaccine status" in inp or "vaccine detail" in inp):
            out=executeVx()
            baseui.var.set(out)
            baseui.window.update()
            speak(out)
            id=15
            query=inp
            rv="Vaccination Details"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)

        elif intent=="stock_status" or ("stock status" in inp):
            out=executeStk()
            baseui.var.set(out)
            baseui.window.update()
            speak(out)
            id=16
            query=inp
            rv="Stock status"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)

        elif ('lock windows' in inp):
            id=17
            query=inp
            rv="Lock windows"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)
            out=executeLk()

        elif intent=="create_note" or ("note" in inp):
            out=executeNtOp(inp)
            baseui.var.set(out)
            baseui.window.update()
            speak(out)
            id=18
            query=inp
            rv="Notes"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)

        elif intent=="calculate" or ("calculate" in inp):
            out=executeWCal(inp)
            baseui.var.set(out)
            baseui.window.update()
            speak(out)
            id=19
            query=inp
            rv="Calculate"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)

        elif intent=="query" or ("what is" in inp or "who is" in inp or "where is" in inp):
            out=executeWQ(inp)
            baseui.var.set(out)
            baseui.window.update()
            speak(out)
            id=20
            query=inp
            rv="WQuery"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)

        elif intent=="day_q" or ("which day it is" in inp or "what day is it" in inp or "what is the day today" in inp):
            out=executeDay()
            baseui.var.set(out)
            baseui.window.update()
            speak(out)
            id=21
            query=inp
            rv="Day"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)

        elif intent=="end_app_exec" or (inp=='thank you'):
            speak("Have a nice Day")
            baseui.var.set("De-initializing")
            baseui.window.update()
            id=22
            query=inp
            rv="EXit"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inLogDb(id,query,rv,dt)
            exit(0)

        elif 'shutdown system' in inp:
                speak("Are you sure you want me to shutdown the system?")
                baseui.var.set("yes/no")
                baseui.window.update()
                if takeInp()=="yes":
                    id=23
                    query=inp
                    rv="Shutdown"
                    dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    inLogDb(id,query,rv,dt)
                    subprocess.call('shutdown / p /f')
                else:
                    speak("Let me know if you need anything else")

        elif 'restart system' in inp:
                speak("Are you sure you want me to restart the system?")
                baseui.var.set("yes/no")
                baseui.window.update()
                if takeInp()=="yes":
                    id=24
                    query=inp
                    rv="Restart"
                    dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    inLogDb(id,query,rv,dt)
                    subprocess.call('shutdown / p /f')
                else:
                    speak("Let me know if you need anything else") 
        else:
            if inp!="none":
                query=inp
                rv="Unfurnished Query"
                dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                inNLogDb(query,rv,dt)
                speak("I'm not sure, if i can do that")
        
        fl=0

        if inp=="none":
            query=inp
            rv="Query Failure"
            dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            inFLogDb(query,rv,dt)
            speak("Lets try Again")
            continue

        else:
            while True:
                time.sleep(1.2)
                baseui.var.set("do you wish to continue?(Yes/No)")
                speak("do you wish to continue?")
                baseui.window.update()
                time.sleep(1.0)
                baseui.btn1.configure(bg = '#2980B9')
                baseui.btn1['state'] = 'normal'
                baseui.btn2['state'] = 'normal'
                baseui.window.update()
                conf=takeInp()
                try:
                    if conf=="yes":
                        time.sleep(0.5)
                        speak("What shall i do next?")
                        break
                    elif conf=="no":
                        speak("Have a nice Day")
                        baseui.var.set("De-initialized")
                        baseui.btn1.configure(text="RESTART")
                        baseui.window.update()
                        fl=1
                        break
                    else:
                        speak("Please reply with yes or no")
                except:
                    speak("Something Happened. Re-initializing")
                    break

        if fl==1:
            break