from app import db


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
