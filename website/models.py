from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import os

# Requires key file

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    key_file = db.Column(db.BLOB()) 


