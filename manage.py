import os
from flask_script import Manager

from TheApp import app
from TheApp.database import session, Base
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)


@manager.command
def seed():
    pass


from getpass import getpass
from werkzeug.security import generate_password_hash
from TheApp.database import User

@manager.command
def adduser():
    pass


class DB(object):
    def __init__(self, metadata):
        self.metadata = metadata

migrate = Migrate(app, DB(Base.metadata))
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
