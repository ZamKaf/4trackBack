from flask import *
from wtforms_alchemy import ModelForm
from flask_restless import APIManager
from app import app, db, jsonrpc
import json
from .database import Database
from .model import DbModel

from .db_classes import *


class UserForm(ModelForm):
    class Meta:
        model = User


manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(User)
manager.create_api(Chat)
manager.create_api(Attachment)


@app.route("/<string:name>")
@app.route("/")
def index(name = "world"):
    return f"Hello, {name}!"


@jsonrpc.method('print_name')
def foo():
    #return json.dumps("[' Hello' ]")
    return {"name": "Ivan"}
#curl -i -X POST -H "Content-type: application/json" --data='{ "jsonrpc": "2.0", "method": "print_name", "params":[], "id": "1"}' http://127.0.0.1:5000/api/

@app.route("/login/", methods=["GET", "POST"])
def login():
    model = DbModel()
    print(model.create_chat(1,2))
    # OAuth2
    resp = jsonify({})
    resp.status_code = 200
    resp.content_type = 'application/json'

    return resp


@app.route("/api/create_user/", methods=["POST"])
def create_user():
    print("create_user")
    user = User("", "")
    form = UserForm(request.form)
    resp = jsonify({})
    resp.content_type = 'application/json'
    if not form.validate():
        resp = jsonify({})
        resp.status_code = 400
        return resp

    form.populate_obj(user)
    print(f'user name {user.name}')

    db.session.add(user)
    db.session.commit()

    resp = jsonify({})
    resp.status_code = 200

    return resp


@app.route("/api/delete_user/", methods=["POST"])
def delete_user():
    print(f"delete_user")
    nickname = request.form['nick']

    resp = jsonify({})
    resp.content_type = 'application/json'
    user = User.query.filter(User.nick == nickname).first()
    print(user.nick)
    db.session.delete(user)
    db.session.commit()

    resp = jsonify({})
    resp.status_code = 200

    return resp


@app.route("/api/list_chats/", methods=["GET"])
def list_chats():

    resp = jsonify({"chats": Database().get_chats})
    resp.content_type = 'application/json'
    resp.headers['status_code'] = 200

    return resp


@app.route("/api/create_pers_chat/", methods=["POST"])
def create_pers_chat():
    args = request.form
    user_id1 = args['user_id1']
    user_id2 = args['user_id2']
    topic = f"{user_id1}_{user_id2}"
    chat = Chat(topic, False)
    db.session.add(chat)
    db.session.commit()

    mem1 = Member(chat.id, user_id1)
    mem2 = Member(chat.id, user_id2)
    db.session.add(mem1)
    db.session.add(mem2)
    db.session.commit()

    resp = jsonify({"chats": Database().get_chats})
    resp.status_code = 200
    resp.content_type = 'application/json'

    return resp


@app.route("/api/create_group_chat/", methods=["POST"])
def create_group_chat():
    args = request.form
    user_ids = args['user_ids']
    topic = args['topic']
    chat = Chat(topic, False)
    db.session.add(chat)
    db.session.commit()

    for user_id in user_ids:
        mem = Member(chat.id, user_id)
        db.session.add(mem)

    db.session.commit()

    resp = jsonify({})
    resp.status_code = 200
    resp.content_type = 'application/json'

    return resp


@app.route("/api/add_members_to_group_chat/", methods=["POST"])
def add_members_to_group_chat():
    args = request.form
    user_id = args['user_id']
    chat_id = args['chat_id']

    mem = Member(chat_id, user_id)
    db.session.add(mem)
    db.session.commit()

    resp = jsonify({})
    resp.status_code = 200
    resp.content_type = 'application/json'

    return resp


@app.route("/api/leave_group_chat/", methods=["POST"])
def leave_group_chat():
    args = request.form
    user_id = args['user_id']
    chat_id = args['chat_id']
    member = Member.query.filter(Member.chat_id == chat_id, Member.user_id == user_id).first()
    db.session.delete(member)
    db.session.commit()

    resp = jsonify({})
    resp.status_code = 200
    resp.content_type = 'application/json'

    return resp


@app.route("/api/send_message/", methods=["POST"])
def send_message():
    args = request.form
    content = args['content']
    chat_id = args['chat_id']
    user_id = args['user_id']
    msg = Message(content, user_id, chat_id)
    db.session.add(msg)
    db.session.commit()

    resp = jsonify({'message': Database().message1})
    resp.status_code = 200
    resp.content_type = 'application/json'

    return resp


@app.route("/api/read_message/", methods=["GET"])
def read_message():
    args = request.form
    chat_id = args['chat_id']
    user_id = args['user_id']
    message_id = args['message_id']
    member = Member.query.filter(Member.chat_id == chat_id, Member.user_id == user_id).first()
    member.last_readed_message = message_id
    db.session.commit()

    resp = jsonify({'chat': Database().chat1})
    resp.status_code = 200
    resp.content_type = 'application/json'

    return resp


@app.route("/api/upload_file/", methods=["POST"])
def upload_file():
    print('upload_file')
    args = request.form
    chat_id = args['chat_id']
    user_id = args['user_id']
    url = args['url']

    msg = Message("", user_id, chat_id)
    db.session.add(msg)
    db.session.commit()
    att = Attachment(url, msg.id, chat_id)
    db.session.add(att)
    db.session.commit()

    resp = jsonify({})
    resp.status_code = 200
    resp.content_type = 'application/json'

    return resp
