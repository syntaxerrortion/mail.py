import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddress = 'syntaxerror.exe04@outlook.com'
toaddress = 'araba_ekrem@hotmail.com'
text = 'berk naber knk'
username = 'syntaxerror.exe04@outlook.com'
password = 'ejderekrem123'

msg = MIMEMultipart()
msg['From'] =fromaddress
msg['To'] = toaddress
msg['Subject'] = text
msg.attach(MIMEText(text))
server = smtplib.SMTP('smtp.live.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(fromaddress,toaddress,msg.as_string())
server.quit()
