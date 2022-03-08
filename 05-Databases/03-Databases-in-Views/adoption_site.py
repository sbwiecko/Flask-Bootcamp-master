import os

from forms import  AddForm, DelForm, AddOwnerForm

from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY']='mysecretkey'


###########################
# SQL DATABASE AND MODELS #
###########################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

# could also define the class in a different file
class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)

    # This is a ONE-TO-ONE relationship
    # ONE puppy only has ONE owner, thus uselist is False.
    # Strong assumption of 1 dog per 1 owner and vice versa.
    owner = db.relationship('Owner', backref='puppy', uselist=False)
    # in a one-to-one relationship, no need to get a list of relationships
    # as there will be only one, i.e. one owner (default=True)


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner.name}"
            # the Puppy object has a Owner object as an attribute,
            # we get its name as an attribute of the object attribute...
        else:
            return f"Puppy name is {self.name} and has no owner assigned yet."

class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Text)

    # We use puppies.id because __tablename__='puppies'
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id


####################
# VIEWS WITH FORMS #
####################

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add', methods=['GET','POST'])
def add_pup():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        # Add new Puppy to database
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add.html', form=form)


@app.route('/list')
def list_pup():
    # Grab a list of puppies from database.
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@app.route('/add_owner')
def add_owner():
    
    form = AddOwnerForm()

    if form.validate_on_submit():
        id_pup = form.id_pup.data
        pup = Puppy.query.get(id_pup)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html', form=form)


@app.route('/delete', methods=['GET','POST'])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
