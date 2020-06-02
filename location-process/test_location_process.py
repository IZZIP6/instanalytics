import pika
import time
import json
import mysql.connector
from mysql.connector import Error

def test_location_process():
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='localhost',
                                  database='instadb')
    cursor = cnx.cursor()
    cursor.execute("delete from analytics_location where id=252806986")
    cursor.execute("delete from analytics_location where id=258558523")
    cnx.commit()

    time.sleep(1)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='location_queue', durable=True)

    with open('sara.json') as json_file:
        data = json.load(json_file)

    channel.basic_publish(exchange='',
                  routing_key='location_queue',
                  body=json.dumps(data),
                  properties=pika.BasicProperties(delivery_mode=2,))

    time.sleep(3)
    cursor.execute("select name from analytics_location where id=252806986")
    assert cursor.fetchall()[0][0]=="Trattoria Quaglini"
    cursor.execute("select name from analytics_location where id=258558523")
    assert cursor.fetchall()[0][0] =="Cogne"

    cursor.close()
    cnx.close()
