from flask import Flask

from app.models import db, User, Tag, Post

def create_app():
    app = Flask(__name__)

    from .blueprints.api import api_bp
    app.register_blueprint(api_bp)

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app

