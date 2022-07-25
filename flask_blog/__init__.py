from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_blog.config import Config
from flask_bcrypt import Bcrypt
from flask_mail import Mail

# TODO 0. Что за объект
db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
mail = Mail()


def create_app():
    # TODO 1. почему не в run.py
    app = Flask(__name__)

    # TODO 2. Что такое app.cofig
    app.config.from_object(Config)

    db.init_app(app)

    # TODO 3. Что за объект login_manager
    login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    # TODO 4. Локальный импорт это же не хорошо
    from flask_blog.main.routes import main
    from flask_blog.users.routes import users
    from flask_blog.posts.routes import posts
    from flask_blog.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(errors)

    return app
