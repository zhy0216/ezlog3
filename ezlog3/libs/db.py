# coding:utf8

import os

from flask_mongoengine import MongoEngine

from ezlog3.config import conf

def get_db(database=None):
    database = conf.MONGODB_DB
    mongo = MongoEngine()
    mongo.connect(
        database,
        host=conf.MONGODB_HOST,
        port=conf.MONGODB_PORT,
        username=conf.MONGODB_USER,
        password=conf.MONGODB_PASSWD
    )
    return mongo

db = get_db()