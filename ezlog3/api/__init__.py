from flask import Blueprint

apiapp = Blueprint('apiapp', __name__)

import user
import tweet