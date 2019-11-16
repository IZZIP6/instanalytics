import requests
import json
import os
import time
import os

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Host': 'www.instagram.com', 'Accept': '*/*', 'Connection': 'keep-alive'})


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

