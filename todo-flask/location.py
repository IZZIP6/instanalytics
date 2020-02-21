import pika
import time
import json

def post_location(data, i):
    location = data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['location']
    if location is not None:
        return location['name']



def post_location_id(data, i):
    id = data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['location']
    if id is not None:
        return id['id']

def post_number(data):
    return data['graphql']['user']['edge_owner_to_timeline_media']['count']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='location_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    message = json.loads(body)
    npost = post_number(message)
    location = ""
    id = ""
    if npost > 12:
        npost = 12
    for i in range(0, npost):
        location = post_location(message, i)
        id = post_location_id(message, i)
        print(" [x] Received LOCATION:%s\t\t\tID:%s" % (location, id))
    time.sleep(3)
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='location_queue', on_message_callback=callback)

channel.start_consuming()