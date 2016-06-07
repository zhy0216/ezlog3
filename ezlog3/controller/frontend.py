import base64
from functools import wraps

import flask
from flask import render_template, Response,request
import flask.ext.login as flask_login

from ezlog3 import app, login_manager
from ezlog3.model import User, Tweet



@login_manager.unauthorized_handler
def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

@login_manager.request_loader
def load_user_from_request(request):
    auth = request.authorization
    if auth:
        user = User.validate_user(auth.username, auth.password)
        if user:
            flask_login.login_user(user)
            return user


@app.route("/")
def main():
    data = {
        "user": User.objects().first(),
        "tweets": Tweet.objects.order_by('-create_date'),
        "cur_user": flask_login.current_user,
    }

    return render_template('main.html',**data)

@app.route("/config", methods=["GET", "POST"])
@flask_login.login_required
def config():
    if request.method == "GET":
        data = {
            "cur_user": flask_login.current_user,
        }
        return render_template('config.html',**data)
    else:
        cur_user = flask_login.current_user
        for attr in request.form:
            if request.form[attr]:
                setattr(cur_user, attr, request.form[attr])
        cur_user.save()
        return flask.redirect("/")

@app.route("/login")
@flask_login.login_required
def login():
    return flask.redirect("/")


@app.route("/logout")
def logout():
    flask_login.logout_user()
    return authenticate()