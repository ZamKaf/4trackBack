from app.database import Database
import datetime


class DbModel:
    def __init__(self):
        self.db = Database()

    def get_chat_ids(self, user_id):
        ids = []
        chats_where_member = self.db.query_all("""
            SELECT 'ChatId' FROM public."Members"
            WHERE 'UserId' = '%(user_id)s'
            """, user_id=int(user_id))

        for key, value in chats_where_member.items():
            ids.append(value['ChatId'])

        return ids

    def list_chats(self, user_id, limit=10):
        chats = {}
        ids = self.get_chat_ids(user_id)

        for index, chat_id in enumerate(ids):
            chats.update({index: self.db.query_one("""
            SELECT * FROM public."Chats"
            WHERE 'ChatId' = '%(chat_id)s'
            LIMIT %(limit)s""", chat_id=chat_id, limit=int(limit))})
        return chats

    def get_users_by_query(self, query, limit=10):
        query = query + ':*'
        return self.db.query_all("""
        SELECT * FROM public."Users"
        WHERE to_tsvector(Nick) @@ to_tsquery(%(query)s)
        OR to_tsvector(Name) @@ to_tsquery(%(query)s)
        LIMIT %(limit)s""", query=str(query), limit=int(limit))

    def create_new_chat(self):
        ret = self.db.create("""
            INSERT INTO public."Chats" ("IsGroup", "Topic") 
            VALUES ('false', '')
            RETURNING 'ChatId'""")
        self.db._commit_db()
        return ret

    def create_chat(self, id1, id2):
        ids1 = set(self.get_chat_ids(id1))
        ids2 = set(self.get_chat_ids(id2))
        matches = list(ids1 & ids2)
        if not matches:
            chat_id = self.create_new_chat()
            self.db.insert("""
            INSERT INTO public."Members" ('UserId', 'ChatId', 'UnreadedMessageCount')
            VALUES ('%(id1)s', '%(chat_id)s', '0')""", id1=id1, last_id=chat_id)
            self.db.insert("""
            INSERT INTO public."Members" ('UserId', 'ChatId', 'UnreadedMessageCount')
            VALUES ('%(id2)s','%(chat_id)s', '0')""", id2=id2, last_id=chat_id)
            self.db._commit_db()
            return 'OK'
        else:
            matches_chat_id = matches[0]
            ret = self.db.query_one("""
            SELECT * FROM public."Chats"
            WHERE 'ChatId'='%(matches_chat_id)s'
            AND 'IsGroup'=false""", id=matches_chat_id)

            self.db._commit_db()
            return ret

    def send(self, user_id, chat_id, content):
        last_message_id = self.create_new_message(user_id, chat_id, content)
        self.db.execute("""
            UPDATE public."Members"
            SET 'UnreadMessageCount'='UnreadMessageCount'+1
            WHERE 'ChatId'='%(chat_id)s'
            AND 'UserId'<>'%(user_id)s'""", chat_id=chat_id, user_id=user_id)

        message = {
            'message_id': last_message_id,
            'user_id': user_id,
            'content': content,
            'added_at': datetime.datetime.now(),
            'chat_id': chat_id
        }
        self.db._commit_db()
        return message

    def read(self, user_id, message_id):
        print(message_id)
        target_chat = self.db.query_one("""
        SELECT 'ChatId' FROM messages
        WHERE 'Id'='%(message_id)s'""", message_id=message_id)
        chat_id = target_chat['ChatId']
        print(chat_id)

        self.db.execute("""
            UPDATE public."Members"
            SET 'UnreadMessageCount'='UnreadMessageCount'-1
            WHERE 'ChatId'='%(chat_id)s'
            AND 'UserId'='%(user_id)s'""", chat_id=chat_id, user_id=user_id)

        res = self.db.query_one("""
        SELECT * FROM chats
        WHERE chat_id=%(chat_id)s""", chat_id=chat_id)

        self.db._commit_db()

        return res
