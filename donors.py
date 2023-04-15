from main import *
import json
import csv

# This information will head the page. 
information = "Project Headspace and Timing is a 501(c)3 nonprofit organization that connects veterans to their communities, nature, and themselves."
       
# Code that creates donor sheet and accesses the information to be emailed.   
csv_headers = ['Amount Donated', 'EIN', 'Name']

with open('donors_information.csv', 'w', encoding = 'utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)

list1 = ['1000','584459865','Joe Smith'].lower()
list2 = ['1000','584459654','Jane Doe'].lower()
list3 = ['1000','584659765','Greg Gardner'].lower()
list4 = ['1000','585459645','Nathan Solis'].lower()
list5 = ['1000','583459615','Mateo Chavez'].lower()
lists = [list1, list2, list3, list4, list5]

with open('donors_information.csv', 'a', encoding = 'utf-8', newline='') as file:
    writer = csv.writer(file)
    for i in lists:
        writer.writerow(i)
    
# Emailing Code
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# This gives me the information I am looking for and looking through. 
question = input('What is your name? ').lower()
with open(filename, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    
# This finds if the person on the page is a donor, then retrieves the other data for the email if they are.
for row in reader:
    if question in reader:
        name = question
        # amount = Amount Donated
        # ein = EIN Number
    else:
        print("You are not a donator.")

email = ("samzajc@gmail.com")
message = (f"Here is your reciept. {name}, with the EIN {ein}, has donated {amount}")
msg = MIMEMultipart()
msg['From'] = "nasolis600@gmail.com"
msg['To'] = email
msg['Subject'] = "Reciept for donation."
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
print("Your donation has been received, thank you for your support!")