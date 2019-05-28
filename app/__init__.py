from flask import Flask
from .instance.config import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_jsonrpc import JSONRPC

app = Flask(__name__)
app.config.from_object(TestConfig)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://trackback:trackback@192.168.33.136/tt1'
db = SQLAlchemy(app)
jsonrpc = JSONRPC(app, '/api/')

from . import views


class Person(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    username = db.Column(db.String(90), unique=True, nullable=False)

    def __init__(self, username):
        self.username = username