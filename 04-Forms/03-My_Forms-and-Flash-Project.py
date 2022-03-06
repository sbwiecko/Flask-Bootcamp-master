from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class SimpleForm(FlaskForm):
    breed = StringField(label='What breed are you?')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        # we get the data inside the `breed` Field
        # could also save it into the session dict
        # session['breed']=form.breed.data
        flash(f"You just typed the {mess} breed!") if (mess := form.breed.data) else flash("You didn't enter any breed")

        return redirect(url_for('index'))
    return render_template('03-my_home.html', form=form)


if __name__ == '__main__':
    app.run(debug=True) 
