from src.app_creator import create_app
from flask_apispec.extension import FlaskApiSpec
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from src.db import db
import logging


app = create_app(__name__)
app.config.from_object('configuration')
docs = FlaskApiSpec()


app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Ermak gay',
        version='v1',
        openapi_version='2.0',
        plugins=[MarshmallowPlugin()],
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',
})

def create_loger():
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler('log/api.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

logger = create_loger()


@app.teardown_appcontext
def shut_down(exception=None):
    db.session.remove()


from .users.controller import users
app.register_blueprint(users)

docs.init_app(app)
