# -*- coding: utf-8 *-*
import string,random
from flask import g,session,jsonify,render_template
from ezlog3.libs.db import db
from datetime import datetime as dt
from mongoengine import CASCADE

class Tweet(db.Document):
    content            = db.StringField(required=True)
    type               = db.StringField(default="text")
    create_date        = db.DateTimeField(default=dt.now)

    meta = {
        'allow_inheritance': True,
        'index_types': False,
    }

    def __ini__(self):
        pass

class ArticleTweet(Tweet):
    type               = db.StringField(default="article")

class PictureTweet(Tweet):
    type               = db.StringField(default="picture")

class VideoTweet(Tweet):
    type               = db.StringField(default="video")


class Topic(db.Document):
    name               = db.StringField()
    tweet              = db.ReferenceField("Tweet", reverse_delete_rule=CASCADE)
