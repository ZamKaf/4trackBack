from app import db

class Attachment(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    type = db.Column(db.String(90), unique=False, nullable=False)
    url = db.Column(db.String(90), unique=True, nullable=False)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'), nullable=False)


    def __init__(self, topic, is_group_chat):
        self.topic = topic
        self.is_group_chat = is_group_chat