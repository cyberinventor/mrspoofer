from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from emailvalidator import *
from argsvalidator import *
import smtplib
import readline
import argparse
import getpass
import platform
import sys
import os

print("""

\u001b[33m███╗░░░███╗██████╗░  ░██████╗██████╗░░█████╗░░█████╗░███████╗███████╗██████╗░
\u001b[31m████╗░████║██╔══██╗  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
\u001b[34m██╔████╔██║██████╔╝  ╚█████╗░██████╔╝██║░░██║██║░░██║█████╗░░█████╗░░██████╔╝
\u001b[33m██║╚██╔╝██║██╔══██╗  ░╚═══██╗██╔═══╝░██║░░██║██║░░██║██╔══╝░░██╔══╝░░██╔══██╗
\u001b[31m██║░╚═╝░██║██║░░██║  ██████╔╝██║░░░░░╚█████╔╝╚█████╔╝██║░░░░░███████╗██║░░██║
\u001b[33m╚═╝░░░░░╚═╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░░░░░╚════╝░░╚════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝



\u001b[0m""")


parser = argparse.ArgumentParser(description="Spoof a email")
parser.add_argument("-p", "--password", help="your password for email", required=False)
parser.add_argument("-e", "--email", help="your email address", required=False)
parser.add_argument("-m", "--message", help="message to send to target", required=False)
parser.add_argument("-t", "--target", help="targets email address", required=False)
parser.add_argument("-d", "--disguise", help="name or email to make the target see example\nfacebook.com to make it look like the email is from facebook", required=False)
parser.add_argument("-s", "--subject", help="your subject")
args = parser.parse_args()
TrueorFalse = arguments(args).isvalid()
case = args.password or args.email or args.message or args.disguise or args.target or args.subject

if case and TrueorFalse == True:
		email = args.email
		password = args.password
		message = args.message
		target = args.target
		anonymous = args.disguise
		subject = args.subject
		if maileremail().isvalid(str(email)) and maileremail().isvalid(str(target)):
			print("sending email to target\u001b[0m", args.target)
			client = smtplib.SMTP('smtp.gmail.com', 587)
			client.starttls()
			client.login(email, password)
			contents = message
			message = MIMEMultipart()
			message['From'] = anonymous+" <google.com>"
			message['To'] = target
			message['Subject'] = subject
			message.attach(MIMEText(contents, 'plain'))
			message = message.as_string()
			client.sendmail(email, target, message)
			print("\u001b[0msent email to\u001b[31m", args.target+"\u001b[0m")
		else:
			print("\u001b[31memail is not valid")
			sys.exit()
elif case and TrueorFalse == False:
	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")
		print("\u001b[31mWhat the fuck you are supposed to specify the arguments required")
else:
	youremail = input('enter your email: ')
	yourpassword = getpass.getpass(prompt="enter your password: ")
	target = input("enter the email you want to send message to: ")
	message = input("enter message to send to target: ")
	print("example facebook.com Hailey Belle the disguise thing is to make the email look legit.")
	disguise = input("enter the email or username to disguise as: ")
	subject = input("enter subject: ")
	email = youremail
	password = yourpassword
	if maileremail().isvalid(email) and maileremail().isvalid(target):
		print("sending email to target\u001b[0m", target)
		contents = message
		login = smtplib.SMTP('smtp.gmail.com', 587)
		login.starttls()
		login.login(email, password)
		contents = message
		message = MIMEMultipart()
		message['From'] = disguise+" <google.com>"
		message['To'] = target
		message['Subject'] = subject
		message.attach(MIMEText(contents, 'plain'))
		message = message.as_string()
		login.sendmail(email, target, message)
		login.quit()
		print("\u001b[0msent email to\u001b[31m", target+"\u001b[0m")

	else:
		print("\u001b[31memail is not valid")

