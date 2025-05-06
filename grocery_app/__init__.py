from flask import Flask
from flask_login import LoginManager
from grocery_app.extensions import db, bcrypt
from grocery_app.models import User
from grocery_app.routes import main, auth

def create_app():
    app = Flask(__name__)
    app.config.from_object('grocery_app.config.Config')

    db.init_app(app)
    bcrypt.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
