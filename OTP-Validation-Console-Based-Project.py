import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
n = ["tejaswiemani1010@gmail.com","paramjyothipasupuleti123@gmail.com","pujaparchuri@gmail.com","rokkalasailaja01@gmail.com"]
for i in n:

    otp = random.randint(1111,9999)
    body = f"OTP for Verification is {otp}"

    msg = MIMEMultipart()
    msg["From"] = "tejaswiemani1010@gmail.com"
    msg["To"] = i
    msg["Subject"] = "OTP For Validation"  
    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP("Smtp.gmail.com",587)
    server.starttls()
    server.login("tejaswiemani1010@gmail.com","nxto koxg awuw rujf")
    server.send_message(msg)
    server.quit()

    cotp = int(input("Enter OTP Recieved: "))
    if otp == cotp:
        print("OTP Verification Success")
    else:
        print("Invalid OTP")



