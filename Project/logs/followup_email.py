from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib, ssl
import os,string,sys
sys.path.append(os.path.normpath(os.getcwd()))
from config import location
#location = "E:/recomendar/Project/"
SERVER = "smtp.gmail.com"
port= 587
FROM = "guganvikash@gmail.com"
TO = "gugankaghu22@gmail.com"
password="Vikash@Gugan@123"
SUBJECT = "Follow up questions email"
TEXT = """Hello,

Here are the various questions users asked me today which I have no idea about. Could you help me learn these topics?

Regards,
Sam
"""

msg = MIMEMultipart()
 
msg['From'] = ", ".join(FROM)
msg['To'] = ", ".join(TO)
msg['Subject'] = SUBJECT
 
body = TEXT

msg.attach(MIMEText(body, 'plain'))

filename = 'log_file.TXT'
attachment = open(location + 'log_file.TXT', "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

message = msg.as_string()
context = ssl.create_default_context()
server = smtplib.SMTP(SERVER,port)
server.starttls(context=context)
server.login(FROM, password)
server.sendmail(FROM, TO, message)
server.quit()
