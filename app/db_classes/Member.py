from app import db

class Member(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    new_message_count = db.Column(db.Integer, unique=False, nullable=True)
    last_readed_message = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'), nullable=False)

    def __init__(self, chat_id, user_id):
        self.chat_id = chat_id
        self.user_id = user_id