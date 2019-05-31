#! /home/user/git/4trackBack/venv/bin/python3
from app import app, db

from app.fill_db import *
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from tests.selenium import selenium_tests, selenium_test2

migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def hello():
    print("Hello!")

@manager.command
def fill_db():
    print("fill db")
    fill_user()
    fill_chat()
    fill_message()
    fill_attachment()

@manager.command
def selenium():
    selenium_test2()


if __name__ == "__main__":
    #app.run()
    manager.run()
