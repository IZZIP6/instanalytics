import numpy as np
from app.parser import json_parser as parser
from app.parser import json_comment_parser as comment_parser
from app.parser import json_post_parser as post_parser
import datetime
import re

post_number = 0


def get_username(info):
    return parser.username(info)


def get_fullname(info):
    return parser.full_name(info)


def get_idnumber(info):
    user_id = parser.id_number(info)
    return user_id


def get_verified(info):
    is_verified = parser.is_verified(info)
    return is_verified


def get_bio(info):
    return parser.biography(info)


def get_followers(info):
    return parser.followers(info)


def get_following(info):
    return parser.following(info)


def get_business(info):
    is_business = parser.is_business(info)
    return is_business


def get_private(info):
    is_private = parser.is_private(info)
    return is_private


def get_post_number(info):
    n_post = parser.post_number(info)
    return n_post


def get_profile_pic(info):
    url = parser.profile_pic(info)
    return url


def get_show_suggested_profiles(info):
    return parser.show_suggested_profiles(info)


def get_blocked_by_viewer(info):
    return parser.blocked_by_viewer(info)


def get_show_follow_dialog(info):
    return parser.blocked_by_viewer(info)


def get_country_block(info):
    return parser.country_block(info)


def get_followed_by_viewer(info):
    return parser.followed_by_viewer(info)


def get_follows_viewer(info):
    return parser.follows_viewer(info)


def get_has_channel(info):
    return parser.has_channel(info)


def get_has_blocked_viewer(info):
    return parser.has_blocked_viewer(info)


def get_has_requested_viewer(info):
    return parser.has_requested_viewer(info)


def get_is_joined_recently(info):
    return parser.is_joined_recently(info)


def get_requested_by_viewer(info):
    return parser.requested_by_viewer(info)


def get_connected_fb_page(info):
    return parser.connected_fb_page(info)


def get_edge_felix_video_timeline_count(info):
    n_edge_felix_video = parser.edge_felix_video_timeline_count(info)
    return n_edge_felix_video


def get_edge_felix_video_timeline_has_next_page(info):
    return parser.edge_felix_video_timeline_has_next_page(info)


def get_edge_felix_video_timeline_end_cursor(info):
    return parser.edge_felix_video_timeline_end_cursor(info)


def get_edge_owner_to_timeline_media_has_next_page(info):
    return parser.edge_owner_to_timeline_media_has_next_page(info)


def get_edge_owner_to_timeline_media_end_cursor(info):
    return parser.edge_owner_to_timeline_media_end_cursor(info)


def get_post_edge_media_to_caption(info):
    post_edge_media_to_caption = []
    post_preview = get_post_number(info)
    if post_preview > 12:
        post_preview = 12
    for i in range(0, post_preview):
        post_edge_media_to_caption.append(parser.post_edge_media_to_caption(info, i))
    return post_edge_media_to_caption


def get_post_text(info):
    post_edge_media_to_caption = get_post_edge_media_to_caption(info)
    post_edge_media_to_caption_text = []
    for i in range(0, len(post_edge_media_to_caption)):
        if not post_edge_media_to_caption[i]:
            post_edge_media_to_caption_text.append(" ")
        else:
            post_edge_media_to_caption_text.append(get_post_edge_media_to_caption_text(info, i))
    return post_edge_media_to_caption_text


def get_post_edge_media_to_caption_text(info, i):
    post_edge_media_to_caption_text = parser.post_edge_media_to_caption_text(info, i)
    return post_edge_media_to_caption_text


post_location                               = []
post_is_video                               = []
post_owner_id                               = []
post_owner_username                         = []


def reset_profile_post_1():
    global post_location
    global post_is_video
    global post_owner_id
    global post_owner_username
    post_location                            = []
    post_is_video                            = []
    post_owner_id                            = []
    post_owner_username                      = []


def post_for_function_1(info):
    post_preview = get_post_number(info)
    if post_preview > 12:
        post_preview = 12
    for i in range(0, post_preview):
        post_location.append(parser.post_location(info, i))
        post_is_video.append(parser.post_is_video(info, i))
        post_owner_id.append(parser.post_owner_id(info, i))
        post_owner_username.append(parser.post_owner_username(info, i))


