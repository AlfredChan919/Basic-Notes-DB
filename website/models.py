# database models
# db model for our users and for our notes(for this app)

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # everytime we create a new note, add into this notes relationship that id
    notes=db.relationship('Note')

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    # foreign key relationships
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))


# when youre doing foreign key its lower case, when its relationship you do the name of the class
# if you have many to one relationship, its different many to many is different

