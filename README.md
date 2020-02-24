# Instanalytics
![GitHub Logo](analytics/static/img/logo.png)

#### Requirements 
All the required packages are contained in the [requirements.py](instanalytics/requirements.txt) file. Run `pip install -r requirements.txt`


###### MySQL
1. Run mysql
2. Database settings: 
    * create new user (`NAME = <name>`) with `ALL PRIVILEGES` and `NO PASSWORD`
    * create a new database (`NAME = <dbname>`)
3. edit [setting.py](instanalytics/settings.py)
    * `USER: <username>`
    * `NAME: <dbname>`
4. `python manage.py makemigrations`
5. `python manage.py migrate`

Note that, every time you apply a change to the database, you have to run 4. and 5. commands again.

###### MongoDB
1. Create database `instadb`
2. Create collections `profiledb`, ...
###### RabbitMQ
1. Install RabbitMQ using [github official release](https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.8.2/rabbitmq-server-3.8.2.exe)
```
Check if all services are working!
```

## Run the application

Start the following services
1. `python manage.py runserver 0.0.0.0:8000` in [django-intro](instanalytics/django-intro)
2. `python search-process.py` in [search-process](instanalytics/search-process)
3. `python todo-flask.py` in [todo-flask](instanalytics/todo-flask)
4. `python flask-process.py` in [flask-process](instanalytics/flask-process)

Go to [localhost](http://127.0.0.1:8000). 

You can also use a different host (within the same network) than localhost to connect to your site, in which case you need to specify the IP address of the machine where your services are running.
```
Becareful, don't make too many requests
```

### Issues
1. User not found: check if `flag = True` in [search-process](instanalytics/search-process/app/route.py)
2. `pika.exceptions.StreamLostError`: make sure RabbitMQ service is running