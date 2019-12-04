import json
import datetime
import numpy as np
from .. import endpoint
from .. import json_parser as parser
from ..request_handler import request as rq
from ..request_handler import send_requests
from analytics.static import dir
import os

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
    print(dir.abs_path+'\\'+get_username(info)+'.jpg')
    rq.profile_pic_req(url, dir.abs_path+'\\'+get_username(info)+'.jpg')


def get_user_post(user_id, profile_name):
    count_end_cursor = 0
    if send_requests.is_requested:
        rq.media_request(endpoint.request_account_medias(user_id, 'null'), profile_name)
    post_directory = dir.abs_path+'\\'+profile_name+'\\post'
    last_post_directory = post_directory+'\\'+str(os.listdir(post_directory)[-1])
    with open(last_post_directory+'\\'+profile_name+'_post.json', 'r') as post_json:
        data = json.load(post_json)
    end_cursor = parser.end_cursor(data)
    while not end_cursor is None:
        count_end_cursor += 1
        if send_requests.is_requested:
            rq.media_request(endpoint.request_account_medias(user_id, end_cursor), profile_name)
        with open(last_post_directory+'\\'+profile_name+'_post'+str(count_end_cursor)+'.json', 'r') as post_json:
            data = json.load(post_json)
            end_cursor = parser.end_cursor(data)

'''


# https://www.instagram.com/graphql/query/?query_id=17888483320059182&variables={"id": "234962686","first":20,"after":null}
'''