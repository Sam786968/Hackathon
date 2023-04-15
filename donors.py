from main import *
import json
import csv

# This information will head the page. 
information = ""
       
# Code that creates donor sheet and accesses the information to be emailed.   
csv_headers = ['Amount Donated', 'EIN', 'Name']

with open('donors_information.csv', 'w', encoding = 'utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)




with open('donors_information.csv', 'a', encoding = 'utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([]) 
    
# Emailing Code
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

email = ("samzajc@gmail.com")
message = ("Here is your reciept.")
msg = MIMEMultipart()
msg['From'] = "nasolis600@gmail.com"
msg['To'] = email
msg['Subject'] = "Test email with attachment."
msg.attach(MIMEText(message, 'plain'))
filename = "donors_information.csv"
attachment = open(filename, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("nasolis600@gmail.com", "feieafxmkmijbfzf")
text = msg.as_string()
server.sendmail(msg['From'], msg['To'], text)
server.quit()
print(f"Your donation of ${amount_donated} has been received, thank you for your support!")