import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

body = '''
Simple text
'''

sender = 'aaaaaaaaaaaaaaaa@gmail.com'
password = 'AAAAAAAAAAAAAA'
receiver = receiver_mail
 
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = "Ur title"
 
message.attach(MIMEText(body, 'plain'))
 
pdfname = 'ur_pdf_file.pdf'
 
binary_pdf = open(pdfname, 'rb')
 
payload = MIMEBase('application', 'octate-stream', Name=pdfname)
payload.set_payload((binary_pdf).read())
 
encoders.encode_base64(payload)
 
payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
message.attach(payload)
 
session = smtplib.SMTP('smtp.gmail.com', 587)
 
session.starttls()
 
session.login(sender, password)
 
text = message.as_string()
session.sendmail(sender, receiver, text)
session.quit()
print('Mail Sent')

