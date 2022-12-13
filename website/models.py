from sqlalchemy.sql import func
from . import db
from dataclasses import dataclass
from flask_login import UserMixin


@dataclass
class User(db.Model, UserMixin):
    id: int = db.Column(db.Integer, primary_key=True)
    uid: str = db.Column(db.String(500), unique=True)
    first_name: str = db.Column(db.String(150))
    email: str = db.Column(db.String(150))
    password: str = db.Column(db.String(150))


