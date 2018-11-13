import unittest
from flask import jsonify
from app import app
import  json
from app.database import Database


class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.code = 200
        self.type = 'application/json'

    def common_asserts(self, rv):
        self.assertEqual(self.code, rv.status_code)
        self.assertEqual(self.type,  rv.mimetype)

    def test_search_users(self):
        rv = self.app.get(f'/api/search_users/?query="qq"&limit=12')
        self.common_asserts(rv)

        #self.assertEqual(json.dumps({"users": Database().get_users}), rv.read().decode('utf-8'))

        #self.assertEqual("text/html", rv.mimetype)

    def test_search_chats(self):
        rv = self.app.get(f'/api/search_chats/?query="qq"&limit=12')
        self.common_asserts(rv)

    def test_list_chats(self):
        rv = self.app.get(f'/api/list_chats/')
        self.common_asserts(rv)

    def test_create_pers_chat(self):
        rv = self.app.post(f'/api/create_pers_chat/?user_id=12')
        self.common_asserts(rv)

    def test_create_group_chat(self):
        rv = self.app.post(f'/api/create_group_chat/?topic="topic"')
        self.common_asserts(rv)

    def test_leave_group_chat(self):
        rv = self.app.post(f'/api/leave_group_chat/?chat_id=12')
        self.common_asserts(rv)

    def test_send_message(self):
        rv = self.app.post(f'/api/send_message/?chat_id=12&content="12"&attach_id=12')
        self.common_asserts(rv)

    def test_read_message(self):
        rv = self.app.get(f'/api/read_message/?message_id=12')
        self.common_asserts(rv)


if __name__ == "__main__":
    unittest.main()
