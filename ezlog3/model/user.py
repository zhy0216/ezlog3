#coding: utf-8
import string,random
from ezlog3.libs.db import db

class User(db.Document):
    username    = db.StringField(required=True)
    nickname    = db.StringField(default="imdefault")
    avatar      = db.StringField(default="static/default_avatar.jpg")
    bg_img      = db.StringField(default="static/bg.jpg")
    password    = db.StringField(required=True)
    quote       = db.StringField(default="im a quote, say something")

    meta = {
        'allow_inheritance': False,
        'index_types': False,
        'indexes': [
            {'fields': ['username'], 'unique': True},
        ]
    }

    @classmethod
    def get_user_by_id(cls, id):
        if id is None:
            return None
        return cls.objects(id=id).first()
    @classmethod
    def get_user_by_username(cls,username):
        return cls.objects(username=username).first()

    @classmethod
    def get_user_by_nickname(cls,nickname):
        return cls.objects(nickname=nickname).first()

    @classmethod
    def is_valid(cls,username,password):
        user = cls.objects(username=username,password=password).first()
        return user is not None

    @classmethod
    def validate_user(cls, username, password):
        return cls.objects(username=username,password=password).first()