import smtplib

from consumer.config import Config
from consumer.app import celery

conf = Config()


@celery.task
def send_email(email, message):
    sender = conf.MAIL_USERNAME
    password = conf.MAIL_PASSWORD

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, email, message)

        return {'success': True}

    except Exception as ex:
        return {'err': ex}
