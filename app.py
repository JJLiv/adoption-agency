from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import PetForm



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'

debug = DebugToolbarExtension(app)

with app.app_context():
    connect_db(app)



@app.route('/')
def index():
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)


@app.route('/add', ['GET', 'POST'])
def add_pet():
    """Pet add form; handle adding"""

    form = PetForm()
    if form.validate_on_submit():
        pet = Pet()

        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        db.session.add(pet)
        db.session.commit()

        flash(f"Added {pet.name} a {pet.species}")
        return redirect('/')
    else:
        return render_template('pet_add_form.html', form=form)
    

@app.route('/<int:pet_id>', ['GET', 'POST'])
def edit_pet(pet_id):
    """Show pet edit form and handle it"""

    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        db.session.commit()
        flash(f"Pet {pet_id} updated!")
        return redirect('/')
    else:
        return render_template("pet_edit_form.html", form=form)






