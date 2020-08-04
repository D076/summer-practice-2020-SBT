import bcrypt
import json
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
    User,
    PublicCollection
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
    if temp_user is None or not bcrypt.checkpw(password.encode('utf8'), temp_user.password):
        abort(401, 'Login or password is incorrect')

    token = generateToken()

    global tokens
    temp_dict = {}
    temp_dict['user_id'] = temp_user.id
    temp_dict['token'] = token
    tokens.append(temp_dict)

    return token, 200


@module.route('/logout/<token>/', methods=['GET'])
def logout(token):
    '''
    in
    string
    out
    - 200 OK
    - 404 Non-existing token
    '''
    for i in tokens:
        if i['token'] == token:
            tokens.pop(tokens.index(i))
            return '', 200
    abort(404, 'Non-existing token')

    return '', 200


@module.route('/validate/<token>/', methods=['GET'])
def validate(token):
    '''
    in
    string
    out
    - 200 OK
    - 404 Non-existing token
    '''
    for i in tokens:
        if i['token'] == token:
            return '', 200
    abort(404, 'Non-existing token')


'''
    for i in tokens:
        if i['token'] == token:
            return token, 200
    abort(404, 'Non-existing token')

    return '', 200
'''


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

    # Add user information into database
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

    global tokens
    user_id = None
    for i in tokens:
        if i['token'] == token:
            user_id = i['user_id']
            break

    # If token doesn't exist
    if user_id is None:
        abort(404, 'Non-existing token')

    # yes -> Remove login from db. Decrement userId. return 200
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.commit()

    # Temporarily. In the future, transfer initialization and remove code below
    global last_user_id

    # Initialize last_user_id
    if last_user_id is None:
        last_user_table_id = db.session.query(func.max(User.id)).scalar()
        if last_user_table_id is None:
            last_user_id = 0
        else:
            last_user_id = last_user_table_id
    # End of temp code

    last_user_id -= 1
    # logout
    for i in tokens:
        if i['token'] == token:
            tokens.pop(tokens.index(i))
            break

    return "Complete", 200


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

    global tokens

    # Searching token in tokens list
    user_id = None
    for i in tokens:
        if i['token'] == token:
            user_id = i['user_id']
            break

    # If token doesn't exist
    if user_id is None:
        abort(404, 'Non-existing token')

    user = User.query.filter_by(id=user_id).first()

    info = {
        'user_id': user_id,
        'login': user.login,
        'name': user.name
    }

    return jsonify(info), 200


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
    user = User.query.filter_by(login=login).first()
    if user is None:
        abort(404, 'Non-existing login')

    info = {
        'user_id': user.id,
        'login': user.login,
        'name': user.name
    }

    return jsonify(info), 200


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

    if not 'password' in info or \
            not 'new_password' in info or \
            not 'name' in info:
        abort(400)

    global tokens

    # Searching token in tokens list
    user_id = None
    for i in tokens:
        if i['token'] == token:
            user_id = i['user_id']
            break

    # If token doesn't exist
    if user_id is None:
        abort(404, 'Non-existing token')

    temp_user = User.query.filter_by(id=user_id).first()

    update_name = temp_user.name
    hashed_password = temp_user.password
    password = info['password']
    new_password = info['new_password']
    name = info['name']

    # If user want to change pass, check with hash in db
    if password != '' and new_password != '':
        if temp_user is None \
                or not bcrypt.checkpw(password.encode('utf8'), temp_user.password):
            abort(401, 'Password is incorrect')
        hashed_password = bcrypt.hashpw(new_password.encode('utf8'), bcrypt.gensalt())

    # Check if user want to change name
    if name != '':
        update_name = name

    temp_user.password = hashed_password
    temp_user.name = update_name
    db.session.commit()

    return '', 200


@module.route('/permissions/setPublicCollection/<int:collection_id>/', methods=['POST'])
def setPublicCollection(collection_id):
    '''
    in
    int
    out
    - 200
    - 400
    '''

    # Finding public collection with same collection_id
    existing_public_collection = PublicCollection \
                                .query \
                                .filter_by(collection_id=collection_id) \
                                .first()

    # If collection already public, abort
    if existing_public_collection:
        abort(400, 'Collection already public!')

    # Create new public collection
    new_public_collection = PublicCollection(collection_id=collection_id)

    # Add new public collection into 
    db.session.add(new_public_collection)
    db.session.commit()

    return '', 200


@module.route('/permissions/getPublicCollection/', methods=['POST'])
def getPublicCollection():
    '''
    in
    [5, 7, 8, 12, 56]
    out
    - 200
    [12, 56]
    - 400
    '''

    if not request.json:
        abort(400)

    request_collections = json.loads(request.json)

    # Filter collections
    filtered_collections = [public_collection.collection_id for public_collection in PublicCollection.query \
                            if public_collection.collection_id in request_collections]

    return jsonify(filtered_collections), 200
