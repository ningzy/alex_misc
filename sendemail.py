import smtplib
import getpass

FROM = 'zning'
TO = 'airportico@gmail.com'
SUBJECT = 'test'
TEXT = 'testtttt'

message = """ from: %s\nto: %s\nsubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    user = input("User name: ")
    pwd = getpass.getpass('Password: ')
    server.login(user, pwd)
    server.sendmail(FROM, TO, message)
    server.close()
    print("email sent...")
except:
    print("failed...")