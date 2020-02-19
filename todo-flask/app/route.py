from app import app
from app import start


@app.route("/s/<username>")                   # at the end point /
def hello(username):                      # call method hello
    start.request_to_username(username)
    return "Hello World!"         # which returns "hello world"

@app.errorhandler(404)
def page_not_found(error):
    return "niente di niente", 404