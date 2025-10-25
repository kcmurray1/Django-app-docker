from app.models import User, Tag, Post, db


def UserSerializer(data: User | list[User]):
    """Cnvert User object to JSON"""
    
    users = list()
    for user in data:
        print(user)
        users.append({"id": user.id, "name": user.name})
    return users
