from app.database import db

# User database table
class User(db.Model):
    # Primary key
    id = db.Column(db.BigInteger, primary_key=True)

    # Authentication data
    login = db.Column(db.String(length=30), unique=True, nullable=False)
    password = db.Column(db.String(length=80), nullable=False)

    # User info
    name = db.Column(db.String(length=40), nullable=False)

    # User relationships
    user_roles_in_collections = db.relationship('UserRoleInCollection')
    user_posts =  db.relationship('Post')

    def __repr__(self):
        return '<User(id={0}, login={1}, name{2})>' \
                .format(self.id, self.login, self.name)

# Role database table
class Role(db.Model):
    # Primary key
    id = db.Column(db.BigInteger, primary_key=True)

    # Name role
    name = db.Column(db.String(length=30), unique=True, nullable=False)

    # Link relationships
    permissions_in_role = db.relationship('RolesPermissions')

    def __repr__(self):
        return '<Permission(id={0}, name={1})>' \
                .format(self.id, self.name)  

# Permission database table
class Permission(db.Model):
    # Primary key
    id = db.Column(db.BigInteger, 
        db.Sequence('perm_seq', start=0, increment=1), 
        primary_key=True)

    # Name permission
    name = db.Column(db.String(length=30), unique=True, nullable=False)

    # Link relationships
    roles_in_permission = db.relationship('RolesPermissions')

    def __repr__(self):
        return '<Permission(id={0}, name={1})>' \
                .format(self.id, self.name) 

# Link database table
class RolesPermissions(db.Model):
    # Primary key
    id = db.Column(db.BigInteger, 
        db.Sequence('link_seq', start=0, increment=1), 
        primary_key=True)

    # Foreign keys
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    perm_id = db.Column(db.Integer, db.ForeignKey('permission.id'), nullable=False)

    def __repr__(self):
        return '<Link(id={0}, role_id={1}. perm_id={2})>' \
                .format(self.id, self.role_id, self.perm_id)        

# UserRoleInCollection database table
class UserRoleInCollection(db.Model):
    # Primary key
    id = db.Column(db.BigInteger, 
        db.Sequence('user_role_in_collection_seq', start=0, increment=1), 
        primary_key=True)

    # Collection ID
    collection_id = db.Column(db.BigInteger, nullable=False)

    # Foreign keys
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<UserRoleInCollection(id={0}, collection_id={1}, role_id={2}, user_id={3})>' \
                .format(self.id, self.collection_id, self.role_id, self.user_id)

# Post database table
class Post(db.Model):
    # Primary key
    id = db.Column(db.BigInteger, 
        db.Sequence('post_seq', start=0, increment=1), 
        primary_key=True)

    # Post ID
    post_id = db.Column(db.BigInteger, nullable=False)

    # Foreign keys
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Post(id={0}, post_id={1}, user_id={2})>' \
                .format(self.id, self.post_id, self.user_id)

# PublicCollection database table
class PublicCollection(db.Model):
    collection_id = db.Column(db.BigInteger, primary_key=True, unique=True, nullable=False)

    def __repr__(self):
        return '<PublicCollection(collection_id={0})>' \
                .format(self.collection_id)