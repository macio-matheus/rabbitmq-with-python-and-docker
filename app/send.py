import pika
import os

credentials = pika.PlainCredentials(os.environ['USER'], os.environ['PASSWORD'])
connection = pika.BlockingConnection(
    pika.ConnectionParameters('rabbitmq', 5672, os.environ['RABBITMQ_VHOST'], credentials, ))

channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

connection.close()

print("[x] Sent 'Hello World!'")
