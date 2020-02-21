from app.parser import profiling
from datetime import datetime

def get_user_data(info):
    username = profiling.get_username(info)
    fullname = profiling.get_fullname(info)
    id = profiling.get_idnumber(info)
    verified = profiling.get_verified(info)
    bio = profiling.get_bio(info)
    if bio == "":
        bio = "No-Biography"
    no_followers = profiling.get_followers(info)
    no_following = profiling.get_following(info)
    business = profiling.get_business(info)
    private = profiling.get_private(info)
    no_posts = profiling.get_post_number(info)
    url = profiling.get_profile_pic(info)
    cursor = ''
    #profiling.get_show_suggested_profiles(info)
    blocked_by_viewer = profiling.get_blocked_by_viewer(info)
    country_block = profiling.get_country_block(info)
    followed_by_viewer = profiling.get_followed_by_viewer(info)
    follows_viewer = profiling.get_follows_viewer(info)
    has_channel = profiling.get_has_channel(info)
    has_blocked_viewer = profiling.get_has_blocked_viewer(info)
    has_requested_viewer = profiling.get_has_requested_viewer(info)
    joined_recently = profiling.get_is_joined_recently(info)
    requested_by_viewer = profiling.get_requested_by_viewer(info)
    connected_fb_page = profiling.get_connected_fb_page(info)
    n_highlight_reel = profiling.get_highlight_reel_count(info)
    logging_page_id = profiling.get_logging_page_id(info)
    external_url = profiling.get_external_url(info)
    external_url_linkshimmed = profiling.get_external_url_linkshimmed(info)
    num_edge_mutual_followed_by = profiling.get_edge_mutual_followed_by_count(info)
    num_edge_saved_media = profiling.get_edge_saved_media_count(info)
    edge_saved_media_has_next_page = profiling.get_edge_saved_media_has_next_page(info)
    edge_saved_media_end_cursor = profiling.get_edge_saved_media_end_cursor(info)
    edge_media_collections_count = profiling.get_edge_media_collections_count(info)
    edge_media_collections_has_next_page = profiling.get_edge_media_collections_has_next_page(info)
    edge_media_collections_end_cursor = profiling.get_edge_media_collections_end_cursor(info)
    toast_content_on_load = profiling.get_toast_content_on_load(info)
    if private is False:
        list_of_shortcode, list_of_url = profiling.get_shortcode_list(info)
        post_type_name, post_id, post_comment_count, post_comments_disabled, \
        post_taken_at_timestamp, post_dimensions_height, post_dimensions_width = profiling.get_post_data1(info)
        post_edge_media_to_caption = profiling.get_post_edge_media_to_caption(info)
        post_edge_media_to_caption_text = []
        for i in range(0, len(post_edge_media_to_caption)):
            if not post_edge_media_to_caption[i]:
                post_edge_media_to_caption_text.append("Null")
            else:
                post_edge_media_to_caption_text.append(profiling.get_post_edge_media_to_caption_text(info, i))
        post_location = profiling.get_post_location(info)
        post_location_id = []
        post_location_has_public_page = []
        post_location_name = []
        post_location_slug = []
        for i in range(0, len(post_location)):
            if post_location[i] is None:
                post_location_id.append("Null")
                post_location_has_public_page.append("Null")
                post_location_name.append("Null")
                post_location_slug.append("Null")
            else:
                post_location_id.append(profiling.get_post_location_id(info, i))
                post_location_has_public_page.append(profiling.get_post_location_has_public_page(info, i))
                post_location_name.append(profiling.get_post_location_name(info, i))
                post_location_slug.append(profiling.get_post_location_slug(info, i))
        is_video = profiling.get_post_is_video(info)
        video_view_count = []
        post_accessibility = []
        for i in range(0, len(is_video)):
            if is_video[i]:
                video_view_count.append(profiling.get_post_video_view_count(info, i))
            else:
                video_view_count.append("Null")
                post_accessibility.append(profiling.get_post_accessibility(info, i))
        post_num_like, post_preview_num_like = profiling.get_post_like(info)
        post_owner_id, post_owner_username = profiling.get_post_owner(info)
        post_media_preview = []
        post_preview = profiling.get_post_number(info)
        if post_preview > 12:
            post_preview = 12
        for i in range(0, post_preview):
            post_media_preview.append(profiling.get_post_media_preview(info, i))
        post_gating_info, post_fact_check_overall_rating, post_fact_check_information = profiling.get_post_data2(info)
        post_hashtag = profiling.post_found_hashtag(info)
        post_tag = profiling.post_found_tag(info)

    context = {
        'date_time': datetime.utcnow(),
        #'date_time': datetime.now(tz=pytz.timezone('Europe/Rome')),
        'username': username,
        'fullname': fullname,
        'id': id,
        'url': url,
        'bio': bio,
        'n_followers': no_followers,
        'n_following': no_following,
        'n_post': no_posts,
        'cursor': cursor,
        'verified': verified,
        'business': business,
        'private': private,
        'blocked_by_viewer': blocked_by_viewer,
        'country_block': country_block,
        'followed_by_viewer': followed_by_viewer,
        'follows_viewer': follows_viewer,
        'has_channel': has_channel,
        'has_blocked_viewer': has_blocked_viewer,
        'has_requested_viewer': has_requested_viewer,
        'joined_recently': joined_recently,
        'requested_by_viewer': requested_by_viewer,
        'connected_fb_page': connected_fb_page,
    }
    return context