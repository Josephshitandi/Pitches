from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class Category(db.Model):

    __tablename__ = 'Categories'

    id = db.Column(db.Integer,primary_key = True)
    pitch_title = db.Column(db.String)
    pitch_category = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_category(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_Categories(cls,id):
        Categories = Category.query.filter_by(pitch_title=id).all()
        return Categories
  