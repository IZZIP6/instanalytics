import json
import datetime
import numpy as np
from app.parser import json_parser as parser
from app.parser import json_comment_parser as comment_parser
'''from analytics.static import dir as dir_st'''
import os
import shutil
import re
from app.parser import get_comment


hour_vect = np.zeros(24)


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
    is_verified = parser.is_verified(info)
    if is_verified:
        print('This account is verified')
    return is_verified


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
    is_business = parser.is_business(info)
    if is_business:
        print('Business account:\t', parser.business_category(info))
    return is_business


def get_private(info):
    is_private = parser.is_private(info)
    if is_private:
        print('This user has private account.')
    return is_private


def get_post_number(info):
    n_post = parser.post_number(info)
    print('No. Post:\t\t\t', n_post)
    return n_post

'''
def get_profile_pic(info):
    url = parser.profile_pic(info)
    print(dir_st.abs_path+'\\'+get_username(info)+'.jpg')
    rq.profile_pic_req(url, dir_st.abs_path+'\\'+get_username(info)+'.jpg')
'''

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
    if parser.show_suggested_profiles(info):
        print('This user has suggested profiles.')
        return parser.show_suggested_profiles(info)


def get_blocked_by_viewer(info):
    if parser.blocked_by_viewer(info):
        print('This user has profile blocked by viewer.')
    return parser.blocked_by_viewer(info)


def get_show_follow_dialog(info):
    if parser.blocked_by_viewer(info):
        print('This user has profile blocked by viewer.')
        return parser.blocked_by_viewer(info)


def get_country_block(info):
    if parser.country_block(info):
        print('This user has country block.')
    return parser.country_block(info)


def get_followed_by_viewer(info):
    if parser.followed_by_viewer(info):
        print('This user is followed by viewer.')
    return parser.followed_by_viewer(info)


def get_follows_viewer(info):
    if parser.follows_viewer(info):
        print('This user is follows viewer.')
    return parser.follows_viewer(info)


def get_has_channel(info):
    if parser.has_channel(info):
        print('This user has channel.')
    return parser.has_channel(info)


def get_has_blocked_viewer(info):
    if parser.has_blocked_viewer(info):
        print('This user has blocked viewer.')
    return parser.has_blocked_viewer(info)


def get_has_requested_viewer(info):
    if parser.has_requested_viewer(info):
        print('This user has requester viewer.')
    return parser.has_requested_viewer(info)


def get_is_joined_recently(info):
    if parser.is_joined_recently(info):
        print('This user is joined recently.')
    return parser.is_joined_recently(info)


def get_requested_by_viewer(info):
    if parser.requested_by_viewer(info):
        print('This user is requested by viewer.')
    return parser.requested_by_viewer(info)


def get_connected_fb_page(info):
    if parser.connected_fb_page(info):
        print('This user has a connected fb page.')
    return parser.connected_fb_page(info)


def get_edge_felix_video_timeline_count(info):
    n_edge_felix_video = parser.edge_felix_video_timeline_count(info)
    print('edge felix video timeline count\t\t\t', n_edge_felix_video)
    return n_edge_felix_video


def get_edge_felix_video_timeline_has_next_page(info):
    if parser.edge_felix_video_timeline_has_next_page(info):
        print('edge felix video timeline has next page.')
        return parser.edge_felix_video_timeline_has_next_page(info)


def get_edge_felix_video_timeline_end_cursor(info):
    print('edge felix video timeline end cursor\t\t\t', parser.edge_felix_video_timeline_end_cursor(info))
    return parser.edge_felix_video_timeline_end_cursor(info)


def get_edge_owner_to_timeline_media_has_next_page(info):
    if parser.edge_owner_to_timeline_media_has_next_page(info):
        print('edge owner to timeline media has next page ')
    return parser.edge_owner_to_timeline_media_has_next_page(info)


def get_edge_owner_to_timeline_media_end_cursor(info):
    if parser.edge_owner_to_timeline_media_end_cursor(info):
        print('edge owner to timeline media end cursor')
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
    #print("num_like\t\t\t", post_num_like)
    #print("post_preview_num_like\t\t\t", post_preview_num_like)
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
    #print("post_owner_id\t\t\t", post_owner_id)
    #print("post_owner_username\t\t\t", post_owner_username)
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
    #print("accessibility_caption\t\t\t", post_accessibility_caption)
    return post_accessibility_caption


def get_highlight_reel_count(info):
    n_highlight_reel = parser.highlight_reel_count(info)
    print('number highlight reel\t\t\t', n_highlight_reel)
    return n_highlight_reel


def get_logging_page_id(info):
    logging_page_id = parser.logging_page_id(info)
    print('logging page id\t\t\t', logging_page_id)
    return logging_page_id


def get_external_url(info):
    external_url = parser.external_url(info)
    print('external url\t\t\t', external_url)
    return external_url


def get_external_url_linkshimmed(info):
    external_url_linkshimmed= parser.external_url_linkshimmed(info)
    print('external url link shimmed\t\t\t', external_url_linkshimmed)
    return external_url_linkshimmed


def get_edge_mutual_followed_by_count(info):
    num_edge_mutual_followed_by = parser.edge_mutual_followed_by_count(info)
    print('num edge mutual followed by\t\t\t', num_edge_mutual_followed_by)
    return num_edge_mutual_followed_by


def get_edge_saved_media_count(info):
    num_edge_saved_media = parser.edge_saved_media_count(info)
    print('num edge saved media\t\t\t', num_edge_saved_media)
    return num_edge_saved_media


