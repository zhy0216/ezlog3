# -*- coding: utf-8 -*-

from ezlog3 import app


if(__name__ == "__main__"):
    app.debug = app.config["DEBUG_MODE"]
    port = app.config["PORT"]
    app.run(port=port)