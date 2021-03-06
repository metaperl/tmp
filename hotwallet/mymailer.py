import logging

logging.basicConfig(level=logging.DEBUG)

def _send_via_gmail(user, password, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = password
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        logging.debug('successfully sent the mail')
    except Exception as e:
        logging.debug('failed to send mail %s', e)


def send_via_email(account, body):
    _send_via_gmail(
        'terrence.brannon@gmail.com',
        'serca972Yancey!',
        'terrence.brannon@gmail.com',
        '({}) ADSactly Grid Trader Error'.format(account),
        body
    )

def send_email(app_instance, subject, body):

    # Import smtplib for the actual sending function
    import smtplib

    # Import the email modules we'll need
    from email.mime.text import MIMEText

    msg = MIMEText(body)

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = subject
    msg['From'] = me = 'admin@adsactly.online'
    msg['To'] = you = app_instance.config.get('admin', 'email')

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP(app_instance.config.get('admin', 'smtpserver'))
    s.sendmail(me, [you], msg.as_string())
    s.quit()
