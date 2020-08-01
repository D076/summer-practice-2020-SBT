# import uuid, json
# import bcrypt
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
    return 'Hello'

@module.route('/auth/', methods=['POST'])
def auth(body):
    '''
    in 
    {
        "login": "a1pha1337@gmail.com",
        "password": "rhokef3"
    }
    out
    token
    '''
    # data = json.loads(body)
    # login = ''
    # password = ''
    # if 'login' not in data.keys() or 'password' not in data.keys():
    #     return 400 # incorrect json body
    # for key, value in data.items():
    #     if key == 'login':
    #         login = value
    #     if key == 'password':
    # ...create a token...
    # response = token
    return 'def auth'

@module.route('/validate/<token>/', methods=['GET'])
def validate(token):
    '''
    in
    string
    out
    - 200 OK
    - 404 Non-existing token
    '''
    # ...find actual user token...
    # if token == user_token:
    #   response = 200
    # else:
    #   response = 404
    # return response
    return f'def validate {token}'

@module.route('/user/', methods=['POST'])
def userRegister(body):
    '''
    in
    {
        "login": "a1pha1337@gmail.com",
        "password": "rhokef3"
    }
    out
    - 200
    token
    - 400 Incorrect login/pass
    '''
    # data = json.loads(body)
    # login = ''
    # password = ''
    # if 'login' not in data.keys() or 'password' not in data.keys():
    #     return 400 # incorrect json body
    # for key, value in data.items():
    #     if key == 'login':
    #         login = value
    #     if key == 'password':
    #         password = value
    # ...registration...create token...
    # response = token
    return 'def userRegister'

@module.route('/user/delete/<token>/', methods=['DELETE'])
def userDelete(token):
    '''
    in
    string
    out
    - 200 OK
    - 404 Non-existing token
    '''
    return f'def userDelete {token}'

@module.route('/user/info/<token>/', methods=['GET'])
def userInfoGet(token):
    '''
    in
    string
    out
    - 200
    {
        "user_id": 0,
        "login": "alpha13371@mail.ru",
        "name": "Solo_228"
    }
    - 404 Non-existing token
    '''
    return f'def userInfoGet {token}'

@module.route('/user/info/public/<login>/', methods=['GET'])
def userInfoPublicGet(login):
    '''
    in
    string
    out
    - 200
    {
        "user_id": 0,
        "login": "alpha13371@mail.ru",
        "name": "Solo_228"
    }
    - 404 Non-existing login
    '''
    return f'def userInfoPublicGet {login}'

@module.route('/user/info/', methods=['PUT'])
def userInfoEdit(body):
    '''
    in
    {
        "token": "f57ebe597a3741b688269209fa29b053",
        "info": {
            "password": "rhokef3",
            "name": "Solo_322"
        }
    }
    '''
    return f'def userInfoEdit'
