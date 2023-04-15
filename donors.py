import json
import csv

# This information will head the page. 
information = "Project Headspace and Timing is a 501(c)3 nonprofit organization that connects veterans to their communities, nature, and themselves."
       
# Code that creates donor sheet and accesses the information to be emailed.   
csv_headers = ['Amount Donated', 'EIN', 'Name']

with open('donors_information.csv', 'w', encoding = 'utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)

list1 = ['1000','584459865','joe smith']
list2 = ['1500','584459654','jane doe']
list3 = ['2000','584659765','greg gardner']
list4 = ['3000','585459645','nathan solis']
list5 = ['5000','583459615','mateo chavez']
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
with open('donors_information.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    
# This finds if the person on the page is a donor, then retrieves the other data for the email if they are.
    for row in reader:
        if question in row:
            # print(question)
            amount = row[0] 
            # print(f'amount is {amount}')
            einum = row[1] 
            # print(f'amount is {einum}')
        else:
            None

email = ("samzajc@gmail.com")
message = (f"Here is your reciept. {question}, with the EIN {einum}, has donated {amount}")
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

email = ("samzajc@gmail.com")
message = (f"Here is your reciept. {question}, with the EIN {einum}, has donated {amount}")
msg['From'] = "nasolis600@gmail.com"
msg['To'] = email
msg['Subject'] = "Reciept for donation."
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("nasolis600@gmail.com", "feieafxmkmijbfzf")
text = msg.as_string()
server.sendmail(msg['From'], msg['To'], text)
server.quit()
print("Your donation has been received, thank you for your support!")
