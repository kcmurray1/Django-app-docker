from flask import Blueprint
from .views import user_views, post_view

view_bp = Blueprint('views', __name__, url_prefix='/views/v1')

view_bp.add_url_rule("/users", view_func=user_views.UserCollection.as_view("user_collection"))

view_bp.add_url_rule("/users/<int:id>", view_func=user_views.UserRecord.as_view("user_record"))
view_bp.add_url_rule("/posts", view_func=post_view.PostCollection.as_view("post_collection"))

view_bp.add_url_rule("/posts/<int:id>", view_func=post_view.PostRecord.as_view("post_record"))