def get_post_location():
    return post_location


def get_post_location_id(info, i):
    post_location_id = parser.post_location_id(info, i)
    return post_location_id


def get_post_location_has_public_page(info, i):
    post_location_has_public_page = parser.post_location_has_public_page(info, i)
    return post_location_has_public_page


def get_post_location_name(info, i):
    post_location_name = parser.post_location_name(info, i)
    return post_location_name


def get_post_location_slug(info, i):
    post_location_slug = parser.post_location_slug(info, i)
    return post_location_slug


def get_post_owner():
    return post_owner_id, post_owner_username


def get_post_is_video():
    return post_is_video

'''
    def get_post_video_view_count(info, i):
        post_video_view_count = parser.post_video_view_count(info, i)
        return post_video_view_count
'''


def get_post_like(info):
    post_num_like                        = []
    post_preview_num_like                = []
    post_preview = get_post_number(info)
    if post_preview > 12:
        post_preview = 12
    for i in range(0, post_preview):
        post_num_like.append(parser.post_num_like(info, i))
        post_preview_num_like.append(parser.post_preview_num_like(info, i))
    return post_num_like, post_preview_num_like


def get_post_data2(info):
    post_gating_info                     = []
    post_fact_check_overall_rating       = []
    post_fact_check_information          = []
    post_preview = get_post_number(info)
    if post_preview > 12:
        post_preview = 12
    for i in range(0, post_preview):
        post_gating_info.append(parser.post_gating_info(info, i))
        post_fact_check_overall_rating.append(parser.post_fact_check_overall_rating(info, i))
        post_fact_check_information.append(parser.post_fact_check_information(info, i))
    return post_gating_info, post_fact_check_overall_rating, post_fact_check_information


def get_post_media_preview(info, i):
    post_media_preview = parser.post_media_preview(info, i)
    return post_media_preview


def get_post_accessibility(info, i):
    post_accessibility_caption = parser.post_accessibility_caption(info, i)

    return post_accessibility_caption


def get_highlight_reel_count(info):
    n_highlight_reel = parser.highlight_reel_count(info)
    return n_highlight_reel


def get_logging_page_id(info):
    logging_page_id = parser.logging_page_id(info)
    return logging_page_id


def get_external_url(info):
    external_url = parser.external_url(info)
    return external_url


def get_external_url_linkshimmed(info):
    external_url_linkshimmed= parser.external_url_linkshimmed(info)
    return external_url_linkshimmed


def get_edge_mutual_followed_by_count(info):
    num_edge_mutual_followed_by = parser.edge_mutual_followed_by_count(info)
    return num_edge_mutual_followed_by


def get_edge_saved_media_count(info):
    num_edge_saved_media = parser.edge_saved_media_count(info)
    return num_edge_saved_media


def get_edge_saved_media_has_next_page(info):
    edge_saved_media_has_next_page = parser.edge_saved_media_has_next_page(info)
    return edge_saved_media_has_next_page


def get_edge_saved_media_end_cursor(info):
    edge_saved_media_end_cursor = parser.edge_saved_media_end_cursor(info)
    return edge_saved_media_end_cursor


def get_edge_media_collections_count(info):
    edge_media_collections_count = parser.edge_media_collections_count(info)
    return edge_media_collections_count


def get_edge_media_collections_has_next_page(info):
    edge_media_collections_has_next_page = parser.edge_media_collections_has_next_page(info)
    return edge_media_collections_has_next_page


def get_edge_media_collections_end_cursor(info):
    edge_media_collections_end_cursor = parser.edge_media_collections_end_cursor(info)
    return edge_media_collections_end_cursor


def get_toast_content_on_load(info):
    toast_content_on_load = parser.toast_content_on_load(info)
    return toast_content_on_load


list_shortcode                     = []
url                                = []
post_hashtag                       = []
post_tag                           = []
post_type_name                     = []
post_id                            = []
post_comment_count                 = []
post_comments_disabled             = []
post_taken_at_timestamp            = []
post_dimensions_height             = []
post_dimensions_width              = []
list_shortcode_url                 = []


