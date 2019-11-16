import requests
import json
from server import setup
import time
import os

session = requests.Session()
session.headers.update(setup.header)

def user_request(url, path):
    if not os.path.exists('./server/profiles/'+path.split('/')[3].split('.')[0]):
        os.mkdir('./server/profiles/'+path.split('/')[3].split('.')[0])
    try:
        make_request(url, path)
    except json.decoder.JSONDecodeError as e:
        print('Wrong username')
        directory_path = "../profiles/"+path.split('/')[3].split('.')[0]
        os.rmdir(directory_path)
        quit()


def media_request(url, path):
    if not os.path.exists('./server/profiles/'+path.split('/')[3].split('.')[0]+'/post'):
        os.mkdir('./server/profiles/'+path.split('/')[3].split('.')[0]+'/post')
    make_request(url, path)
    time.sleep(1)


def make_request(url, path):
    r = session.get(url)
    jpost = r.json()
    with open(path, 'w') as fp:
        json.dump(jpost, fp)
    return jpost

