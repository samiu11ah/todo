from email.policy import default
from flask_login import UserMixin
from . import db
from datetime import datetime
import enum

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    username = db.Column(db.String(10), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(20))

    todos = db.relationship("Todo", backref="user", passive_deletes=True)
    categories = db.relationship("Category", backref="user", passive_deletes=True)

    def __repr__(self):
        return '<User %r>' % self.username





class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete='CASCADE'))
    # user -- Column Exists here
    title = db.Column(db.String(80), nullable=False)
    # category -- Colum Exits here
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete='CASCADE'))
    priority = db.Column(db.Integer, default=0)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Todo %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # user -- Column Exists here
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    name = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    todos = db.relationship("Todo", backref="category", passive_deletes=True)

    def __repr__(self):
        return '[Category %r]' % self.name

