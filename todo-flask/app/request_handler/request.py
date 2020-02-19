import json

# CHECK INTERNET AVAILABILITY

def make_request(session, url):
    r = session.get(url)
    print(r.status_code)
    jpost = r.json()
    return jpost