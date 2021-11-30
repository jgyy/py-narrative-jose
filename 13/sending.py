"""
Overview of Sending Emails
"""
from smtplib import SMTP
from getpass import getpass


def main():
    """
    main function
    """
    smtp_object = SMTP("smtp-mail.outlook.com", 587)
    smtp_object.ehlo()
    smtp_object.starttls()
    email = input("Enter your email: ")
    password = getpass("Enter your password: ")
    smtp_object.login(email,password)
    from_address = input("Enter your email: ")
    to_address = input("Enter the email of the recipient: ")
    subject = input("Enter the subject line: ")
    message = input("Type out the message you want to send: ")
    msg = "Subject: " + subject + '\n' + message
    smtp_object.sendmail(from_address,to_address,msg)
    smtp_object.quit()


if __name__ == "__main__":
    main()
