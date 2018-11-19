from flask import Flask
from .instance.config import *

from flask_jsonrpc import JSONRPC

app = Flask(__name__)
app.config.from_object(TestConfig)

jsonrpc = JSONRPC(app, '/api/')

from . import views
