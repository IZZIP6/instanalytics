import pika
import time
import json
from pymongo import MongoClient
from app.parser import get_profile

'''
    This function open a connection with MongoDB and waits from the queue until an JSON is found. Then it processes it 
    and insert the result into the db
'''


def listen_to_username():
    client = MongoClient('localhost', 27017)
    db = client['instadb']
    print(" [x] Opening connection to MongoDB...")
    collection_profile = db['profiledb']
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')

    '''
        Whenever todo-flask sends the downloaded JSON from the API into the queue, it prepares "final JSON" (context), 
        the one which will be inserted into the db and used to render the HTML page. 
    '''
    def callback(ch, method, properties, body):
        message = json.loads(body)
        print(" [x] Received %r" % "RECEIVED")
        if message.get('logging_page_id') is not None:
            context = get_profile.get_user_data(message)
            collection_profile.insert_one(context)
        time.sleep(1)
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)
    channel.start_consuming()

