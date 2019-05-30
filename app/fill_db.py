from app import *

def fill_user():
    print("fill user")
    for i in range(0, 10):
        user = User(f"user{i}", f"user{i}")
        db.session.add(user)
        db.session.commit()

def fill_chat():
    print("fill chat")
    for i in range(0, 10):
        chat = Chat(f"chat{i}", False)
        db.session.add(chat)
    db.session.commit()

    for i in range(1, 11):
        member1 = Member(i, i)
        member2 = Member(i+1 if i < 10 else 1, i)
        db.session.add(member1)
        db.session.add(member2)

    db.session.commit()

def fill_message():
    print("fill message")
    for i in range(1, 11):
        j = i+1 if i < 10 else 1
        message = Message(f"text_user{i}_chat{j}", i, j)
        message1 = Message(f"text_user{i}_chat{i}", i, i)
        db.session.add(message)
        db.session.add(message1)
    db.session.commit()

def fill_attachment():
    print("fill attachment")
    for i in range(1, 21):
        j = ((i+1)//2 + 1)
        if j > 10:
            j = 1
        att = Attachment(f"att{i}", i, i//2 if i % 2 == 0 else j)
        db.session.add(att)
    db.session.commit()