from app import app
import pika
import time
import json
from app.parser import get_profile
from app.parser import get_comment
import json
from pymongo import MongoClient


def listen_to_username():
    client = MongoClient('localhost', 27017)
    db = client['instadb']
    # collection_comment = db['commentdb']
    print(" [x] Opening connection to MongoDB...")
    collection_profile = db['profiledb']
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        message = json.loads(body)
        print(" [x] Received %r" % "RECEIVED")
        if message.get('logging_page_id') is not None:
            context = get_profile.get_user_data(message)
            collection_profile.insert_one(context)
     '''
        elif message.get('data', {}).get('user') != None:
          print("ciaoooooooooo111111111\t\t\t\n", message['data']['user'])
        elif message.get('data', {}).get('shortcode_media') != None:
          #print("ciaoooooooooo222222222\t\t\t\n", message.get('data', {}).get('shortcode_media'))
          context_comment = get_comment.get_comment_data(message)
          collection_comment.insert_one(context_comment)
     '''
        time.sleep(1)
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)
    channel.start_consuming()


