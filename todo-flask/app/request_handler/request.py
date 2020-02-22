'''
    This is the core of the requests module, given a session and the url it sends an HTTP get request to the API and
    returns the json
'''


def make_request(session, url):
    r = session.get(url)
    print(r.status_code)
    jpost = r.json()
    return jpost