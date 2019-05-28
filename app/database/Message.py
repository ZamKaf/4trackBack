from app import db

class Message(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    content = db.Column(db.String(90), unique=False, nullable=True)
    added_at = db.Column(db.Date, unique=False, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'), nullable=False)
    members = db.relationship('Member', backref='message', lazy=True)
    attachments = db.relationship('Attachment', backref='message', lazy=True)


    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id