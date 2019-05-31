from flask import Flask

from .instance.config import *

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_jsonrpc import JSONRPC

app = Flask(__name__)
app.config.from_object(TestConfig)
app.config['SQLALCHEMY_DATABASE_URI'] = TestConfig.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
jsonrpc = JSONRPC(app, '/api/')

from .db_classes import *

'''
class Attachment(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    type = db.Column(db.String(90), unique=False, nullable=True)
    url = db.Column(db.String(90), unique=True, nullable=True)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'), nullable=False)


    def __init__(self, url, message_id, chat_id):
        self.url = url
        self.message_id = message_id
        self.chat_id = chat_id


class Chat(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    topic = db.Column(db.String(90), unique=False, nullable=True)
    is_group_chat = db.Column(db.Boolean, unique=False, nullable=False)
    last_message = db.Column(db.String(90), unique=False, nullable=True)
    messages = db.relationship('Message', backref='chat', lazy=True)
    attachments = db.relationship('Attachment', backref='chat', lazy=True)


    def __init__(self, topic, is_group_chat):
        self.topic = topic
        self.is_group_chat = is_group_chat


class Member(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    new_message_count = db.Column(db.Integer, unique=False, nullable=True)
    last_readed_message = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'), nullable=False)

    def __init__(self, chat_id, user_id):
        self.chat_id = chat_id
        self.user_id = user_id


class Message(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    content = db.Column(db.String(90), unique=False, nullable=True)
    added_at = db.Column(db.Date, unique=False, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'), nullable=False)
    members = db.relationship('Member', backref='message', lazy=True)
    attachments = db.relationship('Attachment', backref='message', lazy=True)


    def __init__(self, content, user_id, chat_id):
        self.content = content
        self.user_id = user_id
        self.chat_id = chat_id


class User(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(90), unique=False, nullable=False)
    nick = db.Column(db.String(90), unique=True, nullable=False)
    avatar= db.Column(db.String(90), unique=False, nullable=True)
    messages = db.relationship('Message', backref='user', lazy=True)
    members = db.relationship('Member', backref='user', lazy=True)


    def __init__(self, nick, name):
        self.nick = nick
        self.name = name
'''

from . import views