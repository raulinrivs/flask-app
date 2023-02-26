from flask import Blueprint
from flask import render_template
from .forms import CarForm
from car_registration.models import Owner, Car
from car_registration import db


cars = Blueprint('cars', __name__)

@cars.route('/car', methods=['GET', 'POST'])
def create_car():
    car = None
    form = CarForm()
    form.owner_id.choices = [(p.id, p.name) for p in Owner.query.order_by('name')]
    if form.validate_on_submit():
        cars_already_owned = Car.query.filter_by(owner_id=form.owner_id.data)
        print(f'Len owned: {cars_already_owned.count()}')
        if cars_already_owned.count() >= 3:
            car = f'Maxium cars already owned'
        else:    
            car = Car(color=form.color.data, car_type=form.car_type.data, owner_id=form.owner_id.data)
            db.session.add(car)
            db.session.commit()
            car = f'Car {form.car_type.data} {form.color.data} added for {form.owner_id.data}'
    return render_template(
        'add_car.html', 
        form = form,
        car = car
    )