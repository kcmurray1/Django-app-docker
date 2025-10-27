from flask import make_response, Blueprint, request
from app.models import User, Tag, Post,db
from app.serializer import UserSerializer, PostSerializer, TagSerializer
from sqlalchemy import delete, update
from flask_sqlalchemy import model
import requests

api_bp = Blueprint("/api", __name__, url_prefix="/api")

def validate_model(class_type, values):
    if isinstance(class_type, model.DefaultMeta):
        print(class_type.__table__.columns)
        for col in class_type.__table__.columns:
            if col.key != "id" and col.key not in values:
                print(col.key, "is missing")
                return False
        return True
    else:
        return False

def basic_get(class_type, class_serializer, id=None):
    try:
        # if no id is provided then will return collection
        if id:
            res = db.session.execute(db.select(class_type).where(class_type.id == id)).scalars()
            serialized_obj = class_serializer(res)

            if not serialized_obj:
                return make_response({"error": f"{id} does not exist"}, 400)
            return make_response({"data": serialized_obj}, 200)
        else:
            res = db.session.execute(db.select(class_type)).scalars()
            
            return make_response({"data": class_serializer(res)}, 200)
    except Exception as e:
        return make_response({"Error": str(e)}, 500)

@api_bp.route("/")
def status():
    return make_response({"result": "running"}, 200)


@api_bp.route("/user", methods=["GET", "POST"])
def user_collection():
    """"""
    
    if request.method == "POST":
        try:
            # NOTE: check if user adds additional parameters?
            new_user = User(name=request.json['name'])
            db.session.add(new_user)
            db.session.commit()
            return make_response({"result": "created"}, 201)
        except Exception as e:
            # NOTE: probably change this to prevent user from understanding backend code
            return make_response({"error": str(e)}, 500)
        
    elif request.method == "GET":
        return basic_get(User, UserSerializer)
    else:
        return make_response({"Invalid method"}, 400)
    


@api_bp.route("/user/<int:id>", methods=["GET", "PUT", "DELETE"])
def user_record(id):
    """return details of a single user"""
    if request.method == "GET":
        return basic_get(User, UserSerializer, id)
    
    elif request.method == "PUT":
        print(request.json)
        # db.session.execute(update(User).where(User.id == id).values(name=))
        return make_response({"result": "updated"}, 204)
    elif request.method == "DELETE":
        db.session.execute(delete(User).where(User.id == id))
        db.session.commit()
        return make_response({"result": "deleted"}, 200)
    else:
        return make_response({"error": "Invalid method"}, 400)
    

@api_bp.route("/post", methods=["GET", "POST"])
def post_collection():
    """"""
    
    if request.method == "POST":
        try:
            # NOTE: check if post adds additional parameters?
            if validate_model(Post, request.json):
                new_post = Post(content=request.json['content'], author_id=request.json['author_id'])
                db.session.add(new_post)
                db.session.commit()
                return make_response({"result": "created"}, 201)
        except Exception as e:
            # NOTE: probably change this to prevent post from understanding backend code
            return make_response({"error": str(e)}, 500)
        
    elif request.method == "GET":
        return basic_get(Post, PostSerializer)
    else:
        return make_response({"Invalid method"}, 400)
    


@api_bp.route("/post/<int:id>", methods=["GET", "PUT", "DELETE"])
def post_record(id):
    """return details of a single post"""
    if request.method == "GET":
        return basic_get(Post, PostSerializer, id)
    
    elif request.method == "PUT":
        return make_response({"result": "updated"}, 204)
    elif request.method == "DELETE":
        db.session.execute(delete(Post).where(Post.id == id))
        db.session.commit()
        return make_response({"result": "deleted"}, 200)
    else:
        return make_response({"error": "Invalid method"}, 400)