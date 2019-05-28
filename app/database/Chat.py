from app import db

class Chat(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(90), unique=False, nullable=False)
    nick = db.Column(db.String(90), unique=True, nullable=False)
    avatar= db.Column(db.String(90), unique=False, nullable=True)


    def __init__(self, nick, name):
        self.nick = nick
        self.name = name