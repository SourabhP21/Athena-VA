import datetime

def executeTym():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        outst=f"the time is {strTime}"
        return outst