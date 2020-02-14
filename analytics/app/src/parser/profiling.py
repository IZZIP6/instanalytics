import json
import datetime
import numpy as np
from .. import endpoint
from .. import json_parser as parser
from ..request_handler import request_adapter as rq
from ..request_handler import send_requests
from analytics.static import dir as dir_static
from analytics.profiles import dir
import os
import shutil

hour_vect = np.zeros(24)

is_private      = False
is_verified     = False
is_business     = False


def get_username(info):
    print('Username:\t\t\t', parser.username(info))
    return parser.username(info)


def get_fullname(info):
    print('Full Name:\t\t\t', parser.full_name(info))
    return parser.full_name(info)

def get_idnumber(info):
    user_id = parser.id_number(info)
    print('Id Number:\t\t\t', user_id)
    return user_id


def get_verified(info):
    if parser.is_verified(info):
        print('This account is verified')
        is_verified = True


def get_bio(info):
    print('Biography:\t\t\t', parser.biography(info))
    return parser.biography(info)


def get_followers(info):
    print('Followers:\t\t\t', parser.followers(info))
    return parser.followers(info)


def get_following(info):
    print('Following:\t\t\t', parser.following(info))
    return parser.following(info)


def get_business(info):
    if parser.is_business(info):
        print('Business account:\t', parser.business_category(info))
        is_business = True


def get_private(info):
    if parser.is_private(info):
        print('This user has private account.')
        is_private = True

def get_postnumber(info):
    n_post = parser.post_number(info)
    print('No. Post:\t\t\t', n_post)
    return n_post


def get_profile_pic(info):
    url = parser.profile_pic(info)
    rq.profile_pic_request(url, dir_static.abs_path + '\\profile_pic\\' + get_username(info) + '.jpg')

def get_shortcode_list(info):
    list = []
    url = []
    post_number = get_postnumber(info)
    if post_number>12:
        post_number = 12
    for i in range(0, post_number-1):
        list.append(parser.shortcode_list(info, i))
        url.append(parser.shortcode_url(info, i))
    return list, url

# NON USARE è DA MODIFICARE
def get_user_post(user_id, profile_name):
    count_end_cursor = 0
    '''
        Since I'm not interested in latest verions, remove old Media directory, if a Media directory exists
    '''
    post_directory = dir.abs_path+'\\'+profile_name+'\\media'
    if os.path.exists(post_directory) and send_requests.is_requested:
        shutil.rmtree(post_directory)

    '''
        Send the first requests with end cursor null. It returns the first 20 posts of the selected username
    '''
    if send_requests.is_requested:
        rq.user_media_request(endpoint.request_account_medias(user_id, "null"), profile_name)

    '''
        Open the json and set the new end cursor
    '''
    with open(post_directory+'\\'+str(os.listdir(post_directory)[-1]), 'r') as post_json:
        data = json.load(post_json)
    end_cursor = '"'+parser.end_cursor(data)+'"'


    while not end_cursor is None:
        count_end_cursor += 1
        '''
            Messo soltanto perchè endcurson non sarà mai null dato che non facciamo esattamente tutte le richieste
        '''
        print(count_end_cursor)
        if count_end_cursor == 2:
            break

        '''
            Send recursive requests until no other posts are found    
        '''
        if send_requests.is_requested:
            rq.user_media_request(endpoint.request_account_medias(user_id, end_cursor), profile_name)

        with open(post_directory+'\\'+str(os.listdir(post_directory)[-1]), 'r') as post_json:
            data = json.load(post_json)
            end_cursor = '"'+parser.end_cursor(data)+'"'


def get_user_post_comment(user_id, profile_name, shortcode):
    count_end_cursor = 0
    '''
        Since I'm not interested in latest verions, remove old Media directory, if a Media directory exists
    '''
    post_directory = dir.abs_path+'\\'+profile_name+'\\comment'
    if os.path.exists(post_directory) and send_requests.is_requested:
        shutil.rmtree(post_directory)

    '''
        Send the first requests with end cursor null. It returns the first 20 posts of the selected username
    '''
    if send_requests.is_requested:
        print(endpoint.request_comment(shortcode, ''))
        rq.comment_media_request(endpoint.request_comment(shortcode, ''), profile_name, shortcode)

    '''
        Open the json and set the new end cursor
    '''

    with open(post_directory+'\\'+str(os.listdir(post_directory)[-1]), 'r') as post_json:
            print(post_directory+'\\'+str(os.listdir(post_directory)[-1]))
            data = json.load(post_json)
            end_cursor = '"'+parser.end_cursor_comment(data)+'"'


    while not end_cursor is None:
        count_end_cursor += 1
        '''
            Messo soltanto perchè endcurson non sarà mai null dato che non facciamo esattamente tutte le richieste
        '''
        print(count_end_cursor)
        if count_end_cursor == 2:
            break

        '''
            Send recursive requests until no other posts are found    
        '''
        if send_requests.is_requested:
            rq.user_media_request(endpoint.request_account_medias(user_id, end_cursor), profile_name)

        with open(post_directory+'\\'+str(os.listdir(post_directory)[-1]), 'r') as post_json:
            data = json.load(post_json)
            end_cursor = '"'+parser.end_cursor_comment(data)+'"'

