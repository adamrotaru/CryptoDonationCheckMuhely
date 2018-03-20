import requests

mailgun_domain = "sandbox71d6b0cfbdc24509a7e8ec91c3fdcb03.mailgun.org"
mailgun_apikey = "key-"   # a_r
to_addr = "adam_rotaru@yahoo.com"

def send_payments(payments):
    subject = str(len(payments))  + " new payments"
    body = "There are " + str(len(payments))  + " new payments" + "\n"
    for p in payments:
        body = body + str(p.amount) + "\n"
    send_mailgun_mail(to_addr, mailgun_domain, mailgun_apikey, subject, body)

def send_mailgun_mail(to_addr, mailgun_domain, mailgun_apikey, subject, body):
    return requests.post(
        "https://api.mailgun.net/v3/" + mailgun_domain + "/messages",
        auth = ("api", mailgun_apikey),
        data = {
            "from": "Mailgun Sandbox <postmaster@sandbox71d6b0cfbdc24509a7e8ec91c3fdcb03.mailgun.org>",
            "to": to_addr,
            "subject": subject,
            "text": body
        })

def send_test_message():
    send_mailgun_mail(to_addr, mailgun_domain, mailgun_apikey, 
        "Hello Mailer", "Congratulations Mailer, you just sent an email with Mailgun!  You are truly awesome!")

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox71d6b0cfbdc24509a7e8ec91c3fdcb03.mailgun.org/messages",
        auth=("api", mailgun_apikey),
        data={"from": "Mailgun Sandbox <postmaster@sandbox71d6b0cfbdc24509a7e8ec91c3fdcb03.mailgun.org>",
              "to": to_addr,
              "subject": "Hello Mailer",
              "text": "Congratulations Mailer, you just sent an email with Mailgun!  You are truly awesome!"})
