import wolframalpha

def executeWCal(inp):
    app_id = ""
    client = wolframalpha.Client(app_id)
    indx = inp.lower().split().index('calculate')
    inp = inp.split()[indx + 1:]
    res = client.query(' '.join(inp))
    answer = next(res.results).text
    return answer