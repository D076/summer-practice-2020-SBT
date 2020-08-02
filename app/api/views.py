import bcrypt
from uuid import uuid4 
from app.database import db
from sqlalchemy.sql import func
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

tokens = []
from app.api.models import (
    User
)

# Token generation function uses
# UUIDv4
def generateToken():
    return uuid4().hex

module = Blueprint('entity', __name__)

last_user_id = None

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
    temp_user = User.query.filter_by(login=login).first()
    if temp_user is None or not bcrypt.checkpw(password, temp_user.password):
        abort(401, 'Login or password is incorrect')

    token = generateToken()

    global tokens
    temp_dict = {}
    temp_dict['user_id'] = last_user_id
    temp_dict['token'] = token
    tokens.append(temp_dict)

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
        "name": "a1pha1337"
    }
    out
    - 200
    token
    - 400 Incorrect login/pass
    '''
    
    # JSON body checking
    if not request.json or \
        not 'login' in request.json or \
        not 'password' in request.json or \
        not 'name' in request.json:
        abort(400, 'Missed required arguments')

    login = request.json['login']
    password = request.json['password']
    name = request.json['name']

    # Get from database user with same login
    duplicated_user = User.query.filter_by(login=login).first()

    # If user with same login exists abort
    if duplicated_user is not None:
        abort(400, 'Login already exists')

    global last_user_id

    # Initialize last_user_id
    if last_user_id is None:
        last_user_table_id = db.session.query(func.max(User.id)).scalar()
        if last_user_table_id is None:
            last_user_id = 0
        else:
            last_user_id = last_user_table_id

    last_user_id += 1
    
    hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    newUser = User(id=last_user_id, login=login, password=hashed_password, name=name)

    db.session.add(newUser)
    db.session.commit()
    token = generateToken()

    global tokens
    temp_dict = {}
    temp_dict['user_id'] = last_user_id
    temp_dict['token'] = token
    tokens.append(temp_dict)

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
    # valid token ?
    # yes -> Remove login from db. Decrement userId. return 200
    # no -> return 404



    return "Complete", 200
    # return f'def userDelete {token}'

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
    # valid token ?
    # yes -> get userId from token. Get login and password by userId. Add to Answer. Return Answer, 200
    # no -> return 404

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
            "new_password": "123",
            "name": "Solo_322"
        }
    }
    out
    - 200
    - 400
    '''
    if not request.json or not 'token' in request.json or not 'info' in request.json:
        abort(400)
    token = request.json['token']
    info = request.json['info']

    if not 'password' in info or not 'new_password' in info or not 'name' in info:
        abort(400)
    # ...create a token...
    # response = token
    return f'def userInfoEdit'
