from app.models import User, BetaEmailSubscriber
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from flask_sqlalchemy import SQLAlchemy



app = create_app()
manager = Manager(app)
manager.add_command('db', MigrateCommand)
db = SQLAlchemy(app)

if __name__ == '__main__':
    manager.run()
    db.create_all()
