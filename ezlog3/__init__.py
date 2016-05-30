# coding: utf-8

import flask

app = flask.Flask(__name__)
app.config.from_object("ezlog3.config.conf")
