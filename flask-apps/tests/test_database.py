
from flask_sqlalchemy import SQLAlchemy, model
from app.models import User, Post, Tag, db
from app import create_app
import pytest


@pytest.fixture()
def app():
    app = create_app()

    yield app


def validate_model(class_type, values):
    if isinstance(class_type, model.DefaultMeta):
        for key in values:
            if key not in class_type.__table__.columns:
                return False
        return True
    else:
        return False
  

def test_validation(app):
    with app.app_context():
        data = {"name" : "John"}

        invalid_data = {"name" : "John", "age": 45}

        res = validate_model(User, data)

        assert res == True

        x = User(name=data['name'])

        res = validate_model(User, invalid_data)

        assert res == False


        