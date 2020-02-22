from app import start
import pika
import time

'''
    Open a connection to localhost using pika client and wait for a message from the username_queue, that returns 
    the username to be searched
'''


def listen_to_username():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='username_queue', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')

    '''
        Each time an username is found, callback function start the procedure to sends requests, passing the username 
        as parameter (contained in body)
    '''
    def callback(ch, method, properties, body):
        print(" [x] Received %s" % body)
        time.sleep(1)
        start.request_to_username(body)
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='username_queue', on_message_callback=callback)
    channel.start_consuming()

