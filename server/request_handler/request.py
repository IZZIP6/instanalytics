import requests
import json
from server import setup
import time
import os
from server.request_handler import auth

session = requests.Session()
session.headers.update(setup.header)


def user_request(url, path):
    if not os.path.exists('./server/profiles/'+path.split('/')[3].split('.')[0]):
        os.mkdir('./server/profiles/'+path.split('/')[3].split('.')[0])
        os.mkdir(path % '0')
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
    v = int(os.listdir('./server/profiles/'+path.split('/')[3].split('.')[0]+'/post')[-1])+1
    if auth.is_auth:
        os.mkdir('./server/profiles/'+path.split('/')[3].split('.')[0]+'/post/'+str(v))
    else:
        v = 0
    make_request(url, path % str(v))
    time.sleep(1)


def make_request(url, path):
    r = session.get(url)
    jpost = r.json()
    with open(path, 'w') as fp:
        json.dump(jpost, fp)
    return jpost

