import requests
from datetime import date

def executeStk():
    try:
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"
        stck="INFY"
        querystring = {"symbol":stck,"region":"IN"}

        headers = {
            'x-rapidapi-key': "",
            'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        x=response.json()
        y=x["price"]
        pr_src=y["quoteSourceName"]
        stnm=y["shortName"]+"("+stck+")"
        z=y["regularMarketOpen"]
        pr=z["raw"]
        y=x["pageViews"]
        trend=y["shortTermTrend"]
        if(trend=="UP"):
            trend="upwards"
        url = "https://currency-exchange.p.rapidapi.com/exchange"

        querystring = {"to":"INR","from":"USD","q":"1.0"}

        headers = {
            'x-rapidapi-key': "",
            'x-rapidapi-host': "currency-exchange.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        cnr=response.json()

        pr=pr*cnr
        pr=round(pr,2)

        outst="According to "+pr_src+".\n"+stnm+" is on short term "+trend+" trend and Opened at ₹"+str(pr)
        return outst
    
    except Exception as e:
        outst=str(e)
        return outst