from app import app
from app import start
from flaskext.mysql import MySQL
import pika
import json
import time

'''
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'instadb'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
print(" [*] START CONFIG")

mysql.init_app(app)
'''


def listen_to_location():
    # start.location_queue(cur)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='location_queue', durable=True)
    print(' [*] Waiting for locations.')
    def callback(ch, method, properties, body):
        message = json.loads(body)
        location = ""
        id = ""
        for location in start.locations(message):
            l = location['node']['location']
            if l is not None and l['id'] is not None:
                location = l['name']
                id = l['id']
                print(" [x] Received LOCATION:%s\t\t\t" % location)
                start.new_location(id, location)
        time.sleep(0.2)
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='location_queue', on_message_callback=callback)

    channel.start_consuming()
