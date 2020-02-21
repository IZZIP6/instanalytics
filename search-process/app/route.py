from app import app
from app import start
from pymongo import MongoClient
import json
from bson import json_util
import time

client = MongoClient('localhost', 27017)
db = client['instadb']
collection_profile = db['profiledb']



@app.route("/s/<username>")                   # at the end point /
def hello(username):                      # call method hello
    start.username_queue(username)
    query = {'username':username}
    initial_spleep = 1

    while True:
        if initial_spleep == 8:
            return "Username non trovato"
        try:
            print("Lettura da mongo...")
            contex = list(collection_profile.find(query))[0]
            js = json.dumps(contex, indent=4, default=json_util.default)
            print("TROVATO")
            return js
        except IndexError:
            print("Non trovato, riprovo tra %ss" %str(initial_spleep))
            time.sleep(initial_spleep)
            initial_spleep*=2

    #print(contex)
    #while is not None
    #js = json.dumps(context, indent=4, default=json_util.default)
    #return js

@app.errorhandler(404)
def page_not_found(error):
    return "niente di niente", 404