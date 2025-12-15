from flask.views import MethodView
from flask import make_response, request
from app.models import db, Tag, User, Post
from app.serializer import UserSchema, TagSchema, PostSchema
from sqlalchemy import select, delete

class UserCollection(MethodView):
    def get(self):
        users = db.session.execute(select(User)).scalars()
        return make_response({"users": [UserSchema().dump(user) for user in users]},200)
    

    def post(self):
        try:
            data = request.get_json()

            new_user = UserSchema().load(data=data, session=db.session)
            # NOTE: check if user adds additional parameters?
            db.session.add(new_user)
            db.session.commit()
            return make_response({"created": UserSchema().dump(new_user)}, 201)
        except Exception as e:
            # NOTE: probably change this to prevent user from understanding backend code
            return make_response({"error": str(e)}, 500)
        

class UserRecord(MethodView):
    def get(self, id):
        user = db.session.execute(select(User).where(User.id == id)).scalar_one_or_none()
        if not user:
            return make_response({"error": "user does not exist"}, 400)
        return make_response({"users": UserSchema().dump(user)},200)


    def delete(self, id):
        db.session.execute(delete(User).where(User.id == id))
        db.session.commit()
        return make_response({"result": "deleted"}, 200)
