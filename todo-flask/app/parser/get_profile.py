from . import profiling
from .. import json_parser as parser


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
    #list_of_shortcode, list_of_url = profiling.get_shortcode_list(info)
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
        'url': 'profile_pic\\'+profiling.get_username(info)+'.jpg',
        #'cursor': cursor,
        #'first_post_shortcode' : list_of_shortcode[0],
        #'first_post_url' : list_of_url[0],
    }
    return context