def end_cursor(data):
    return data['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']


def edge_post(data):
    return data['data']['user']['edge_owner_to_timeline_media']['edges']


def caption(data):
    return data['node']['edge_media_to_caption']['edges'][0]['node']['text']


def like_number(data):
    return data['node']['edge_media_preview_like']['count']


def comment_number(data):
    return data['node']['edge_media_to_comment']['count']


def time_stamp(data):
    return data['node']['taken_at_timestamp']


def username(data):
    return data['graphql']['user']['username']


def full_name(data):
    return data['graphql']['user']['full_name']


def followers(data):
    return str(data['graphql']['user']['edge_followed_by']['count'])


def following(data):
    return str(data['graphql']['user']['edge_follow']['count'])


def id_number(data):
    return data['graphql']['user']['id']


def is_verified(data):
    return data['graphql']['user']['is_verified']


def biography(data):
    return data['graphql']['user']['biography']


def is_business(data):
    return data['graphql']['user']['is_business_account']


def business_category(data):
    return data['graphql']['user']['business_category_name']


def is_private(data):
    return data['graphql']['user']['is_private']


def post_number(data):
    return data['graphql']['user']['edge_owner_to_timeline_media']['count']


def shortcode(data):
    return data['node']['shortcode']


def profile_pic(data):
    return data['graphql']['user']['profile_pic_url_hd']