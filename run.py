#! /home/user/git/4trackBack/venv/bin/python3
from app import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def hello():
    print("Hello!")

if __name__ == "__main__":
    #app.run()
    manager.run()
