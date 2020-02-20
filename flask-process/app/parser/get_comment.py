from app.parser import profiling
from app.parser import json_parser as parser
from app.parser import json_comment_parser as comment_parser
from datetime import datetime
import pytz


def get_comment_data(comment):
    comment_has_next_page = profiling.get_comment_has_next_page(comment)
    list_comment_id = profiling.get_comment_id(comment)
    comment_text = profiling.get_comment_text(comment)
    comment_created_at = profiling.get_comment_created_at(comment)
    comment_owner_id = profiling.get_comment_owner_id(comment)
    comment_owner_username = profiling.get_comment_owner_username(comment)
    comment_found_tag = profiling.comment_found_tag(comment)
    comment_found_hashtag = profiling.comment_found_hashtag(comment)

    context_comment = {
        'date_time': datetime.utcnow(),
        #'date_time': datetime.now(tz=pytz.timezone('Europe/Rome')),
        'comment_has_next_page': comment_has_next_page,
        'list_comment_id': list_comment_id,
        'comment_text': comment_text,
        'comment_created_at': comment_created_at,
        'comment_owner_id': comment_owner_id,
        'comment_owner_username': comment_owner_username,
        'comment_found_tag': comment_found_tag,
        'comment_found_hashtag': comment_found_hashtag
    }
    return context_comment