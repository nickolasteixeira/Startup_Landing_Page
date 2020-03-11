from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
import logging

db = SQLAlchemy()
migrate = Migrate()
api = Api()

logger = logging.basicConfig(level=logging.DEBUG,
                             format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def create_app(config_class=config.DevelopmentConfig):
    # imports
    from app.resources import user_resources
    from app.resources import beta_email_subscribers_resources
    from app import errors

    # configure app
    app = Flask(__name__)

    # change to production config when deploying
    app.config.from_object(config_class)

    # register error handlers
    app.register_error_handler(errors.EmailAlreadyInUse,
                               errors.handle_email_already_in_use)

    # register db
    db.init_app(app)

    # register migration
    migrate.init_app(app, db)

    # register api resources
    api.add_resource(user_resources.UserRegistration, '/registration')
    api.add_resource(user_resources.UserLogin, '/login')
    api.add_resource(user_resources.UserLogoutAccess, '/logout/access')
    api.add_resource(user_resources.UserLogoutRefresh, '/logout/refresh')
    api.add_resource(user_resources.TokenRefresh, '/token/refresh')
    api.add_resource(user_resources.AllUsers, '/users')
    api.add_resource(user_resources.SecretResource, '/secret')

    # beta email api resources
    api.add_resource(beta_email_subscribers_resources.BetaEmailSignUp, '/beta')

    # initialize api
    api.init_app(app)

    return app
