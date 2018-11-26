import flask
import psycopg2
from app.instance.config import TestConfig as config
import psycopg2.extras
from app import app


class Database:
    def __init__(self):
        self.database = config.DB_NAME
        self.host = config.DB_HOST
        self.user = config.DB_USER
        self.password = config.DB_PASS
        self.__connection = None
        flask.got_request_exception.connect(self._rollback_db, app)
        flask.request_finished.connect(self._commit_db, app)

    @property
    def connect(self):
        if not self.__connection:
            self.__connection = psycopg2.connect(
                database=self.database, host=self.host,
                user=self.user, password=self.password)

        return self.__connection

    @property
    def get_cursor(self):
        return self.connect.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def query_one(self, sql, **params):
        with self.get_cursor as cur:
            cur.execute(sql, params)
            return dict(cur.fetchone())

    def query_all(self, sql, **params):
        with self.get_cursor as cur:
            cur.execute(sql, params)
            db_response = cur.fetchall()
            result = {}
            for index, el in enumerate(db_response):
                result.update({index: dict(el)})
            return result

    def _rollback_db(self, sender, exception, **extra):
        if not self.__connection:
            return
        conn = self.connect
        conn.rollback()
        conn.close()
        self.__connection = None

    def _commit_db(self, sender=None, **extra):
        if not self.__connection:
            return
        conn = self.connect
        conn.commit()
        conn.close()
        self.__connection = None

    def insert(self, sql, **params):
        with self.get_cursor as cur:
            cur.execute(sql, params)
            return True

    def create(self, sql, **params):
        with self.get_cursor as cur:
            cur.execute(sql, params)
            new_id = cur.fetchone()[0]
            return new_id
