from main import *
import json
import csv
        
csv_headers = ['Email', 'Name', 'Phone Number']

with open('veterans_information.csv', 'w', encoding = 'utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)
    
email = input("What is your email? ").lower()
name = input("What is your name? ").lower()
phonenum = input("What is your phone number? ").lower()
    
with open('veterans_information.csv', 'a', encoding = 'utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([email, name, phonenum]) 

# ##################################################
