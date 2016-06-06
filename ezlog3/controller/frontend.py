import base64
from functools import wraps

import flask
from flask import render_template, Response,request
import flask.ext.login as flask_login

from ezlog3 import app, login_manager
from ezlog3.model import User, Tweet

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'secret'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

@login_manager.unauthorized_handler
def unauthorized():
    auth = request.authorization
    return authenticate()

@app.route("/")
def main():
    data = {
        "user": User.objects().first(),
        "tweets": Tweet.objects.order_by('-create_date'),
        "cur_user": flask_login.current_user,
    }

    return render_template('main.html',**data)

@app.route("/config")
@flask_login.login_required
def config():
    # config page
    return "1"

if app.config["DEBUG_MODE"]:
    @app.route("/debug/login")
    def debug_login():
        flask_login.login_user(User.objects().first())
        return flask.redirect(flask.url_for('main'))




@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.headers.get('Authorization')
    return None
    user = User.objects().first()
    flask_login.login_user(user)
    return user


@app.route("/logout")
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for('main'))