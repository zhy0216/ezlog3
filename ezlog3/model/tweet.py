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
    author             = db.ReferenceField("User", reverse_delete_rule=CASCADE)

    meta = {
        'allow_inheritance': True,
        'index_types': False,
    }

    def __ini__(self):
        pass

    def post_process(self):
        ## parse topic first
        # content
        topics = re.findall(r"#(\w+)\W", self.content)
        for topic_name in self.topics:
            topic = Topic(name=topic_name, tweet=self)
            topic.save()

class Topic(db.Document):
    name               = db.StringField()
    tweet              = db.ReferenceField("Tweet", reverse_delete_rule=CASCADE)
