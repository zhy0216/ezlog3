# -*- coding: utf-8 -*-

import os
import logging

from fabric.api import local

_warn = logging.warn
CURRENT_PATH = os.path.join(os.getcwd(),os.path.dirname(__file__))

def update():
    """ update function,
        update stuff from model/update
        instal new package ==> check if it is in virtualenv
    """
    pass


def update_req():
    """Updating requirements for pip"""
    # check whether in virtualenv
    if not os.environ.get("VIRTUAL_ENV"):
        _warn("You are not in an Virtualenv, please activate it first")
        return
    local("pip freeze > %s/pip_requirements.txt" % CURRENT_PATH)

def gen_deploy_config():
    config = {

    }
    ## run the script from script/
    pass

def test():
    """Run nose test"""
    local("nosetests --nocapture")