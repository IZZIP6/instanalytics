import numpy as np
from app.parser import json_parser as parser
from app.parser import json_comment_parser as comment_parser
import re


hour_vect = np.zeros(24)


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


def get_shortcode_list(info):
    list = []
    url = []
    post_number = get_post_number(info)
    if post_number>12:
        post_number = 12
    for i in range(0, post_number-1):
        list.append(parser.shortcode_list(info, i))
        url.append(parser.shortcode_url(info, i))
    return list, url


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


def get_post_data1(info):
    post_type_name = []
    post_id = []
    post_comment_count = []
    post_comments_disabled = []
    post_taken_at_timestamp = []
    post_dimensions_height = []
    post_dimensions_width = []
    post_preview = get_post_number(info)
    if post_preview > 12:
        post_preview = 12
    for i in range(0, post_preview):
        post_type_name.append(parser.post_typename(info, i))
        post_id.append(parser.post_id(info, i))
        post_comment_count.append(parser.post_comment_count(info, i))
        post_comments_disabled.append(parser.post_comments_disabled(info, i))
        post_taken_at_timestamp.append(parser.post_taken_at_timestamp(info, i))
        post_dimensions_height.append(parser.post_dimensions_height(info, i))
        post_dimensions_width.append(parser.post_dimensions_width(info, i))
    return post_type_name, post_id, post_comment_count, post_comments_disabled,\
        post_taken_at_timestamp, post_dimensions_height, post_dimensions_width


def get_post_edge_media_to_caption(info):
    post_edge_media_to_caption = []
    post_preview = get_post_number(info)
    if post_preview > 12:
        post_preview = 12
    for i in range(0, post_preview):
        post_edge_media_to_caption.append(parser.post_edge_media_to_caption(info, i))
    return post_edge_media_to_caption


def get_post_edge_media_to_caption_text(info, i):
    post_edge_media_to_caption_text = parser.post_edge_media_to_caption_text(info, i)
    return post_edge_media_to_caption_text


def get_post_location(info):
    post_location = []
    post_preview = get_post_number(info)
    if post_preview > 12:
        post_preview = 12
    for i in range(0, post_preview):
        post_location.append(parser.post_location(info, i))
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


def get_post_is_video(info):
    post_is_video = []
    post_preview = get_post_number(info)
    if post_preview > 12:
        post_preview = 12
    for i in range(0, post_preview):
        post_is_video.append(parser.post_is_video(info, i))
    return post_is_video


def get_post_video_view_count(info, i):
    post_video_view_count = parser.post_video_view_count(info, i)
    return post_video_view_count


def get_post_like(info):
    post_num_like = []
    post_preview_num_like = []

    post_preview = get_post_number(info)
    if post_preview > 12:
        post_preview = 12
    for i in range(0, post_preview):
        post_num_like.append(parser.post_num_like(info, i))
        post_preview_num_like.append(parser.post_preview_num_like(info, i))
    return post_num_like, post_preview_num_like


def get_post_owner(info):
    post_owner_id = []
    post_owner_username = []
    post_preview = get_post_number(info)
    if post_preview > 12:
        post_preview = 12
    for i in range(0, post_preview):
        post_owner_id.append(parser.post_owner_id(info, i))
        post_owner_username.append(parser.post_owner_username(info, i))
    return post_owner_id, post_owner_username


def get_post_data2(info):
    post_gating_info = []
    post_fact_check_overall_rating = []
    post_fact_check_information = []
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


def get_shortcode_list(info):
    list = []
    url = []
    post_number = get_post_number(info)
    if post_number > 12:
        post_number = 12
    for i in range(0, post_number):
        list.append(parser.shortcode_list(info, i))
        url.append(parser.shortcode_url(info, i))
    return list, url


'''Found hashtag'''


def post_found_hashtag(info):
    post_hashtag = []
    post_number = get_post_number(info)
    if post_number > 12:
        post_number = 12
    for i in range(0, post_number):
        edges = get_post_edge_media_to_caption(info)
        if edges[i]:
            text = get_post_edge_media_to_caption_text(info, i)
            regex = r"#[^ #]+"
            matches = [match.group() for match in re.finditer(regex, text, re.MULTILINE)]
            post_hashtag.append(matches)
        else:
            post_hashtag.append("None")
    return post_hashtag


''' Found tag in post caption text'''


def post_found_tag(info):
    post_tag = []
    post_number = get_post_number(info)
    if post_number > 12:
        post_number = 12
    for i in range(0, post_number):
        edges = get_post_edge_media_to_caption(info)
        if edges[i]:
            text = get_post_edge_media_to_caption_text(info, i)
            regex = r"@[^ @]+"
            matches = [match.group() for match in re.finditer(regex, text, re.MULTILINE)]
            post_tag.append(matches)
        else:
            post_tag.append("None")
    return post_tag


''' comment get data '''


def get_comment_has_next_page(data):
    comment_has_next_page = comment_parser.comment_has_next_page(data)
    return comment_has_next_page


def get_comment_id(comment_list):
    comment_id = []
    comment_count = len(comment_parser.comment_post_edge_media_to_comment(comment_list))
    for i in range(0, comment_count):
        comment_id.append(comment_parser.comment_id(comment_list, i))
    return comment_id


def get_comment_text(comment_list):
    comment_text = []
    comment_count = len(comment_parser.comment_post_edge_media_to_comment(comment_list))
    for i in range(0, comment_count):
        comment_text.append(comment_parser.comment_text(comment_list, i))
    print("comment text\t\t\t", comment_text)
    return comment_text


def get_comment_created_at(comment_list):
    comment_created_at = []
    comment_count = len(comment_parser.comment_post_edge_media_to_comment(comment_list))
    for i in range(0, comment_count):
        comment_created_at.append(comment_parser.comment_created_at(comment_list, i))
    return  comment_created_at


def get_comment_owner_id(comment_list):
    comment_owner_id = []
    comment_count = len(comment_parser.comment_post_edge_media_to_comment(comment_list))
    for i in range(0, comment_count):
        comment_owner_id.append(comment_parser.comment_owner_id(comment_list, i))
    return comment_owner_id


def get_comment_owner_username(comment_list):
    comment_owner_username = []
    comment_count = len(comment_parser.comment_post_edge_media_to_comment(comment_list))
    for i in range(0, comment_count):
        comment_owner_username.append(comment_parser.comment_owner_username(comment_list, i))
    return comment_owner_username


''' Found Comment tag'''

def comment_found_tag(comment_list):
    comment_tag = []
    comment_count = len(comment_parser.comment_post_edge_media_to_comment(comment_list))
    text = get_comment_text(comment_list)
    for i in range(0, comment_count):
        if text[i]:
            regex = r"@[^ @]+"
            matches = [match.group() for match in re.finditer(regex, text[i], re.MULTILINE)]
            comment_tag.append(matches)
        else:
            comment_tag.append("None")
    return comment_tag


''' Found Comment tag'''

def comment_found_hashtag(comment_list):
    comment_hashtag = []
    comment_count = len(comment_parser.comment_post_edge_media_to_comment(comment_list))
    text = get_comment_text(comment_list)
    for i in range(0, comment_count):
        if text[i]:
            regex = r"#[^ #]+"
            matches = [match.group() for match in re.finditer(regex, text[i], re.MULTILINE)]
            comment_hashtag.append(matches)
        else:
            comment_hashtag.append("None")
    return comment_hashtag

