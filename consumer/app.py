from flask import Flask
from celery import Celery

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'], include=['tasks'])
celery.conf.update(app.config)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
