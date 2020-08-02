import bcrypt
from uuid import uuid4 
from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    abort,
    redirect,
    url_for,
    current_app,
    jsonify
)

# Token generation function uses
# UUIDv4
def generateToken():
    return uuid4().hex

module = Blueprint('entity', __name__)

@module.route('/', methods=['GET'])
def index():
    return 'Hello'

@module.route('/auth/', methods=['POST'])
def auth():
    '''
    in 
    {
        "login": "a1pha1337@gmail.com",
        "password": "rhokef3"
    }
    out
    token
    '''
    if not request.json or not 'login' in request.json or not 'password' in request.json:
        abort(400)
    login = request.json['login']
    password = request.json['password']
    # comp login/pass with data in db
    # if incorret -> abort(401)

    # else
    token = generateToken()
    # write token in memory
    return token, 200

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
def userRegister():
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
    if not request.json or not 'login' in request.json or not 'password' in request.json:
        abort(400)
    login = request.json['login']
    password = request.json['password']
    # comp login with logins in db
    # if true -> abort(401)

    # else write in db
    token = generateToken()
    # write token in memory
    return token, 200

@module.route('/user/delete/<token>/', methods=['DELETE'])
def userDelete(token):
    '''
    in
    string
    out
    - 200 OK
    - 404 Non-existing token
    '''
    # valid tioken ?
    # yes -> go next
    # no -> ERROR 404

    


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
def userInfoEdit():
    '''
    in
    {
        "token": "f57ebe597a3741b688269209fa29b053",
        "info": {
            "password": "rhokef3",
            "name": "Solo_322"
        }
    }
    out
    - 200
    - 400
    '''
    # data = ???
    # login = ''
    # password = ''
    # if 'token' not in data.keys() or 'info' not in data.keys():
    #     return 400 # incorrect json body
    # elif 'password' not in data.keys(info) or 'name' not in data.keys(info):
    #     return 400
    # for key, value in data.items():
    #     if key == 'login':
    #         login = value
    #     if key == 'password':
    # ...create a token...
    # response = token
    return f'def userInfoEdit'
