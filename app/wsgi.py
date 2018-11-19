import pprint
import json
import datetime


def app(environ, start_response):
    time = str(datetime.datetime.now().time())
    info = json.dumps(
        {"time": time, "url": environ["HTTP_HOST"] }
    )
    start_response('200 OK', [('content-type', 'application/json')])
    return [info.encode('utf-8')]


#gunicorn --threads 20 --access-logfile - wsgi:app
