import smtplib

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login('', '')
    server.sendmail('', to, content)
    server.close()

def executeSendMail(to, content):
    recipient=to
    msg=content
    try:
        sendEmail(recipient, msg)
        outst="Email has been sent !"
    except Exception as e:
        outst="I am not able to send this email "+e
    return outst