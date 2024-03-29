from myproject import app, db # from __init__.py
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm

from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/welcome')
@login_required # the used should be logged in to see this view
def welcome_user():
    return render_template('welcome_user.html')


@app.route('/logout')
@login_required
def logout():
    logout_user() # Flask Login
    flash('You logged out!')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = User.query.filter_by(email=form.email.data).first() # email are unique
        
        # Check that the user was supplied and the password is correct
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

        if user is None:
            return redirect(url_for('register'))
        
        if user.check_password(form.password.data):
            login_user(user) # imported from Flask Login
            flash('Logged in successfully.')

            # If a user was trying to visit a page that requires
            # a login flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists,
            # otherwise we'll go to the welcome page.
            if next == None or not next[0]=='/':
                next = url_for('welcome_user')

            return redirect(next)
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data, # the User class uses the password hash
        )

        db.session.add(user)
        db.session.commit()

        flash('Thanks for registering! Now you can login!')
        
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
