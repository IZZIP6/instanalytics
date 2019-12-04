from analytics.app.src.parser import profiling
from analytics.app.src import json_parser as parser


def get_user_data(info):
    username = profiling.get_username(info)
    fullname = profiling.get_fullname(info)
    id = profiling.get_idnumber(info)
    profiling.get_verified(info)
    bio = profiling.get_bio(info)
    no_followers = profiling.get_followers(info)
    no_following = profiling.get_following(info)
    profiling.get_business(info)
    profiling.get_private(info)
    no_posts = profiling.get_postnumber(info)
    if profiling.send_requests.is_requested:
        url = profiling.get_profile_pic(info)
    cursor = ''
    # if not profiling.is_private:
      #  profiling.get_user_post(parser.id_number(info), parser.username(info))

    context = {
        'username': username,
        'fullname': fullname,
        'id': id,
        'bio': bio,
        'n_followers': no_followers,
        'n_following': no_following,
        'n_post': no_posts,
        'url': profiling.get_username(info)+'.jpg',
        'cursor': cursor
    }
    return context