def reset_profile_post():
    global list_shortcode
    global url
    global post_hashtag
    global post_tag
    global post_type_name
    global post_id
    global post_comment_count
    global post_comments_disabled
    global post_taken_at_timestamp
    global post_dimensions_height
    global post_dimensions_width
    list_shortcode                       = []
    url                                  = []
    post_hashtag                         = []
    post_tag                             = []
    post_type_name                       = []
    post_id                              = []
    post_comment_count                   = []
    post_comments_disabled               = []
    post_taken_at_timestamp              = []
    post_dimensions_height               = []
    post_dimensions_width                = []
    list_shortcode_url                   = []


def profile_post_for_function(info):
    post_number = get_post_number(info)
    if post_number > 12:
        post_number = 12
    for i in range(0, post_number):
        list_shortcode.append(parser.shortcode_list(info, i))
        url.append(parser.shortcode_url(info, i))
        list_shortcode_url.append((parser.shortcode_list(info, i),parser.shortcode_url(info, i)))
        edges = get_post_edge_media_to_caption(info)
        post_type_name.append(parser.post_typename(info, i))
        post_id.append(parser.post_id(info, i))
        post_comment_count.append(parser.post_comment_count(info, i))
        post_comments_disabled.append(parser.post_comments_disabled(info, i))
        post_taken_at_timestamp.append(parser.post_taken_at_timestamp(info, i))
        post_dimensions_height.append(parser.post_dimensions_height(info, i))
        post_dimensions_width.append(parser.post_dimensions_width(info, i))
        if edges[i]:
            text = get_post_edge_media_to_caption_text(info, i)
            regex = r"#[^ #]+"
            matches = [match.group() for match in re.finditer(regex, text, re.MULTILINE)]
            post_hashtag.append(matches)

            text = get_post_edge_media_to_caption_text(info, i)
            regex = r"@[^ @]+"
            matches = [match.group() for match in re.finditer(regex, text, re.MULTILINE)]
            post_tag.append(matches)
        else:
            post_hashtag.append(" ")
            post_tag.append(" ")


def get_shortcode_list():
    return list_shortcode, url


def get_shortcode_url_list():
    return list_shortcode_url


'''Found hashtag in post caption text'''


def post_found_hashtag():
    return post_hashtag


''' Found tag in post caption text'''


def post_found_tag():
    return post_tag


def get_post_type_name():
    return post_type_name


def get_post_id():
    return post_id


def get_post_comment_count():
    return post_comment_count


def get_post_comments_disabled():
    return post_comments_disabled


def get_post_taken_at_timestamp():
    return post_taken_at_timestamp


def get_post_dimensions():
    return post_dimensions_height, post_dimensions_width


def get_timestamp(info):
    post_number = get_post_number(info)
    datep = []
    hour_vect = np.zeros(24)
    timestamp = []
    if post_number > 12:
        post_number = 12
    for i in range(0, post_number):
        date = datetime.datetime.fromtimestamp(parser.post_taken_at_timestamp(info, i))
        hour = int(date.strftime('%H'))
        hour_vect[hour] += parser.post_num_like(info, i)
        datep.append(hour)
    for i in range(0, 24):
        timestamp.append(hour_vect[i])
    return timestamp, datep


''' comment get data '''

comment_id                       = []
comment_text                     = []
comment_created_at               = []
comment_owner_id                 = []
comment_owner_username           = []
comment_hashtag                  = []
comment_tag                      = []


def reset_comment():
    global comment_id
    global comment_text
    global comment_created_at
    global comment_owner_id
    global comment_owner_username
    global comment_hashtag
    global comment_tag
    comment_id                   = []
    comment_text                 = []
    comment_created_at           = []
    comment_owner_id             = []
    comment_owner_username       = []
    comment_hashtag              = []
    comment_tag                  = []


