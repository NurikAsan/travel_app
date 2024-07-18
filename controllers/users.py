from app import app
from flask import request
from models.user import User
from models import db
from schema.user import UserSchema


@app.route('api/v1/register', methods=['POST'])
def register():
    try:
        user = User(**request.json)
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return str(e)
    return UserSchema().dump(user)


@app.route('api/v1/login', methods=['POST'])
def login():
    try:
        user = User(**request.json)
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return str(e)
    return 'Hello World'
