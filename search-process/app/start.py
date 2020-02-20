import pika

def username_queue(username):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='username_queue', durable=True)
    channel.basic_publish(exchange='',
                              routing_key='username_queue',
                              body=username,
                              properties=pika.BasicProperties(delivery_mode=2,))
    print(" [x] Send %s" % username)
    connection.close()
