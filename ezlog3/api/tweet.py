# -*- coding: utf-8 *-*
from flask import jsonify, request

import flask.ext.login as flask_login

from ezlog3.api import apiapp
from ezlog3.model import User, Tweet





@apiapp.route("/tweet/", methods=["POST"])
@flask_login.login_required
def tweetit():
    if request.method == "POST":
        content = request.form.get("content") or None
        if content is None:
            return jsonify(dict(msg="input your content", rcode=404)) # change to the right 
        content = content.strip() + " "
        tweet = Tweet(content=content, author=flask_login.current_user.id)
        tweet.save()
        tweet.post_process()
        return jsonify(dict(tweet=tweet.render(), rcode=200))



@apiapp.route("/tweet/", methods=["GET"])
def get_tweets():
    pass


@apiapp.route("/tweet/<tweetid>/", methods=["GET"])
def get_tweet(tweetid):
    pass