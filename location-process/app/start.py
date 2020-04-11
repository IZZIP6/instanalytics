import pika
import time
import json
from flaskext.mysql import MySQL
from app import app
import click
from pymysql import cursors

'''
    da commentare :)
'''
#mysql mysql = MySQL(cursorclass=cursors.DictCursor)

# app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'instadb'
app.config['MYSQL_DATABASE_PASSWORD'] = ''

mysql.init_app(app)

flag = True


def locations(data):
    location = data['graphql']['user']['edge_owner_to_timeline_media']['edges']
    if location is not None:
        return location

def new_location(id, location):
    print("PD")
    location = location.replace("'", " ")
    select_query = "SELECT id FROM analytics_location"
    cur = mysql.get_db().cursor()
    cur.execute(select_query)
    # mysql.get_db().commit()
    results = cur.fetchall()
    if id in str(results):
        if flag:
            click.secho(
                " [*] %s already in" % location,
                fg="green",
            )
    else:
        insert_query = "INSERT INTO analytics_location(id, name) VALUES ('%s', '%s')" % (id, location)
        cur.execute(insert_query)
        mysql.get_db().commit()

        if flag:
            click.secho(
                " [*] %s inserted" % location,
                fg="green",
            )
    cur.close()



def query():
    select_query = "SELECT * FROM instadb.analytics_location;"
    insert_query = "INSERT INTO analytics_location(id, name) VALUES ('%s', '%s')" % (25, "ciao")
    cur = mysql.get_db().cursor()

    cur.execute(insert_query)
    mysql.get_db().commit()
    cur.execute(select_query)
    #cur.close()
    results = cur.fetchall()
    print(" [*] RESULT")
    print(results)
    cur.close()
