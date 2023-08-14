from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "Max"
message["to"] = "adiomi90@gmail.com"
message["subject"] = "This is a test"

message.attach(MIMEText("Body"))
with smtplib.SMTP(host="smtp.outlook.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("adiomi90@outlook.com","5408kila")
    smtp.send_message(message)
    print("sent")

