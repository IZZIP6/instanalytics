import requests
import json
from analytics.app.src import setup
import time
import os
from analytics.app.src.request_handler import auth
from analytics.profiles import dir
import shutil

session = requests.Session()
session.headers.update(setup.header)


def user_request(url, username):
    directory = dir.abs_path
    print(directory)
    if not os.path.exists(directory+'\\'+username):
        os.mkdir(directory+'\\'+username)
    try:
        make_request(url, directory+'\\'+username+'\\'+username+'.json')
    except json.decoder.JSONDecodeError as e:
        print('Wrong username')
        os.rmdir(directory+'\\'+username)


def media_request(url, path):
    if not os.path.exists('./src/profiles/'+path.split('/')[3].split('.')[0]+'/post'):
        os.mkdir('./src/profiles/'+path.split('/')[3].split('.')[0]+'/post')
    v = int(os.listdir('./src/profiles/'+path.split('/')[3].split('.')[0]+'/post')[-1])+1
    if auth.is_auth:
        os.mkdir('./src/profiles/'+path.split('/')[3].split('.')[0]+'/post/'+str(v))
    else:
        v = 0
    make_request(url, path % str(v))
    time.sleep(1)


def profile_pic_req(url, path):
    r = requests.get(url, stream=True)
    with open(path, 'wb') as fp:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, fp)


def make_request(url, path):
    r = session.get(url)
    jpost = r.json()
    with open(path, 'w') as fp:
        json.dump(jpost, fp)
    return jpost

