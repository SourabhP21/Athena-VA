import requests

def executeFt():
    try:
        url = "https://numbersapi.p.rapidapi.com/random/trivia"

        querystring = {"json":"true","fragment":"true"}

        headers = {
            'x-rapidapi-key': "",
            'x-rapidapi-host': "numbersapi.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        x=response.json()
        ftxt=x["text"]
        ftn=x["number"]
        ftn=str(ftn)
        outst=ftxt+" is "+ftn
        return outst
    
    except Exception as e:
        outst=str(e)
        return outst