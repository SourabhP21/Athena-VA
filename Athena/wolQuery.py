import wolframalpha

def executeWQ(inp):
    client = wolframalpha.Client("")
    res = client.query(inp)
             
    try:
        outr=next(res.results).text
    except StopIteration:
        outr="No Matching Results Found"
    return outr