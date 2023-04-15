from main import *
import json
import csv

# This information will head the page. 
information = "Volutneers are able to help"
       
# Code that creates volunteer sheets.   
csv_headers = ['Email', 'Name', 'Phone Number']

with open('volunteers_information.csv', 'w', encoding = 'utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)
    
email = input("What is your email? ").lower()
name = input("What is your name? ").lower()
phonenum = input("What is your phone number? ").lower()
    
with open('volunteers_information.csv', 'a', encoding = 'utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([email, name, phonenum]) 

# Emailing Code
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

email = ("samzajc@gmail.com")
message = (f"Here is the donor receipt for {name}.")
msg = MIMEMultipart()
msg['From'] = "nasolis600@gmail.com"
msg['To'] = email
msg['Subject'] = "Test email with attachment."
msg.attach(MIMEText(message, 'plain'))
filename = "volunteers_information.csv"
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
print("Information recorded. Thank you for signing up!")