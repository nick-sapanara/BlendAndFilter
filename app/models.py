from hashlib import md5
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(64), index=True, unique=True)
   username = db.Column(db.String(64), index=True, unique=True)
   email = db.Column(db.String(120), index=True, unique=True)
   password_hash = db.Column(db.String(128))
   about_me = db.Column(db.String(140))

   u2s_list = db.relationship('User2Shop', backref='user', lazy='dynamic')

   def __repr__(self):
       return '<My_Account {}>'.format(self.username)

   def set_password(self, password):
       self.password_hash = generate_password_hash(password)

   def check_password(self, password):
       return check_password_hash(self.password_hash, password)

   def avatar(self, size):
       digest = md5(self.email.lower().encode('utf-8')).hexdigest()
       return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
           digest, size)
   # Does this need something like password_hash?

   # also are we still doing the other login pages from the model we made?


@login.user_loader
def load_user(id):
   return User.query.get(int(id))


class Shop(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   shopName = db.Column(db.String(64), index=True)
   ownerName = db.Column(db.String(64), index=True)
   address = db.Column(db.String(127), index=True)
   website = db.Column(db.String(127), index=True)
   about_shop = db.Column(db.String(140))

   u2s_list = db.relationship('User2Shop', backref='shop', lazy='dynamic')
   city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
   reviewDetails = db.relationship('ReviewDetails', backref='reviewDetails', lazy='dynamic')

   def __repr__(self):
       return '<Shop {}>'.format(self.shopName)


class User2Shop(db.Model):
   id = db.Column(db.Integer, primary_key=True)

   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)


class City(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(64), index=True, unique=True)
   country = db.Column(db.String(64), index=True)

   shop = db.relationship('Shop', backref='city', lazy='dynamic')

   def __repr__(self):
       return '<City {}>'.format(self.name)


class ReviewDetails(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   noiseLevel = db.Column(db.Integer, index=True)
   customerService = db.Column(db.Integer, index=True)
   liveMusic = db.Column(db.Boolean, index=True)
   atmosphere = db.Column(db.String(64), index=True)

   shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)

   def __repr__(self):
       return '<Vibes {}>'.format(self.title)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
