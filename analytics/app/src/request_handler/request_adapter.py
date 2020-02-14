import requests
import json
from analytics.app.src import setup
import time
import os
from analytics.profiles import dir
import shutil
from analytics.app.src.request_handler.request import make_request

session = requests.Session()
session.headers.update(setup.header)


def user_request(url, username):
    directory = dir.abs_path+'\\'+username+'\\'+'profile'
    if not os.path.exists(directory+'\\'+'0'):
        os.makedirs(directory+'\\'+'0')
        v = 0
    else:
        v = len(os.listdir(directory))
        os.makedirs(directory + '\\' + str(v))
    try:
        make_request(session, url, directory+'\\'+str(v)+'\\'+username+'.json')
    except json.decoder.JSONDecodeError as e:
        print('Wrong username\n')
        print(e)
        os.rmdir(directory)

def user_media_request(url, username):
    media_directory = dir.abs_path+'\\'+username+'\\'+'media'
    if not os.path.exists(media_directory):
        os.mkdir(media_directory)
    n = len(os.listdir(media_directory))
    make_request(session, url, media_directory+'\\'+str(n)+".json")
    time.sleep(1)







def comment_media_request(url, username, shortcode):
    media_directory = dir.abs_path+'\\'+username+'\\'+'comment'
    if not os.path.exists(media_directory):
        os.mkdir(media_directory)
    n = len(os.listdir(media_directory))
    make_request(session, url, media_directory+'\\'+str(n)+".json")
    time.sleep(1)










def post_request(url, shortcode, username):
    post_directory = dir.abs_path+'\\'+username+'\\'+shortcode
    if not os.path.exists(post_directory):
        os.mkdir(post_directory)
    make_request(session, url, post_directory+'\\'+shortcode+'.json')



def profile_pic_request(url, path):
    r = requests.get(url, stream=True)
    with open(path, 'wb') as fp:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, fp)




