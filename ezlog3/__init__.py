# coding: utf-8

import flask
import flask.ext.login as flask_login

app = flask.Flask(__name__)
app.config.from_object("ezlog3.config.conf")

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    from ezlog3.model import User
    return User.get_user_by_id(user_id)


import controller