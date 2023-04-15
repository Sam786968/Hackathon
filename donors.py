import csv
# from flask import Flask, render_template, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# This information will head the page.
##################flask code##################################
# app = Flask(__name__)
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     name = request.form['name']
#     email = request.form['email']
#     message = request.form['message']
#     amountDonated = request.form['amountDonated']
#     ein = request.form['ein']
#     # do something with the data
#     return 'Data received: name={}, email={}, message={}'.format(name, email, message), name, email, message, amountDonated, ein

# name, email , message, amountDonated, ein = submit()
###########################end flask app################################# 

information = "Project Headspace and Timing is a 501(c)3 nonprofit organization that connects veterans to their communities, nature, and themselves."
       
# Code that creates donor sheet and accesses the information to be emailed.   
csv_headers = ['Amount Donated', 'ein', 'Name']

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


# This gives me the information I am looking for and looking through. 
question = input('What is your name? ').lower()

with open('donors_information.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        if question in row:
            amount = row[0] 
            einum = row[1] 
            
            # send email
            sender_email = 'nasolis600@gmail.com'
            sender_password = 'feieafxmkmijbfzf'
            recipient_email = 'samzajc@gmail.com' # email address from the CSV file
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            message = f"Here is your receipt. {question}, with the EIN {einum}, has donated {amount}."
            msg = MIMEMultipart()
            msg['From'] = "nasolis600@gmail.com"
            msg['To'] = recipient_email
            msg['Subject'] = "Receipt for donation."
            msg.attach(MIMEText(message, 'plain'))
            
            filename = "donors_information.csv"
            attachment = open(filename, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(part)
            
            email = ("samzajc@gmail.com")
            message = (f"Here is your reciept. {question}, with the EIN {einum}, has donated {amount}. Thank you so much for your donation, have a great day.")
            msg['From'] = "nasolis600@gmail.com"
            msg['To'] = email
            msg['Subject'] = "Reciept for donation."
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("nasolis600@gmail.com", "feieafxmkmijbfzf")
            text = msg.as_string()
            server.sendmail(msg['From'], msg['To'], text)
            server.quit()
        
            # exit the loop after finding the matching row
            print("Your donation has been received, thank you for your support!")
            break
        else:
            None
            break
            


# To Donor
# email = ("samzajc@gmail.com")
# message = (f"Here is your reciept. {question}, with the EIN {einum}, has donated {amount}. Thank you so much for your donation, have a great day.")
# msg['From'] = "nasolis600@gmail.com"
# msg['To'] = email
# msg['Subject'] = "Reciept for donation."
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login("nasolis600@gmail.com", "feieafxmkmijbfzf")
# text = msg.as_string()
# server.sendmail(msg['From'], msg['To'], text)
# server.quit()

