from flask import render_template
from flask import Blueprint
from .forms import OwnerForm
from car_registration.models import Owner
from car_registration import db

owners = Blueprint('owners', __name__)

@owners.route('/owner', methods=['GET', 'POST'])
def create_owner():
    name = None
    form = OwnerForm()
    if form.validate_on_submit():
        owner = Owner(name=form.name.data)
        db.session.add(owner)
        db.session.commit()
        name = f'{form.name.data} added'
    return render_template(
        'add_owner.html', 
        form = form,
        name = name
    )