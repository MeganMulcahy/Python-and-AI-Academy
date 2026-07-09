import os
import smtplib

# Generate the App Password at myaccount.google.com/apppasswords (requires 2-Step Verification enabled on the account)

my_email = "megan.mulcahy03@gmail.com"
password = os.environ["EMAIL_APP_PASSWORD"]  # Gmail App Password, not your account password

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user = my_email, password = password)

connection.sendmail(from_addr = my_email,
    to_addrs = "recipientemail@gmail.com", msg = "subject: Test Email\n\nHello World"
    )
connection.close()