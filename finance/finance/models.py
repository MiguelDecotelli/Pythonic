from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from finance import login_manager, db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, index=True)
    password_hash = Column(String(128))
    cash = Column(Float(16), default=10000)
    transactions = db.relationship('Transactions', backref='user', lazy='dynamic')

    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Portfolio(db.Model):
    __tablename__ = 'portfolio'
    id = Column(Integer, primary_key=True)
    symbol = Column(String(16))
    name = Column(String(64))
    shares = Column(Integer)
    transactions = db.relationship('Transactions', backref='portfolio', lazy='dynamic')

class Transactions(db.Model):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('portfolio.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    transaction_time = Column(DateTime(64))
    price = Column(Float(32))
    total = Column(Float(16))