def get_edge_saved_media_has_next_page(info):
    edge_saved_media_has_next_page = parser.edge_saved_media_has_next_page(info)
    print('edge saved media has next page\t\t\t', edge_saved_media_has_next_page)
    return edge_saved_media_has_next_page


def get_edge_saved_media_end_cursor(info):
    edge_saved_media_end_cursor = parser.edge_saved_media_end_cursor(info)
    print('edge saved media end cursor\t\t\t', edge_saved_media_end_cursor)
    return edge_saved_media_end_cursor


def get_edge_media_collections_count(info):
    edge_media_collections_count = parser.edge_media_collections_count(info)
    print('edge media collections count\t\t\t', edge_media_collections_count)
    return edge_media_collections_count


def get_edge_media_collections_has_next_page(info):
    edge_media_collections_has_next_page = parser.edge_media_collections_has_next_page(info)
    print('edge media collections has next page\t\t\t', edge_media_collections_has_next_page)
    return edge_media_collections_has_next_page


def get_edge_media_collections_end_cursor(info):
    edge_media_collections_end_cursor = parser.edge_media_collections_end_cursor(info)
    print('edge media collections end cursor\t\t\t', edge_media_collections_end_cursor)
    return edge_media_collections_end_cursor


def get_toast_content_on_load(info):
    toast_content_on_load = parser.toast_content_on_load(info)
    print('toast content on load\t\t\t', toast_content_on_load)
    return toast_content_on_load


'''


# https://www.instagram.com/graphql/query/?query_id=17888483320059182&variables={"id": "234962686","first":20,"after":null}
'''


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
    print("post hashtag\t\t\t", post_hashtag)
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
    print("post tag\t\t\t", post_tag)
    return post_tag


''' comment get data '''


def get_comment_has_next_page(data):
    comment_has_next_page = comment_parser.comment_has_next_page(data)
    print("comment_has_next_page\t\t\t", comment_has_next_page)
    return comment_has_next_page


def get_comment_id(comment_list):
    comment_id = []
    comment_count = len(comment_parser.comment_post_edge_media_to_comment(comment_list))
    #comment_count = parser.post_comment_count(info, i)
    #print("num_com:\t\t\t",comment_count)
    #if comment_count > 20:
    #    comment_count = 20
    for i in range(0, comment_count):
        comment_id.append(comment_parser.comment_id(comment_list, i))
    print("comment id\t\t\t", comment_id)
    return comment_id


def get_comment_text(comment_list):
    comment_text = []
    comment_count = len(comment_parser.comment_post_edge_media_to_comment(comment_list))
    #print("num_com:\t\t\t",comment_count)
    #if comment_count > 20:
    #    comment_count = 20
    for i in range(0, comment_count):
        comment_text.append(comment_parser.comment_text(comment_list, i))
    print("comment text\t\t\t", comment_text)
    return comment_text


def get_comment_created_at(comment_list):
    comment_created_at = []
    comment_count = len(comment_parser.comment_post_edge_media_to_comment(comment_list))
    #print("num_com:\t\t\t", comment_count)
    # if comment_count > 20:
    #    comment_count = 20
    for i in range(0, comment_count):
        comment_created_at.append(comment_parser.comment_created_at(comment_list, i))
    print("comment created at\t\t\t", comment_created_at)
    return  comment_created_at


def get_comment_owner_id(comment_list):
    comment_owner_id = []
    comment_count = len(comment_parser.comment_post_edge_media_to_comment(comment_list))
    #print("num_com:\t\t\t", comment_count)
    # if comment_count > 20:
    #    comment_count = 20
    for i in range(0, comment_count):
        comment_owner_id.append(comment_parser.comment_owner_id(comment_list, i))
    print("comment owner id\t\t\t", comment_owner_id)
    return comment_owner_id


def get_comment_owner_username(comment_list):
    comment_owner_username = []
    comment_count = len(comment_parser.comment_post_edge_media_to_comment(comment_list))
    #print("num_com:\t\t\t", comment_count)
    # if comment_count > 20:
    #    comment_count = 20
    for i in range(0, comment_count):
        comment_owner_username.append(comment_parser.comment_owner_username(comment_list, i))
    print("comment owner username\t\t\t", comment_owner_username)
    return comment_owner_username


''' Found Comment tag'''

def comment_found_tag(comment_list):
    comment_tag = []
    comment_count = len(comment_parser.comment_post_edge_media_to_comment(comment_list))
    #print("num_com:\t\t\t", comment_count)
    # if comment_count > 20:
    #    comment_count = 20
    text = get_comment_text(comment_list)
    for i in range(0, comment_count):
        if text[i]:
            regex = r"@[^ @]+"
            matches = [match.group() for match in re.finditer(regex, text[i], re.MULTILINE)]
            comment_tag.append(matches)
        else:
            comment_tag.append("None")
    print("comment tag\t\t\t", comment_tag)
    return comment_tag


''' Found Comment tag'''

def comment_found_hashtag(comment_list):
    comment_hashtag = []
    comment_count = len(comment_parser.comment_post_edge_media_to_comment(comment_list))
    #print("num_com:\t\t\t", comment_count)
    # if comment_count > 20:
    #    comment_count = 20
    text = get_comment_text(comment_list)
    for i in range(0, comment_count):
        if text[i]:
            regex = r"#[^ #]+"
            matches = [match.group() for match in re.finditer(regex, text[i], re.MULTILINE)]
            comment_hashtag.append(matches)
        else:
            comment_hashtag.append("None")
    print("comment hashtag\t\t\t", comment_hashtag)
    return comment_hashtag

