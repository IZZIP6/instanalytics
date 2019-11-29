import json
from analytics.app.src import endpoint
from analytics.app.src.request_handler import send_requests
from analytics.app.src.request_handler import request as rq
from analytics.profiles import dir
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
        with open(dir.abs_path + '\\' + username + '\\' + username + '.json', 'r') as file:
            data = json.load(file)
            context = get_profile.get_user_data(data)
    except FileNotFoundError as e:
        print(e)
    return context