def comment_for_function(data):
     for comment in comment_parser.comment_post_edge_media_to_comment(data):
        comment_id.append(comment_parser.comment_id(comment))
        comment_text.append(comment_parser.comment_text(comment))
        comment_created_at.append(comment_parser.comment_created_at(comment))
        comment_owner_id.append(comment_parser.comment_owner_id(comment))
        comment_owner_username.append(comment_parser.comment_owner_username(comment))

        try:
            if comment_text[-1]:
                regex = r"@[^ @]+"
                matches = [match.group() for match in re.finditer(regex, comment_text[-1], re.MULTILINE)]
                comment_tag.append(matches)

                regex = r"#[^ #]+"
                matches = [match.group() for match in re.finditer(regex, comment_text[-1], re.MULTILINE)]
                comment_hashtag.append(matches)
            else:
                comment_tag.append(" ")

                comment_hashtag.append(" ")
        except IndexError:
            print('out of limits')


def get_comment_has_next_page(data):
    comment_has_next_page = comment_parser.comment_has_next_page(data)
    return comment_has_next_page


def get_comment_id():
    return comment_id


def get_comment_text():
    return comment_text


def get_comment_created_at():
    return comment_created_at


def get_comment_owner_id():
    return comment_owner_id


def get_comment_owner_username():
    return comment_owner_username


''' Found Comment tag'''


def comment_found_tag():
    return comment_tag


''' Found Comment tag'''


def comment_found_hashtag():
    return comment_hashtag


''' POST DATA'''


def post_get_post_count(info):
    post_count = post_parser.post_count(info)
    return post_count


def post_get_post_page_info_has_next_page(info):
    post_page_info_has_next_page = post_parser.post_page_info_has_next_page(info)
    return post_page_info_has_next_page


def post_get_post_page_info_end_cursor(info):
    post_page_info_end_cursor = post_parser.post_page_info_end_cursor(info)
    return post_page_info_end_cursor


def post_get_post_edges(info):
    post_edges = post_parser.post_edges(info)
    return post_edges


list_post_id                                = []
list_post_typename                          = []
list_post_edge_media_to_caption_shortcode   = []
list_post_edge_media_to_comment             = []
list_post_comment_count                     = []
list_post_comment_disbled                   = []
list_post_taken_at_timestamp                = []
list_post_dimensions                        = []
list_post_width                             = []
list_post_height                            = []
list_post_display_url                       = []
list_post_edge_media_preview_like           = []
list_post_edge_media_preview_like_count     = []
list_post_edge_media_to_caption_text        = []
list_post_text_tag                          = []
list_post_text_hashtag                      = []
list_post_owner                             = []
list_post_owner_id                          = []
list_post_thumbnail_src                     = []
list_post_is_video                          = []
list_video_view_count                       = []

def reset_post():
    global list_post_id
    global list_post_typename
    global list_post_edge_media_to_caption_shortcode
    global list_post_edge_media_to_comment
    global list_post_comment_count
    global list_post_comment_disbled
    global list_post_taken_at_timestamp
    global list_post_dimensions
    global list_post_width
    global list_post_height
    global list_post_display_url
    global list_post_edge_media_preview_like
    global list_post_edge_media_preview_like_count
    global list_post_edge_media_to_caption_text
    global list_post_text_tag
    global list_post_text_hashtag
    global list_post_owner
    global list_post_owner_id
    global list_post_thumbnail_src
    global list_post_is_video
    global list_video_view_count
    list_post_id                                       = []
    list_post_typename                                 = []
    list_post_edge_media_to_caption_shortcode          = []
    list_post_edge_media_to_comment                    = []
    list_post_comment_count                            = []
    list_post_comment_disbled                          = []
    list_post_taken_at_timestamp                       = []
    list_post_dimensions                               = []
    list_post_width                                    = []
    list_post_height                                   = []
    list_post_display_url                              = []
    list_post_edge_media_preview_like                  = []
    list_post_edge_media_preview_like_count            = []
    list_post_edge_media_to_caption_text               = []
    list_post_text_tag                                 = []
    list_post_text_hashtag                             = []
    list_post_owner                                    = []
    list_post_owner_id                                 = []
    list_post_thumbnail_src                            = []
    list_post_is_video                                 = []
    list_video_view_count                              = []


