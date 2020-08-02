from app.database import db

# User database tabel
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
        return '<User(id={0}, login={1}, name{2})>'
                .format(self.id, self.login, self.name)

# Role database tabel
class Role(db.Model):
    # Primary key
    id = db.Column(db.BigInteger, 
        db.Sequence('role_seq', start=0, increment=1), 
        primary_key=True)

    # Role permissions
    role_id = db.Column(db.BigInteger, unique=True, nullable=False)
    name = db.Column(db.String(length=30), unique=True, nullable=False)
    read = db.Column(db.Boolean, nullable=False)
    rate = db.Column(db.Boolean, nullable=False)
    write = db.Column(db.Boolean, nullable=False)
    edit_other_user_permissions = db.Column(db.Boolean, nullable=False)
    delete_collection = db.Column(db.Boolean, nullable=False)

    # Role relationships
    roles_in_users_collections = db.relationship('UserRoleInCollection')

    def __repr__(self):
        return '<Role(id={0}, role_id={1}, name={2}, read={3}, rate={4}, write={5}, \
                    edit_other_user_permissions={6}, delete_collection={7})>'
                .format(self.id, self.role_id, self.name, self.read, self.rate, self.write, \
                    self.edit_other_user_permissions, self.delete_collection)

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
        return '<UserRoleInCollection(id={0}, collection_id={1}, role_id={2}, user_id={3})>'
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
        return '<Post(id={0}, post_id={1}, user_id={2})>'
                .format(self.id, self.post_id, self.user_id)

# PublicCollection database table
class PublicCollection(db.Model):
    collection_id = db.Column(db.BigInteger, primary_key=True, unique=True, nullable=False)

    def __repr__(self):
        return '<PublicCollection(collection_id={0})>'
                .format(self.collection_id)