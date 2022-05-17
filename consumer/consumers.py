import pika
import json

from consumer.config import Config

conf = Config()
params = pika.ConnectionParameters(conf.PARAMS)


def send_email_handler():
    with pika.BlockingConnection(params) as conn:
        def callback(ch, method, properties, body):
            from tasks import send_email
            data = json.loads(body)

            send_email.apply_async(args=[data.get('email'), data.get('message')])

        channel = conn.channel()
        channel.queue_declare(conf.QUEUE, durable=True)
        channel.basic_consume(queue=conf.QUEUE,
                              on_message_callback=callback,
                              auto_ack=True)
        channel.start_consuming()
        channel.close()
