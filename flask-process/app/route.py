from app import app
import pika
import time
import json
from app.parser import get_profile
from app.parser import get_comment
import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['instadb']
collection_profile = db['profiledb']
collection_comment = db['commentdb']

# if pymongo < 3.0, use insert()
#collection_currency.insert(file_data)
# if pymongo >= 3.0 use insert_one() for inserting one document
#collection_currency.insert_one(file_data)
# if pymongo >= 3.0 use insert_many() for inserting many documents
#collection_currency.insert_many(file_data)

client.close()

connection = pika.BlockingConnection(
pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
     message = json.loads(body)
     print(" [x] Received %r" % "RECEIVED")
     #print(message)
     if message.get('logging_page_id') != None:
          #print(message['logging_page_id'])
          context = get_profile.get_user_data(message)
          collection_profile.insert_one(context)
     elif message.get('data', {}).get('user') != None:
          print("ciaoooooooooo111111111\t\t\t\n", message['data']['user'])
     elif message.get('data', {}).get('shortcode_media') != None:
          #print("ciaoooooooooo222222222\t\t\t\n", message.get('data', {}).get('shortcode_media'))
          context_comment = get_comment.get_comment_data(message)
          collection_comment.insert_one(context_comment)
     time.sleep(3)
     print(" [x] Done")
     #to get last record of profile inserted in mongo
     data = list(collection_profile.find({}).sort([("date_time", -1)]).limit(1))
     print(data)
     ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()
client.close()