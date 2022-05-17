import json

import pika

from producer.config import PARAMS, QUEUE

params = pika.ConnectionParameters(PARAMS)


def send_mail_to_broker(email, message):
    with pika.BlockingConnection(params) as conn:
        channel = conn.channel()
        channel.queue_declare(QUEUE, durable=True)
        channel.basic_publish(exchange='',
                              routing_key=QUEUE,
                              body=json.dumps({"email": email,
                                               "message": message}))
