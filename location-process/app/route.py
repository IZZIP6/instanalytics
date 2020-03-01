from app import app
from app import start
from flaskext.mysql import MySQL

mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'instadb'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
print(" [*] START CONFIG")

mysql.init_app(app)

@app.route("/")
def hello():
    print(" [*] PROVA ROUTE")
    cur = mysql.connect().cursor()
    start.location_queue(cur)
