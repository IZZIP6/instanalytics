import requests
import json
from .. import setup
from .request import make_request
import time

session = requests.Session()
session.headers.update(setup.header)


def user_request(url):
    try:
        message = make_request(session, url)
        return message
    except json.decoder.JSONDecodeError as e:
        print(' [x] Wrong username -- see requst_adapter.py\n')
        print(e)


def user_media_request(url):
    message = make_request(session, url)
    time.sleep(1)
    return message

def comment_media_request(url):
    message = make_request(session, url)
    time.sleep(1)
    return message


def post_request(url):
    make_request(session, url)







