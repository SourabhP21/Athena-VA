import datetime


def wishMe():
    outstr=""
    hour=int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        outstr+="Good Morning!"
    elif hour>=12 and hour<17:
        outstr+="Good Afternoon!"
    elif hour>=17 and hour<20:
        outstr+="Good Evening!"
    else:
        outstr+="Good Evening!"
    
    outstr+=" How may I assist you?"
    return outstr