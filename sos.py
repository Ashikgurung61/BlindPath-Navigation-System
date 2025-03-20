import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "ashikgurunge@gmail.com"
    msg['from'] = user
    password = "yuzj lqqa ffwj isqn"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

def main():
    subject = "Emergency Attention Required"
    body = "My current Location is __________, and I'm in danger"
    recepient = "ashikgrg61@gmail.com"
    email_alert(subject, body, recepient)