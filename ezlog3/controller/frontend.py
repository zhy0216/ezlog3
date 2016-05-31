
from flask import render_template

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
        pass