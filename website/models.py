import uuid
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import os
from dataclasses import dataclass, field
# Requires key file

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(150), unique=True)
#     password = db.Column(db.String(150))
#     first_name = db.Column(db.String(150))
#     key_file = db.Column(db.BLOB()) 

@dataclass
class User(db.Model, UserMixin):
    uid: str = db.Column(db.String(200), unique=True)
    id: int = db.Column(db.Integer, primary_key=True)
    email: str = db.Column(db.String(150), unique=True)
    password: str = db.Column(db.String(150))
    first_name: str = db.Column(db.String(150))
    key_file: str = db.Column(db.String(500)) # Saves the *.txt version of the key_file



