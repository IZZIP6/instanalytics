from flask import Flask
import threading

app = Flask(__name__)

from app import route

'''
    Each time the app is run, a thread is started to connect to RabbitMQ queue
'''
t = threading.Thread(target=route.listen_to_username)
t.daemon = True
t.start()