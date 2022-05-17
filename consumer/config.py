import os

from dotenv import load_dotenv

load_dotenv('.env')


class Config:
    SECRET_KEY = os.environ['SECRET_KEY']
    CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
    CELERY_RESULT_BACKEND = os.environ['CELERY_RESULT_BACKEND']
    MAIL_SERVER = os.environ['MAIL_SERVER']
    MAIL_PORT = os.environ['MAIL_PORT']
    MAIL_USE_TLS = os.environ['MAIL_USE_TLS']
    MAIL_USE_SSL = os.environ['MAIL_USE_SSL']
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
    MAIL_USERNAME = os.environ['MAIL_USERNAME']
    QUEUE = os.environ['QUEUE']
    PARAMS = os.environ['PARAMS']
