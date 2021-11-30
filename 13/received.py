"""
Overview of Received Emails
"""
from imaplib import IMAP4_SSL
from getpass import getpass
from email import message_from_string


def main():
    """
    main function
    """
    imap = IMAP4_SSL("imap.outlook.com")
    user = input("Enter your email: ")
    password = getpass("Enter your password: ")
    imap.login(user, password)
    print(imap.list())
    print(imap.select("inbox"))
    typ, data = imap.search(None, 'SUBJECT "this is a test email for python"')
    print(typ)
    print(data)
    _, email_data = imap.fetch(data[0], "(RFC822)")
    raw_email = email_data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = message_from_string(raw_email_string)
    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            print(body)


if __name__ == "__main__":
    main()
