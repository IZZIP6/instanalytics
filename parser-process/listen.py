import pika
import time
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='location_queue', durable=True)

def callback(ch, method, properties, body):
    time.sleep(0.2)
    msg= body
    print(msg)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='location_queue', on_message_callback=callback)
channel.start_consuming()
