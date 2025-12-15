from flask.views import MethodView
from flask import make_response, request
from app.models import db, Tag, User, Post
from app.serializer import PostSchema
from sqlalchemy import select, delete

class PostCollection(MethodView):
    def get(self):
        posts = db.session.execute(select(Post)).scalars()

        return make_response({"posts": [PostSchema().dump(post) for post in posts]}, 200)

    def post(self):
        try:
            # NOTE: check if post adds additional parameters?
            data = request.get_json()

            new_post = PostSchema().load(data=data, session=db.session)
            db.session.add(new_post)
            db.session.commit()
            return make_response({"result": "created"}, 201)
        except Exception as e:
            # NOTE: probably change this to prevent post from understanding backend code
            return make_response({"error": str(e)}, 500)


class PostRecord(MethodView):
    def get(self, id):
        post = db.session.execute(select(Post).where(Post.id==id)).scalar_one_or_none()

        if not post:
            return make_response({"error": "post does not exist"}, 400)
        return make_response({"post" : PostSchema().dump(post)}, 200)
    
    def delete(self, id):
        db.session.execute(delete(Post).where(Post.id == id))
        db.session.commit()
        return make_response({"result": "deleted"}, 200)
