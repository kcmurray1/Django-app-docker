from flask import make_response, Blueprint, request
from app.models import User, Tag, Post,db
from app.serializer import UserSerializer
from sqlalchemy import delete, update
import requests

api_bp = Blueprint("/api", __name__, url_prefix="/api")

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
        res = db.session.execute(db.select(User)).scalars()

        return make_response({"data": UserSerializer(res)}, 200)
    else:
        return make_response({"Invalid method"}, 400)
    


@api_bp.route("/user/<int:id>", methods=["GET", "PUT", "DELETE"])
def user_record(id):
    """return details of a single user"""
    if request.method == "GET":
        try:
            print(id)
            res = db.session.execute(db.select(User).where(User.id == id)).scalars()
            x = UserSerializer(res)
            if not x:
                return make_response({"error": "user does not exist"}, 400)
            return make_response(x, 200)
        except Exception as e:
            return make_response({"Error": str(e)}, 500)
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