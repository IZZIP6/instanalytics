import pika
import time
import json
from flaskext.mysql import MySQL
from app import app
import click
from pymysql import cursors

'''
    da commentare :)
'''
mysql = MySQL(cursorclass=cursors.DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'instadb'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
print(" [*] START CONFIG")

mysql.init_app(app)

flag = True


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='location_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def locations(data):
    location = data['graphql']['user']['edge_owner_to_timeline_media']['edges']
    if location is not None:
        return location

def new_location(cur, id, location):
    location = location.replace("'", " ")
    select_query = "SELECT id FROM analytics_location"
    cur.execute(select_query)
    results = cur.fetchall()
    if id in str(results):
        if flag:
            click.secho(
                " [*] %s already in" % location,
                fg="green",
            )
    else:
        insert_query = "INSERT INTO analytics_location(id, name) VALUES ('%s', '%s')" % (id, location)
        cur.execute(insert_query)
        if flag:
            click.secho(
                " [*] %s inserted" % location,
                fg="green",
            )

def location_queue(cur):
    def callback(ch, method, properties, body):
        message = json.loads(body)
        location = ""
        id = ""
        for location in locations(message):
            l = location['node']['location']
            if l is not None and l['id'] is not None:
                location = l['name']
                id = l['id']
                print(" [x] Received LOCATION:%s\t\t\tID:%s" % (location, id))
                new_location(cur, id, location)
        time.sleep(0.2)
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='location_queue', on_message_callback=callback)

    channel.start_consuming()