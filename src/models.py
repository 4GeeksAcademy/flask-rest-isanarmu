from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(
        String(13), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    posts: Mapped[list["Post"]] = relationship(back_populates="author")
    followers: Mapped[list["User"]] = relationship(back_populates="following")


class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(200), nullable=False)
    link: Mapped[str] = mapped_column(unique=True, nullable=False)
    userid: Mapped[int] = mapped_column(
        ForeignKey('user.id'), nullable=False)
    author: Mapped["User"] = relationship(back_populates="posts")


class Followers(db.Model):
    __tablename__ = "followers"

    id: Mapped[int] = mapped_column(
        primary_key=True)
    followerid: Mapped[int] = mapped_column(
        ForeignKey('user.id'), nullable=False)
    followedid: Mapped[int] = mapped_column(
        ForeignKey('user.id'), nullable=False)


class Actions(db.Model):
    __tablename__ = "actions"

    id: Mapped[int] = mapped_column(
        primary_key=True)
    like: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    postid: Mapped[int] = mapped_column(
        ForeignKey('post.id'), nullable=False)
    userid: Mapped[int] = mapped_column(
        ForeignKey('user.id'), nullable=False)


class Comment_section(db.Model):
    __tablename__ = "comment"

    id: Mapped[int] = mapped_column(
        primary_key=True)
    comment: Mapped[str] = mapped_column(
        String(200), nullable=False)
    postid: Mapped[int] = mapped_column(
        ForeignKey('post.id'), nullable=False)
    userid: Mapped[int] = mapped_column(
        ForeignKey('user.id'), nullable=False)

    post: Mapped["Post"] = relationship(back_populates="comment")


def serialize(self):
    return {
        "id": self.id,
        "comment": self.comment,
        "postid": self.postid,
        "userid": self.userid,
    }
