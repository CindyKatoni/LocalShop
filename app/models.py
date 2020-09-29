from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

<<<<<<< HEAD
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

=======
>>>>>>> intialised log manager
from app import db, login_manager


class User(UserMixin, db.Model):
    """
<<<<<<< HEAD
    Create an User table
=======
    Create an Employee table
>>>>>>> intialised log manager
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
<<<<<<< HEAD
    return User.query.get(int(user_id))
=======
    return Employee.query.get(int(user_id))
>>>>>>> intialised log manager


class Product(db.Model):
    """
    Create a Products table
    """

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(60), unique=True)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Numeric(12, 2), nullable=False)

    @classmethod
    def unit_price(self):
        return self.total_price / self.quantity
    
    def __repr__(self):
        return '<Products: {}>'.format(self.name)


class Role(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
<<<<<<< HEAD
    users = db.relationship('User', backref='role',
                                lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)
        
=======
    employees = db.relationship('User', backref='role',
                                lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)
>>>>>>> intialised log manager
