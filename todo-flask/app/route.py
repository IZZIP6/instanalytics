from app import app
from app import start
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='username_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %s" % body)
    time.sleep(1)
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()

@app.route("/s/<username>")                   # at the end point /
def hello(username):                      # call method hello
    start.request_to_username(username)
    return "Hello World!"         # which returns "hello world"

@app.errorhandler(404)
def page_not_found(error):
    return "niente di niente", 404