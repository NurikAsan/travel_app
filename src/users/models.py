import logging
from typing import Any
from passlib.hash import bcrypt
from src.db import db


Base = db.Model


class User(Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, **kwargs: Any) -> None:
        self.full_name = kwargs.get('full_name')
        self.email = kwargs.get('email')
        self.password = bcrypt.hash(kwargs.get('password'))

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            logging.warning(str(e))
            db.session.rollback()
