from sqlalchemy import ForeignKey, Table, Column, String, Text

from typing import List, Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


tag_post = Table(
    "tag_post",
    db.Model.metadata,
    Column("tags", ForeignKey("tags.id"), primary_key=True),
    Column("posts", ForeignKey("posts.id"), primary_key=True)
)

class User(db.Model):
    """Users can make posts"""
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)

    # One to many
    posts: Mapped[List["Post"]] = relationship(back_populates="author")

    @validates('name')
    def validate_name(self, key, value):
        print('validating..', key, value)

        return value

    def __repr__(self):
        return f"User: {self.id} {self.name}"

class Post(db.Model):
    """Post can be made by a single person"""
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(Text)

    # Many to one
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped[Optional["User"]] = relationship(back_populates="posts")

    # Many to many
    tags: Mapped[List["Tag"]] = relationship(secondary=tag_post, back_populates="posts")

    
    def __repr__(self):
        return f"Post {self.id} {self.tags} posted by {self.author} {self.content}"

class Tag(db.Model):
    """Each post can have many tags"""
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    name: Mapped[str] = mapped_column(String(100))

    posts: Mapped[List["Post"]] = relationship(secondary=tag_post, back_populates="tags")

    def __repr__(self):
        return f"Tag {self.id} {self.name}"