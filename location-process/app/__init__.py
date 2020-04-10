from flask import Flask
import threading

app = Flask(__name__)

from app import route

t = threading.Thread(target=route.listen_to_location)
t.daemon = True
t.start()