class Database:
    def __init__(self):
        self.user1 = {
            "user_id": 19,
            "nick": "the.good",
            "name": "Clint Eastwood",
            "avatar": "avatars/d9099cd0d3e6cb47fe3a9b0e631901fa.png"
        }
        self.user2 = {
            "user_id": 13,
            "nick": "the.good.inc",
            "name": "FeelGood Inc",
            "avatar": "avatars/d9099cd0d3e6cb47fe3a9b0e631901fa.png"
        }

        self.chat1 = {
            "chat_id": 33,
            "is_group_chat": False,
            "topic": "Chuck Norris",
            "last_message": "argh!",
            "new_messages": 30,
            "last_read_message_id": 214
        }
        self.chat2 = {
            "chat_id": 50,
            "is_group_chat": True,
            "topic": "Broxigar Saurfang",
            "last_message": "axe!",
            "new_messages": 130,
            "last_read_message_id": 2147
        }

        self.message1 = {
            "message_id": 200,
            "chat_id": 33,
            "user_id": 22,
            "content": "Hmmm, @chuck.norris",
            "added_at": 1540198594
        }

        self.attachment1 = {
            "attach_id": 1,
            "message_id": 200,
            "chat_id": 33,
            "user_id": 22,
            "type": "image",
            "url": "attach/e7ed63c5f815d5b308c9a3720dd1949d.png"
        }


    @property
    def get_users(self):
        return [self.user1, self.user2]

    @property
    def get_chats(self):
        return [self.chat1, self.chat2]

    def create_chat(self, id_):
        return self.chat1

    def create_group_chat(self, topic):
        return self.chat2

    def add_members_to_group_chat(self, id_, ids):
        pass