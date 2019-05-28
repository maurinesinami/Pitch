from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pitches_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    comments = db.relationship("Comment", backref="user", lazy = "dynamic")
    pass_secure = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    # @password.setter
    # def password(self, password):
    #     self.password_hash = generate_password_hash(password)


    # def verify_password(self,password):
    #     return check_password_hash(self.password_hash,password) 
    # 
    @password.setter
    def password(self, password):
        self.pass_secure= generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)  
class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship("User", backref = "pitch", lazy = "dynamic")
    category = db.Column(db.String)

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'
class Comment(db.Model):
    
    __tablename__= "comments"

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

def init_db():
    db.session.add()
    db.session.commit()

if __name__ == '__main__':
    init_db()
