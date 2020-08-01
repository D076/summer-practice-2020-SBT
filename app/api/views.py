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
    return 'def Index'

@module.route('/auth/', methods=['POST'])
def auth():
    return 'def auth'

@module.route('/validate/<token>/', methods=['GET'])
def validate(token):
    return f'def validate {token}'

@module.route('/user/', methods=['POST'])
def userRegister():
    return 'def userRegister'

@module.route('/user/delete/<token>/', methods=['DELETE'])
def userDelete(token):
    return f'def userDelete {token}'

@module.route('/user/info/<token>/', methods=['GET'])
def userInfoGet(token):
    return f'def userInfoGet {token}'

@module.route('/user/info/public/<login>/', methods=['GET'])
def userInfoPublicGet(login):
    return f'def userInfoPublicGet {login}'

@module.route('/user/info/', methods=['PUT'])
def userInfoEdit(login):
    return f'def userInfoEdit'
