import webbrowser

def executeSrch(inp):
    inp = inp.replace("search", "")       
    webbrowser.open("google.com/"+inp)
    outst="Searching the web"
    return outst