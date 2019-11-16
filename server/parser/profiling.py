import json
import datetime
import numpy as np
import server.endpoint as endpoint
import server.json_parser as parser
from server.request_handler import request as rq
from server.request_handler import send_requests

hour_vect = np.zeros(24)

is_private      = False
is_verified     = False
is_business     = False


def get_username(info):
    print('Username:\t\t\t', parser.username(info))


def get_fullname(info):
    print('Full Name:\t\t\t', parser.full_name(info))


def get_idnumber(info):
    user_id = parser.id_number(info)
    print('Id Number:\t\t\t', user_id)


def get_verified(info):
    if parser.is_verified(info):
        print('This account is verified')
        is_verified = True


def get_bio(info):
    print('Biography:\t\t\t', parser.biography(info))


def get_followers(info):
    print('Followers:\t\t\t', parser.followers(info))


def get_following(info):
    print('Following:\t\t\t', parser.following(info))


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


def get_user_data(info):
    get_username(info)
    get_fullname(info)
    get_idnumber(info)
    get_verified(info)
    get_bio(info)
    get_followers(info)
    get_following(info)
    get_business(info)
    get_private(info)
    get_postnumber(info)
    if not is_private:
        get_user_post(parser.id_number(info), parser.username(info))


def get_user_post(user_id, profile_name):
    max_like = 0
    max_comment = 0
    count_end_cursor = 0
    print('\n[LATEST POST]')
    url = endpoint.request_account_medias(user_id, 'null')
    if send_requests.is_requested:
        rq.media_request(url, './server/profiles/'+profile_name+'/post/'+profile_name+'_post.json')
    with open('./server/profiles/'+profile_name+'/post/'+profile_name+'_post.json', 'r') as post_json:
        data = json.load(post_json)
    end_cursor = parser.end_cursor(data)
    edges_post = parser.edge_post(data)
    max_like, max_comment = show_post(edges_post, max_like, max_comment)
    while not end_cursor is None:
        count_end_cursor += 1
        if send_requests.is_requested:
            url = endpoint.request_account_medias(user_id, end_cursor)
            rq.user_request(url, './server/profiles/'+profile_name+'/post/'+profile_name+'_post'+str(count_end_cursor)+'.json')
        with open('./server/profiles/'+profile_name+'/post/'+profile_name+'_post'+str(count_end_cursor)+'.json', 'r') as post_json:
            data = json.load(post_json)
            end_cursor = parser.end_cursor(data)
            print(end_cursor)
            edges_post = parser.edge_post(data)
            max_like, max_comment = show_post(edges_post, max_like, max_comment)
    print(max_like, max_comment)
    for i in range(len(hour_vect)):
        print(i, '\t', hour_vect[i])
    print(hour_vect.argmax(), hour_vect.max())


def show_post(edges_post, max_like, max_comment):
    for i in range(0, len(edges_post)):
        print('Post Code\t\t\t', parser.shortcode(edges_post[i]))
        try:
            print('Caption\t\t\t\t', parser.caption(edges_post[i]))
        except IndexError as e:
            print('No Caption')
        n_like = parser.like_number(edges_post[i])
        if n_like>max_like:
            max_like = n_like
        print('No. like\t\t\t', n_like)
        n_comment = parser.comment_number(edges_post[i])
        if n_comment>max_comment:
            max_comment = n_comment
        print('No. comment\t\t\t', n_comment)
        date = datetime.datetime.fromtimestamp(parser.time_stamp(edges_post[i]))
        hour = int(date.strftime('%H'))
        hour_vect[hour] += n_like
        print('Date\t\t\t\t', date.strftime('%Y %B %d %A %H:%M:%S'))
        print()
    return max_like, max_comment

# https://www.instagram.com/graphql/query/?query_id=17888483320059182&variables={"id": "234962686","first":20,"after":null}
