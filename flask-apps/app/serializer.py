from app.models import User, Tag, Post, db


def serailize(instance, plus=None):

    attributes = [col.key for col in instance.__table__.columns] 

    if plus:
        attributes.extend(plus if isinstance(plus, list) else [plus])

    res = {attr : getattr(instance, attr) for attr in attributes}

    return res


def UserSerializer(data: User | list[User]):
    """Cnvert User object to JSON"""
    return [serailize(user) for user in data]

    

def PostSerializer(data):
    """"""
    return [serailize(post) for post in data]


def TagSerializer(data: User | list[User]):
    """Cnvert User object to JSON"""
    return [serailize(tag) for tag in data]