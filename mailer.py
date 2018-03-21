import config

import requests
import smtplib
from email.mime.text import MIMEText

#mailgun_domain = "sandbox71d6b0cfbdc24509a7e8ec91c3fdcb03.mailgun.org"
#mailgun_apikey = ""

def send_payments(paymentRes):
    if paymentRes.count() == 0:
        subject = "No new payments :("
        body = "There are no new payments" + "\n"
    else:
        if paymentRes.count() == 1:
            subject = "New payment"
            body = "There is one new payment:" + "\n"
        else:
            subject = "New payments"
            body = "There are " + str(paymentRes.count())+ " new payments:" + "\n"
    for p in paymentRes.payments:
        body = body + "- " + p.to_string() + "\n"
    body = body + "\n" + "Check included period: " + datetime.datetime.fromtimestamp(self.time_from).__str__() + " - " + datetime.datetime.fromtimestamp(self.time_to).__str__() +  + "\n"

    cfg = config.get()
    to_addr = cfg["to_addr"]
    #send_mail_mailgun_api(to_addr, subject, body, mailgun_domain, mailgun_apikey)
    send_mail_smpt(
        to_addr, cfg["from_addr"], 
        subject, body, 
        cfg["smtp_server"], cfg["smtp_port"], cfg["smtp_user"], cfg["smtp_pass"])
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
    if user != None and len(user) > 0:
        s.login(user, password)
    s.sendmail(sender_addr, [to_addr], msg.as_string())
    s.quit()
