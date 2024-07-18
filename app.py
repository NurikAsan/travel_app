from app_creator import create_app
from models import db


app, logger = create_app(__name__)


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
