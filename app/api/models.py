from sqlalchemy.orm import relationship
from app.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    login = db.Column(db.String)
    password = db.Column(db.String)
    name = db.Column(db.String)

    user_roles_in_collections = db.relationship('UserRoleInCollection')
    user_posts =  db.relationship('Post')

class Role(db.Model):
    id = db.Column(db.Integer, 
        db.Sequence('role_seq', start=0, increment=1), 
        primary_key=True)

    role_id = db.Column(db.Integer)
    name = db.Column(db.String)
    read = db.Column(db.Boolean)
    rate = db.Column(db.Boolean)
    write = db.Column(db.Boolean)
    edit_othet_user_permissions = db.Column(db.Boolean)
    delete_collection = db.Column(db.Boolean)

    roles_in_users_collections = db.relationship('UserRoleInCollection')

class UserRoleInCollection(db.Model):
    id = db.Column(db.Integer, 
        db.Sequence('user_role_in_collection_seq', start=0, increment=1), 
        primary_key=True)

    collection_id = db.Column(db.Integer)

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Post(db.Model):
    id = db.Column(db.Integer, 
        db.Sequence('post_seq', start=0, increment=1), 
        primary_key=True)

    post_id = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class PublicCollection(db.Model):
    collection_id = db.Column(db.Integer, primary_key=True)