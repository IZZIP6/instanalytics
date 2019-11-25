# Instanalytics
![GitHub Logo](analytics/static/img/logo.png)

# Set up
###### Django
1. Install Django: `pip install Django==2.2.7` (if `pip version==19.3.1` use `python -m pip install Django==2.2.7`)
2. Add to PATH `django-admin.py`.
###### MySQL
1. Install mysql driver: `pip install django-mysql`
2. Install mysql client: `pip install mysqlclient`
3. Run mysql
4. Database settings: 
    * create new user (`NAME = <username>`) with `ALL PRIVILEGES` and `NO PASSWORD`
    * create a new database (`NAME = <dbname>`)
5. edit [setting.py](instanalytics/settings.py)
    * `USER: <username>`
    * `NAME: <dbname>`
6. `python manage.py makemigrations`
7. `python manage.py migrate`
# Test it

Go to [127.0.0.1:8000](https://127.0.0.0.1:8000) and digit the username of Instagram account.
- Offline analysis  : set `is_requested = False` in [send_request](./analytics/app/src/request_handler/send_requests.py) and choose one of the available [profiles](analytics/profiles)
- Online analysis   : set `is_requested = True`


```
Becareful, don't make too many requests
```
