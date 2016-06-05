# -*- coding: utf-8 *-*
import flask.ext.login as flask_login

from ezlog3.api import apiapp
from ezlog3.model import User, Tweet



@apiapp.route("/tweet/", methods=["GET", "POST"])
@login_required
def tweetit():
    if request.method == "POST":
        content = request.form.get("content").strip() or None
        if content is None:
            return dict(rcode=403)
        content = content + " "
        tweet = Tweet(content=content, author=flask_login.current_user)
        tweet.save()
        tweet.post_process()
        return dict(rcode=200)


