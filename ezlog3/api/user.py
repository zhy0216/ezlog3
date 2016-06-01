from flask.ext.login import login_required, current_user

from ezlog3.api import  apiapp


@apiapp.route("/")
@login_required
def api_main():
    return current_user.nickname


