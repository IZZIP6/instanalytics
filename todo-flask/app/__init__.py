from flask import Flask
import threading

app = Flask(__name__)

from app import route

t = threading.Thread(target=route.listen_to_username)
t.daemon = True
t.start()