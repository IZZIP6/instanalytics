def edge_post_comment_count(data):
    return data['data']['shortcode_media']['edge_media_to_comment']['count']


def comment_has_next_page(data):
    return data['data']['shortcode_media']['edge_media_to_comment']['page_info']['has_next_page']


def comment_end_cursor(data):
    return data['data']['shortcode_media']['edge_media_to_comment']['page_info']['end_cursor']


def comment_id(data, i):
    return data['data']['shortcode_media']['edge_media_to_comment']['edges'][i]['node']['id']


def comment_text(data, i):
    return data['data']['shortcode_media']['edge_media_to_comment']['edges'][i]['node']['text']


def comment_created_at(data, i):
    return data['data']['shortcode_media']['edge_media_to_comment']['edges'][i]['node']['created_at']


def comment_owner_id(data, i):
    return data['data']['shortcode_media']['edge_media_to_comment']['edges'][i]['node']['owner']['id']


def comment_owner_username(data, i):
    return data['data']['shortcode_media']['edge_media_to_comment']['edges'][i]['node']['owner']['username']


def comment_post_edge_media_to_comment(data):
    return data['data']['shortcode_media']['edge_media_to_comment']['edges']