
import flask
from flask import render_template
import flask.ext.login as flask_login

from ezlog3 import app
from ezlog3.model import User, Tweet

@app.route("/")
def main():
    data = {
        "user": User.objects().first(),
        "tweets": Tweet.objects().all(),
        "cur_user": flask_login.current_user,
    }

    return render_template('main.html',**data)

@app.route("/config")
def config():
    # config page
    pass

if app.config["DEBUG_MODE"]:
    @app.route("/debug/login")
    def debug_login():
        flask_login.login_user(User.objects().first())
        return flask.redirect(flask.url_for('main'))

    @app.route("/debug/logout")
    @flask_login.login_required
    def debug_logout():
        flask_login.logout_user()
        return flask.redirect(flask.url_for('main'))

