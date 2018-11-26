from flask import *
from app import app, jsonrpc
import json
from .database import Database
from .model import DbModel

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


@app.route("/api/search_users/", methods=["GET"])
def search_users():

    args = request.args.to_dict()
    query = str(args['query'])
    limit = int(args['limit'])

    resp = jsonify({"users": Database().get_users})

    resp.content_type = 'application/json'
    resp.status_code = 200

    return resp


@app.route("/api/search_chats/", methods=["GET"])
def search_chats():

    args = request.args.to_dict()
    query = str(args['query'])
    limit = int(args['limit'])

    resp = jsonify({"chats": Database().get_chats})
    resp.content_type = 'application/json'
    resp.headers['status_code'] = 200

    return resp



@app.route("/api/list_chats/", methods=["GET"])
def list_chats():

    resp = jsonify({"chats": Database().get_chats})
    resp.content_type = 'application/json'
    resp.headers['status_code'] = 200

    return resp


@app.route("/api/create_pers_chat/", methods=["POST"])
def create_pers_chat():
    user_id = int(request.args.get('user_id'))

    resp = jsonify({'chat': Database().create_chat(user_id)})
    resp.status_code = 200
    resp.content_type = 'application/json'

    return resp


@app.route("/api/create_group_chat/", methods=["POST"])
def create_group_chat():
    topic = str(request.args.get('topic'))
    Database().create_group_chat(topic)
    resp = jsonify({})
    resp.status_code = 200
    resp.content_type = 'application/json'

    return resp


@app.route("/api/add_members_to_group_chat/", methods=["POST"])
def add_members_to_group_chat():
    chat_id = int(request.args.get('chat_id'))
    user_ids = [int(i) for i in request.args.getlist('user_ids')]

    Database().add_members_to_group_chat(chat_id, user_ids)
    resp = jsonify({})
    resp.status_code = 200
    resp.content_type = 'application/json'

    return resp


@app.route("/api/leave_group_chat/", methods=["POST"])
def leave_group_chat():
    chat_id = int(request.args.get('chat_id'))
    #Database
    resp = jsonify({})
    resp.status_code = 200
    resp.content_type = 'application/json'

    return resp


@app.route("/api/send_message/", methods=["POST"])
def send_message():
    args = request.args.to_dict()
    chat_id = int(args['chat_id'])
    content = str(args['content'])
    attach_id = int(args['attach_id'])

    resp = jsonify({'message': Database().message1})
    resp.status_code = 200
    resp.content_type = 'application/json'

    return resp


@app.route("/api/read_message/", methods=["GET"])
def read_message():
    message_id = int(request.args.get('message_id'))
    resp = jsonify({'chat': Database().chat1})
    resp.status_code = 200
    resp.content_type = 'application/json'

    return resp


@app.route("/api/upload_file/", methods=["POST"])
def upload_file():
    args = request.args.to_dict()
    chat_id = args['chat_id']
    content = args['content']

    resp = jsonify({'attach': Database().attachment1})
    resp.status_code = 200
    resp.content_type = 'application/json'

    return resp
