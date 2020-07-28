from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    abort,
    redirect,
    url_for,
    current_app,
)

module = Blueprint('entity', __name__)

@module.route('/', methods=['GET'])
def index():
    return 'Hui'