from app import app
from app import start
from app import search_stat
from pymongo import MongoClient
import json
from bson import json_util
import time
import click
from datetime import date
from flask_cors import CORS
from bson import json_util
import requests

'''
    Open connection to mongodb, using "instadb" as database and "profiledb" as collection. Verify that you have
    correctly installed MongoDB and created the database and collection
'''
#client = MongoClient('mongodb://admin:admin@10.200.1.67/instadb', 27017)
client = MongoClient('localhost', 27017)
db = client['instadb']
collection_profile = db['profiledb']
collection_comment = db['commentdb']
current_date = date.today()

'''
    If false it doesn't send any requests and used pre-cached JSON
'''
flag = True

'''
    Whenever is sent a request to this server at the address '/s/<username>', hello function publishes into the queue
    the username provided. Then it queries the db asking for the relative json. Whenever that JSON has not yet been
    produced, it tries again after a few seconds.
'''
@app.route("/s/<username>")
def hello(username):
    query = {'username': username}
    '''
        At first, it searched for the JSON of the username and, if found, doesn't send any more requests
    '''
    try:
        context = list(collection_profile.find(query))[-1]
        profile_date = context['date_time']
        if current_date.strftime('%d') == profile_date.strftime('%d') \
                and profile_date.strftime('%m') == profile_date.strftime('%m'):
            js = json.dumps(context, indent=4, default=json_util.default)
            click.secho(
                "\n [route.py]\t\tA recently downloaded JSON was found, no further requests will be sent",
                fg="green",
            )
            search_stat.new_search(username)
            return js
        else:
            click.secho(
                "\n [route.py]\t\tThe cached JSON is too old, wait for the new JSON to be downloaded",
                fg="green",
            )
    except IndexError:
        click.secho(
                "\n [route.py]\t\tNo JSON were found for %s, started the download process..." % username,
                fg="green",
            )
    if flag:
        start.username_queue(username)
    else:
        click.secho(
            "\n [route.py]\t\tHTTP requests are disabled",
            fg="blue",
        )
    initial_spleep = 1
    while True:
        if initial_spleep == 8:
            click.secho(
                "\n [route.py]\t\tUser not found",
                fg="green",
            )
            return "Username not found", 404
        try:
            '''
                If the JSON is found, is extracted from the database using the query and serialized as a string, in
                order to be passed as HTTP response. Note that, at this point, we don't put any requirements on which
                version of the JSON take, since each profile can be requested several times. To-Do: modify the query
                and ask for the json of the username, for which the date is the latest
            '''
            print("\n [*] Read from database...")
            context_list = list(collection_profile.find(query))
            context = context_list[-1]
            print(" [*] JSONs found ", len(context_list))
            profile_date = context['date_time']
            '''
                The JSON is used only if it's recent, i.e. downloaded the same day, otherwise you are still looking for
            '''
            if current_date.strftime('%d') == profile_date.strftime('%d') \
                    and current_date.strftime('%m') == profile_date.strftime('%m'):
                js = json.dumps(context, indent=4, default=json_util.default)
                '''
                    Who is returned to? 1) Backend of Django, to rendering the HTML page; 2) Internal API, if you only
                    ask for the JSON after directly connected to this server at this address

                    AGGIUNGERE AL CONTEXT TOP SEARCH
                '''
                return js
            click.secho(
                "\n [route.py]\t\tThe found JSON is too old, wait for the new JSON to be downloaded",
                fg="green",
            )
            print("\n\n", initial_spleep, '\n\n')
            click.secho(
                "\n [date   ►]\t\t"+current_date.strftime('%d')+'\\'+current_date.strftime('%m')+'\\'
                + current_date.strftime('%y') +
                "\n [date   ◄]\t\t"+profile_date.strftime('%d')+'\\'+profile_date.strftime('%m')+'\\'
                + profile_date.strftime('%y'),
                fg="blue",
            )
            time.sleep(initial_spleep)
        except IndexError:
            '''
            Each time the JSON is not found, it stops for a number of seconds equal to "initial_second" and tries again.
            Then "initial_second" is doubled. This procedure lasts until the sleep time is small enough (=4s).
            Why? Because we need some kind of mechanism that alerts us whenever db changes, like trigger event, however
            community version does not support it. If you have a better idea, change it!
            '''
            click.secho(
                "\n [route.py]\t\tUser not yet found, try again in %s" % str(initial_spleep),
                fg="green",
            )
            time.sleep(initial_spleep)
            initial_spleep *= 2


'''
    For AJAX, return the comment of a given post
'''

CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/a/<shortcode>', methods=['POST'])
def post_javascript_data(shortcode):
    query = {'shortcode': shortcode}
    context = list(collection_comment.find(query))[0]
    json_comment = json.dumps(context, indent=4, default=json_util.default)    # json containing the comment list
    # make a HTTP request to parser-process and ask for sentiment analysis. r contains the response code, while r.content contians the final json
    r = requests.post('http://127.0.0.1:5002/sentiment', data = json_comment)
    sentiment_json = r.content
    print(sentiment_json)
    return sentiment_json

'''
    Return an 404 error code if the path does not match with any functions above
'''
@app.errorhandler(404)
def page_not_found(error):
    return "Requested page is not available, contact the site administrator", 404
