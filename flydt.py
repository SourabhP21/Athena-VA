import requests
from datetime import date

def executeFyd():
    try:
        today = date.today()
        d4 = today.strftime("%Y-%m")

        srcf="BOM-sky"
        desf="DEL-sky"
        url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/IN/INR/en-US/"+srcf+"/"+desf+"/"+d4

        headers = {
            'x-rapidapi-key': "",
            'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers)
        x=response.json()
        y=x["Quotes"]
        z=y[0]
        ftyp=""
        if(z["Direct"]==True):
            ftyp="direct"
        pr=str(z["MinPrice"])
        p=z["OutboundLeg"]
        l=p["DepartureDate"]
        l=l.split("T")
        dpdt=l[0]

        y=x["Carriers"]
        p=y[0]
        nmc=p["Name"]

        y=x["Places"]
        p=y[0]
        srcpl=p["Name"]
        p=y[1]
        despl=p["Name"]

        y=x["Currencies"]
        p=y[0]
        cur=p["Symbol"]
    
        outst=ftyp+" flight from "+srcpl+" to "+despl+" found for departure on "+dpdt+" by "+nmc+" at "+cur+" "+pr
        return outst
    
    except Exception as e:
        outst=str(e)
        return outst