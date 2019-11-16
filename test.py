import os
import json
from server.parser import profiling
from server.request_handler import request as rq
from server.request_handler import send_requests
import server.endpoint as endpoint


def open_json():
    try:
        with open('./server/profiles/'+profile_name+'/'+profile_name+'.json', 'r') as json_file:
            data = json.load(json_file)
            profiling.get_user_data(data)
    except FileNotFoundError as e:
        print(e)
        ls = os.listdir('./server/profiles/')
        print('[Available profiles]')
        for item in ls:
            print(item)


profile_name = input("Enter Instagram username you want to analyze:\t")
profile_name.replace(" ", "")
url = endpoint.request_account_info(profile_name)
if send_requests.is_requested:
    rq.user_request(url, './server/profiles/'+profile_name+'/'+profile_name+'.json')
open_json()

