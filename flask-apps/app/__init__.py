from flask import Flask
from flask_cors import CORS
from app.models import db, User, Tag, Post
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)
    CORS(app)
    from .urls import view_bp

    app.register_blueprint(view_bp)

    load_dotenv()
    #  f"sqlite:///{os.getenv('DB_NAME', "///:memory:")}.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///:memory:"

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app

