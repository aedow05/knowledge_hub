# app/models.py
# Defines the database models and tables using SQLAlchemy ORM.

from enum import unique
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize SQLAlchemy instance
db = SQLAlchemy()

class User(db.Model):
    """
    User model representing a registered user in the system.
    Attributes:
        id: Primary key, auto-incrementing integer.
        username: Unique username for login/display purposes.
        email: Unique email address of the user.
        password_hash: Secure hashed password (never store plain passwords!).
        created_at: Timestamp of user creation; defaults to current time.
    Methods:
        set_password: Hashes and sets the password.
        check_password: Checks a plaintext password against stored hash.
    """

    # Table name in the database
    __tablename__ = "users"

    #Primary key column
    id = db.Column(db.Integer, primary_key=True)

    #Username must be unique and cannot be null
    username = db.Column(db.String(80), unique=True, nullable=False)

    #Email must be unique and cannot be null
    email = db.Column(db.String(80), unique=True, nullable=False)

    #Store hashed password, cannot be null
    password_hash = db.Column(db.String(128), nullable=False)

    #Automatically set to current time on creation
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    #---------- Methods for password handling ----------#
    """
        Hashes the given plaintext password and stores it in password_hash.
        Never store plaintext passwords!
        """
    def set_password(self,password: str):
       
       self.password_hash = generate_password_hash(password)

       return check_password_hash(self.password_hash, password)

    def __repr__(self):
        """
        Developer-friendly string representation of the user object.
        Useful for debugging and interactive shell.
        """
        return f"<User {self.username}>"