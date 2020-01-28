import pika
import os


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


credentials = pika.PlainCredentials(os.environ['USER'], os.environ['PASSWORD'])
connection = pika.BlockingConnection(
    pika.ConnectionParameters('rabbitmq', 5672, os.environ['RABBITMQ_VHOST'], credentials, ))

channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
