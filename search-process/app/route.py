from app import app
from app import start
from pymongo import MongoClient
import json
from bson import json_util
import time

'''
    Open connection to mongodb, using "instadb" as database and "profiledb" as collection. Verify that you have 
    correctly installed MongoDB and created the database and collection
'''
client = MongoClient('localhost', 27017)
db = client['instadb']
collection_profile = db['profiledb']


'''
    Whenever is sent a request to this server at the address '/s/<username>', hello function publishes into the queue 
    the username provided. Then it queries the db asking for the relative json. Whenever that JSON has not yet been 
    produced, it tries again after a few seconds. 
'''
@app.route("/s/<username>")
def hello(username):

    '''
    Comment on this statement if you don't want to send requests every time, and use only the JSON currently contained
    into the database
    '''

#   start.username_queue(username)
    query = {'username': username}
    initial_spleep = 1

    while True:
        if initial_spleep == 8:
            return "Username not found", 404
        try:
            '''
                If the JSON is found, is extracted from the database using the query and serialized as a string, in
                order to be passed as HTTP response. Note that, at this point, we don't put any requirements on which 
                version of the JSON take, since each profile can be requested several times. To-Do: modify the query
                and ask for the json of the username, for which the date is the latest 
            '''
            print("Read from database...")
            contex = list(collection_profile.find(query))[0]
            js = json.dumps(contex, indent=4, default=json_util.default)
            print("It works!")
            '''
                Who is returned to? 1) Backend of Django, to rendering the HTML page; 2) Internal API if you only ask
                for the JSON after directly connected to this server at this address
            '''
            return js
        except IndexError:
            '''
            Each time the JSON is not found, it stops for a number of seconds equal to "initial_second" and tries again.
            Then "initial_second" is doubled. This procedure lasts until the sleep time is small enough (=4s).
            Why? Because we need some kind of mechanism that alerts us whenever db changes, like trigger event, however 
            community version does not support it. If you have a better idea, change it!
            '''
            print("Not found yet,  try again in %ss" % str(initial_spleep))
            time.sleep(initial_spleep)
            initial_spleep *= 2


'''
    Return an 404 error code if the path does not match with any functions above
'''
@app.errorhandler(404)
def page_not_found(error):
    return "Requested page is not available, contact the site administrator", 404