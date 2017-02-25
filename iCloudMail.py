#!/usr/bin/python
from urllib2 import urlopen
import smtplib

accountName = 'from@domain.com' #Your icloud email address
password='yourpassword' #password for icloud account

receivers = ['toAddress@domain.com'] #Recipient list

server='smtp.me.com' #Default for iCloud, For other provider change to your sender mailing server

my_ip = urlopen('http://ip.42.pl/raw').read()

s=smtplib.SMTP(server, 587)
s.ehlo()
s.starttls()
s.login(accountName, password)

message = """From: %s
To: %s
Subject: IP Address %s

Your Public address is %s: """%(accountName,",".join(receivers),str(my_ip),str(my_ip))

s.sendmail(accountName, receivers, message)      #Sending mail   


