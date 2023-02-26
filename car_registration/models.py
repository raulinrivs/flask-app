from datetime import datetime
import enum
from car_registration import db

class CarColorsEnum(enum.Enum):
    yellow = 'yellow'
    blue = 'blue'
    gray = 'gray'
    
class CarTypeEnum(enum.Enum):
    hatch = 'hatch'
    sedan = 'sedan'
    convertible = 'convertible'
    
class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    owner = db.relationship('Car', backref='post')
    
    
    def __repr__(self) -> str:
        return '<Owner %r>' % self.id
    
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.Enum(CarColorsEnum), nullable=False)
    car_type = db.Column(db.Enum(CarTypeEnum), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    owner_id = db.Column(db.Integer, db.ForeignKey('Owner.id'))
    
    def __repr__(self) -> str:
        return '<Car %r>' % self.id