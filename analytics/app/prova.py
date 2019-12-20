import json
from analytics.app.src import endpoint
from analytics.app.src.request_handler import send_requests
from analytics.app.src.request_handler import request_adapter as rq
from analytics.profiles import dir
import os
from analytics.app.src.parser import profiling, get_profile

def insert_username(username):
    profile_name = username
    profile_name.replace(" ", "")
    url = endpoint.request_account_info(profile_name)
    if send_requests.is_requested:
        rq.user_request(url, profile_name)
        print("Send request ...")
    return load_json(username)

def load_json(username):
    try:
        last = os.listdir(dir.abs_path + '\\' + username +  '\\' + "profile")[-1]
        with open(dir.abs_path + '\\' + username +  '\\' + "profile\\" + last + '\\' + username + '.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError as e:
        print("EXCEPTION")
        print(e)
    context = get_profile.get_user_data(data)
    return context


# https://www.instagram.com/p/B6LZ6-4IRj0/?__a=1&max_id=QVFBeXlIZnc2ampsaDVPb0Z0YWRLU1hjLXJpZGF3Zl9rWW9UOEtXdTdZNklYLWd5WFVBQmw3akhXdmVoNE44U1ljdjBYVFVJSm9tY3ZqRW45QXEzMXBOTg==
