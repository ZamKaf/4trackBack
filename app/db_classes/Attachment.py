from app import db

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