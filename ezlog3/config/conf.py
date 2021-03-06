# -*- coding: utf-8 -*-

import logging
import datetime as dt

DEBUG_MODE = True
DEMO = False

SITENAME = "EZLOG"#your site here
SITE_VERSION  = 1.0
MODEL_VERSION = 1.0
SITE_DOMAIN = ""#your site here
SERVER_NAME = None
PORT = 5000
SECRET_KEY = "secret_keyplzchangeit~"

MONGODB_DB_UNITTEST = "somedbnameforunittest"
MONGODB_HOST = "localhost"
MONGODB_PORT = 27017
MONGODB_USER = ''
MONGODB_PASSWD = ''

SENTRY_DSN = ''#somethinf about sentry


try:
    from local_conf import *
except ImportError, e:
    pass
except Exception, e:
    logging.warn("Cannot import configurations from local_config, error: %s" % e)

SITE = "http://%s:%s"%(SITE_DOMAIN, PORT)