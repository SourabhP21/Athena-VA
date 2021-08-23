import wikipedia

def executeWiki(inp):
    inp = inp.replace("wikipedia", "")
    results = wikipedia.summary(inp, sentences=2)
    outst="According to Wikipedia: "+results
    return outst