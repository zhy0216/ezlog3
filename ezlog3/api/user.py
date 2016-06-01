from flask.ext.login import login_required, current_user

from ezlog3.api import  apiapp


@apiapp.route("/")
@login_required
def api_main():
    return current_user.nickname


@apiapp.route("/user/<userid>/", methods=["POST"])
@login_required
def modify_user(userid):
    if userid != current_user.id:
        # throw out an exception
        return "error"

    
