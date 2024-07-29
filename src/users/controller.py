from .models import User
from .schema import UserSchema
from flask import Blueprint
from flask_apispec import use_kwargs
from src import logger, docs

users = Blueprint('users', __name__)


@users.route('/api/v1/register', methods=['POST'])
@use_kwargs(UserSchema)
def registration(**kwargs):
    try:
        user = User(**kwargs)
        user.save()
    except Exception as e:
        logger.warning(f'User not created')
        return str(e)
    return UserSchema().dump(user)

docs.register(registration, blueprint='users')