import webbrowser

def executeOp(inp):
   outst=""
   if 'open youtube' in inp:
        outst="opening youtube"
        webbrowser.open("youtube.com")

   elif 'open google' in inp:
        outst="opening google"
        webbrowser.open("google.com")

   elif 'open stackoverflow' in inp:
        outst="opening stackoverflow"
        webbrowser.open("stackoverflow.com")
   else:
       outst="unknown open operation"
   return outst    