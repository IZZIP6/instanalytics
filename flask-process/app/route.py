import pika
import time
import json
from pymongo import MongoClient
from app.parser import get_profile
from app.parser import get_comment
from app.parser import get_post
from app.parser import profiling

'''
    This function open a connection with MongoDB and waits from the queue until an JSON is found. Then it processes it 
    and insert the result into the db
'''


def listen_to_username():
    client = MongoClient('localhost', 27017)
    db = client['instadb']
    print(" [x] Opening connection to MongoDB...")
    collection_profile = db['profiledb']
    collection_comment = db['commentdb']
    collection_post = db['postdb']
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
            'reset post_profile lists '
            profiling.reset_profile_post()
            profiling.reset_profile_post_1()
        elif message.get('data', {}).get('user') != None:
            print(" [*] START POST")
            context_post = get_post.get_post_data(message)
            post_has_next_page = profiling.post_get_post_page_info_has_next_page(message)
            if not post_has_next_page:
               collection_post.insert_one(context_post)
               'reset post lists '
               profiling.reset_post()
        elif message.get('data', {}).get('shortcode_media') != None:
            print(" [*] START COMMENT")
            context_comment = get_comment.get_comment_data(message)
            comment_has_next_page = profiling.get_comment_has_next_page(message)
            if not comment_has_next_page:
                collection_comment.insert_one(context_comment)
                'reset comment lists '
                profiling.reset_comment()

        time.sleep(1)
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)
    channel.start_consuming()

