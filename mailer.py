import requests
import smtplib
from email.mime.text import MIMEText

mailgun_domain = "sandbox71d6b0cfbdc24509a7e8ec91c3fdcb03.mailgun.org"
mailgun_apikey = ""
to_addr = "adam_rotaru@yahoo.com"
from_addr = "DonationCheck@blokklancmuhely.club"
smtp_server = "smtp.mailgun.org"
smtp_port = 587
smtp_user = "postmaster@sandbox71d6b0cfbdc24509a7e8ec91c3fdcb03.mailgun.org"
smtp_pass = ""

def send_payments(paymentRes):
    subject = str(paymentRes.count())  + " new payments"
    body = "There are " + str(paymentRes.count())  + " new payments" + "\n"
    for p in paymentRes.payments:
        body = body + "- " + p.to_string() + "\n"
    #send_mail_mailgun_api(to_addr, subject, body, mailgun_domain, mailgun_apikey)
    send_mail_smpt(to_addr, from_addr, subject, body, smtp_server, smtp_port, smtp_user, smtp_pass)
    print("mail sent to", to_addr, "payments:", paymentRes.count())

def send_mail_mailgun_api(to_addr, subject, body, mailgun_domain, mailgun_apikey):
    return requests.post(
        "https://api.mailgun.net/v3/" + mailgun_domain + "/messages",
        auth = ("api", mailgun_apikey),
        data = {
            "from": "Mailgun Sandbox <postmaster@sandbox71d6b0cfbdc24509a7e8ec91c3fdcb03.mailgun.org>",
            "to": to_addr,
            "subject": subject,
            "text": body
        })

def send_mail_smpt(to_addr, sender_addr, subject, body, server, port, user, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_addr
    msg['To'] = to_addr

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP(server, port)
    s.login(user, password)
    s.sendmail(sender_addr, [to_addr], msg.as_string())
    s.quit()
