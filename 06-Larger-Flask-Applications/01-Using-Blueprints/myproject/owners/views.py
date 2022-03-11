from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddForm


# kind of micro-app
owners_blueprint = Blueprint(
    name='owners',
    import_name= __name__,
    template_folder='templates/owners' # relative to blueprint's root path
)


@owners_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data

        new_owner = Owner(name, pup_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('puppies.list'))
    return render_template('add_owner.html',form=form)
