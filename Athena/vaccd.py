import requests
from datetime import date

def executeVx():
    try:
        headers = {
            'User-Agent': 'Chrome/70.0.3538.77'
            }

        today = date.today()
        d4 = today.strftime("%d-%m-%Y")
        pc="400000"
        complete_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="+pc+"&date="+d4
        response = requests.get(complete_url,headers=headers) 
        x=response.json()
        y=x["centers"]
        z=y[0]
        center=z["name"]
        w=z["sessions"]
        u=w[0]
        vacc=u["vaccine"]
        av=str(u["available_capacity"])

        outst=" for pincode "+pc+". "+av+". "+vacc+" vaccines available at "+center
        return outst
    
    except Exception as e:
        outst=str(e)
        return outst