def post_for_function(info, n):
    post_preview = len(post_parser.post_edges(info))
    for i in range(0, post_preview):
        list_post_id.append(post_parser.post_id(info, i))
        list_post_typename.append(post_parser.post_typename(info, i))
        list_post_edge_media_to_caption_shortcode.append(post_parser.post_edge_media_to_caption_shortcode(info, i))
        list_post_edge_media_to_comment.append(post_parser.post_edge_media_to_comment(info, i))
        if list_post_edge_media_to_comment[i+n]:
            list_post_comment_count.append(post_parser.post_edge_media_to_comment_count(info, i))
        else:
            list_post_comment_count.append(" ")
        list_post_comment_disbled.append(post_parser.post_comment_disabled(info, i))
        list_post_taken_at_timestamp.append(post_parser.post_taken_at_timestamp(info, i))
        list_post_dimensions.append(post_parser.post_dimensions(info, i))
        if list_post_dimensions[i+n]:
            list_post_width.append(post_parser.post_width(info, i))
            list_post_height.append(post_parser.post_height(info, i))
        else:
            list_post_width.append(" ")
            list_post_height.append(" ")
        list_post_display_url.append(post_parser.post_display_url(info, i))
        list_post_edge_media_preview_like.append(post_parser.post_edge_media_preview_like(info, i))
        if list_post_edge_media_preview_like[i+n]:
            list_post_edge_media_preview_like_count.append(post_parser.post_edge_media_preview_like_count(info, i))
        else:
            list_post_edge_media_preview_like_count.append(" ")
        if list_post_edge_media_to_caption_text[i+n]:
            regex = r"@[^ @]+"
            matches = [match.group() for match in re.finditer(regex, list_post_edge_media_to_caption_text[i + n], re.MULTILINE)]
            list_post_text_tag.append(matches)

            regex = r"#[^ #]+"
            matches = [match.group() for match in re.finditer(regex, list_post_edge_media_to_caption_text[i + n], re.MULTILINE)]
            list_post_text_hashtag.append(matches)
        else:
            list_post_text_tag.append(" ")
            list_post_text_hashtag.append(" ")
        list_post_owner.append(post_parser.post_owner(info, i))
        if list_post_owner[i+n]:
            list_post_owner_id.append(post_parser.post_owner_id(info, i))
        else:
            list_post_owner_id.append(" ")
        list_post_thumbnail_src.append(post_parser.post_thumbnail_src(info, i))
        list_post_is_video.append(post_parser.post_is_video(info, i))
        if list_post_is_video[i+n]:
            list_video_view_count.append(post_parser.post_video_view_count(info, i))
        else:
            list_video_view_count.append(" ")


def post_get_post_id():
    return list_post_id


def post_get_post_typename():
    return list_post_typename


def post_get_post_edge_media_to_caption_edges(info):
    list_post_edge_media_to_caption_edges = []
    post_preview = len(post_parser.post_edges(info))
    for i in range(0, post_preview):
        list_post_edge_media_to_caption_edges.append(post_parser.post_edge_media_to_caption_edges(info, i))
    return list_post_edge_media_to_caption_edges


def post_get_post_text(info):
    post_edge_media_to_caption_edges = post_get_post_edge_media_to_caption_edges(info)
    for i in range(0, len(post_edge_media_to_caption_edges)):
        if not post_edge_media_to_caption_edges[i]:
            list_post_edge_media_to_caption_text.append(" ")
        else:
            list_post_edge_media_to_caption_text.append(post_parser.post_edge_media_to_caption_text(info, i))
    return list_post_edge_media_to_caption_text


def post_get_post_edge_media_to_caption_shortcode():
    return list_post_edge_media_to_caption_shortcode


def post_get_post_edge_media_to_comment_count():
    return list_post_comment_count


def post_get_post_comment_disabled():
    return list_post_comment_disbled


def post_get_post_taken_at_timestamp():
    return list_post_taken_at_timestamp


def post_get_post_dimensions():
    return list_post_width, list_post_height


def post_get_post_display_url():
    return list_post_display_url


def post_get_post_preview_like_count():
    return list_post_edge_media_preview_like_count


def post_get_post_tag():
    return list_post_text_tag


def post_get_post_hashtag():
    return list_post_text_hashtag


def post_get_post_owner_id():
    return list_post_owner_id


def post_get_list_post_thumbnail_src():
    return list_post_thumbnail_src


def post_get_post_is_video():
    return list_post_is_video


def post_get_post_video_view_count():
    return list_video_view_count