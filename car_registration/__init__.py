from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "completly secret"
    app.config.from_object("car_registration.config.Config")
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    from car_registration.cars.routes import cars
    app.register_blueprint(cars)
    
    from car_registration.owner.routes import owner
    app.register_blueprint(owner)
    
    from car_registration.main.routes import main
    app.register_blueprint(main)

    return app