import unittest
from mock import patch
import app.memcache
from flask import jsonify
#from app import app
import app

import json
from forbiddenfruit import curse
from app.database import Database

# python3 -m unittest tests/app_tests.py

class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.code = 200
        self.type = 'application/json'

        # мог и хотел
        curse(str, 'json_compare_re', json_compare_re)
        curse(str, 'json_compare', json_compare)

    def common_asserts(self, rv):
        self.assertEqual(self.code, rv.status_code)
        self.assertEqual(self.type,  rv.mimetype)

    def test_create_user(self):
        with patch('app.memcache.get_cache_hello') as cache_mock:
            cache_mock.return_value = "underworld"
            app.memcache.just4test()
            #test_nick = 'test_nick'
            #self.app.post('/api/delete_user/', data={'nick':test_nick})

'''
    def test_list_chats(self):
        rv = self.app.get(f'/api/list_chats/')
        self.common_asserts(rv)
        self.assertTrue(rv.data.decode('utf-8')
                        .json_compare({"chats": Database().get_chats}))

    def test_create_pers_chat(self):
        rv = self.app.post(f'/api/create_pers_chat/?user_id=12')
        self.common_asserts(rv)
        self.assertTrue(rv.data.decode('utf-8')
                        .json_compare({"chats": Database().get_chats}))

    def test_create_group_chat(self):
        rv = self.app.post(f'/api/create_group_chat/?topic="topic"')
        self.common_asserts(rv)
        self.assertTrue(rv.data.decode('utf-8')
                        .json_compare({}))

    def test_leave_group_chat(self):
        rv = self.app.post(f'/api/leave_group_chat/?chat_id=12')
        self.common_asserts(rv)
        self.assertTrue(rv.data.decode('utf-8')
                        .json_compare({}))

    def test_add_members_to_group_chat(self):
        rv = self.app.post(f'/api/add_members_to_group_chat/?chat_id=12&user_ids[]=12&user_ids[]=13')
        self.common_asserts(rv)
        self.assertTrue(rv.data.decode('utf-8')
                        .json_compare({}))

    def test_send_message(self):
        rv = self.app.post(f'/api/send_message/?chat_id=12&content="12"&attach_id=12')
        self.common_asserts(rv)
        self.assertTrue(rv.data.decode('utf-8')
                        .json_compare({'message': Database().message1}))

    def test_read_message(self):
        rv = self.app.get(f'/api/read_message/?message_id=12')
        self.common_asserts(rv)
        self.assertTrue(rv.data.decode('utf-8')
                        .json_compare({'chat': Database().chat1}))

    def test_upload_file(self):
        rv = self.app.post(f'/api/upload_file/?chat_id=12&content="12"')
        self.common_asserts(rv)
        self.assertTrue(rv.data.decode('utf-8')
                        .json_compare({'attach': Database().attachment1}))
        
'''

def json_compare(self, other_json):
    """
    Собственно, функа сравнения джейсонов) Вообще - обёртка над рекурсивной функцией,
    реальо выполняющей сравнение.
    :param self: стринга
    :param other_json: стринга или валидный json-подобный объект
    :return: True Если всё валидно и совпало, иначе False
    """
    if type(other_json) is str:
        other_json = json.loads(other_json)
    self_json = json.loads(self)
    return self.json_compare_re(self_json, other_json)


def json_compare_re(self, self_json, other_json):
    """
    Сама рекурсивная функа. Пробегается по объектам вся сравнивает)
    :param self:
    :param self_json: валидный json-подобный объект
    :param other_json: валидный json-подобный объект
    :return: True Если всё валидно и совпало, иначе False
    """
    if type(self_json) != type(other_json):
        return False
    if type(self_json) == list:
        if len(self_json) != len(other_json):
            return False
        # Перебираем все элементы одного массива.
        # Если нашли в другом, запоминаем где и там больше не ищем.
        counted = set()
        for value in self_json:
            found = False
            for i in range(len(other_json)):
                if i in counted:
                    continue
                if self.json_compare_re(value, other_json[i]):
                    counted.add(i)
                    found = True
                    break
            if not found:
                return False
        return True

    if type(self_json) == dict:
        if len(self_json.keys()) != len(other_json.keys()):
            return False
        for k in self_json.keys():
            if k not in other_json:
                return False
            if not self.json_compare_re(self_json[k], other_json[k]):
                return False
        return True

    types = {int, float, complex, str, bool, }
    if type(self_json) in types:
        return self_json == other_json

    print(f"\nwrong type! + {type(self_json)}\n")
    return False


if __name__ == "__main__":

    #print('{"type": "my"}'.json_compare('[{"type": "my"}, {"t":"m"}]'))
    unittest.main()