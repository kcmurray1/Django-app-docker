
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


def serailize_general(instance, plus=None):

    attributes = [col.key for col in instance.__table__.columns] 

    if plus:
        attributes.extend(plus if isinstance(plus, list) else [plus])

    res = {attr : getattr(instance, attr) for attr in attributes}

    print(res)

    return res


   
        
  

def test_validation(app):
    with app.app_context():
        data = {"name" : "John"}

        invalid_data = {"name" : "John", "age": 45}

        res = validate_model(User, data)

        assert res == True
        t = Tag(name="Funny")
        x = User(name=data['name'])
        p = Post(content="""This is a long body of text that is a part of a post. Thist post was made to test sqlalchemy models.""", author_id=1)
        p.tags.append(t)
        db.session.add_all([x,p, t])
        db.session.commit()
        serailize_general(x, "posts")
        serailize_general(p)
        serailize_general(t)
        
        print(t)
        print(x)
        print(p)
        # print(x.posts, p.tags, p.author)
        res = validate_model(User, invalid_data)

        assert res == False


        