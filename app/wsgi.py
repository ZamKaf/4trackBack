import pprint
import json
import datetime


def app(environ, start_response):
    time = str(datetime.datetime.now().time())
    info = json.dumps(
        {"data": {"time": time, "url": environ["HTTP_HOST"].encode("utf-8")},
         "content-type": "application/json"}
    )
    start_response('200 OK', [('content-type', 'application/json')])
    return [info]
