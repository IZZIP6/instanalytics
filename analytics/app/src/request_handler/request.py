import requests
import json
from analytics.app.src import setup
import time
import os
from analytics.app.src.request_handler import auth
from analytics.profiles import dir
import shutil
import numpy as np

session = requests.Session()
session.headers.update(setup.header)


def user_request(url, username):
    directory = dir.abs_path+'\\'+username+'\\'+'profile'
    if not os.path.exists(directory+'\\'+'0'):
        os.makedirs(directory+'\\'+'0')
    else:
        v = len(os.listdir(directory))
        os.makedirs(directory + '\\' + str(v))
    try:
        make_request(url, directory+'\\'+str(v)+'\\'+username+'.json')
    except json.decoder.JSONDecodeError as e:
        print('Wrong username')
        os.rmdir(directory)



def media_request(url, username):
    media_directory = dir.abs_path+'\\'+username+'\\'+'post'
    if not os.path.exists(media_directory):
        os.mkdir(media_directory)
    n = len(os.listdir(media_directory))
    make_request(url, media_directory+'\\'+username+'\\'+str(n)+".json")
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

