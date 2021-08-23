import os
import webbrowser

def executePlay(inp):
    if inp=="play music":
        outst="Searching directory for music"
        music_dir = ""
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
    else:
        outst="Playing on Youtube"
        inp = inp.replace("play", "")  
        webbrowser.open("youtube.com/"+inp)
    return outst