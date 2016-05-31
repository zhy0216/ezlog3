
import flask
from flask import render_template
import flask.ext.login as flask_login

from ezlog3 import app
from ezlog3.model import User

@app.route("/")
def main():
    data = {
        "user": User()
    }

    return render_template('main.html',**data)

if app.config["DEBUG_MODE"]:
    @app.route("/debug/login")
    def debug_login():
        flask_login.login_user(User.objects().first())
        return flask.redirect(flask.url_for('main'))

    @app.route("/debug/logout")
    def debug_logout():
        flask_login.logout_user()
        return flask.redirect(flask.url_for('main'))

