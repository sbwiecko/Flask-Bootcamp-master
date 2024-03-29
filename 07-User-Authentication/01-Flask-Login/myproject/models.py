from myproject import db, login_manager

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin
# By inheriting the UserMixin we get access to a lot of built-in attributes
# which we will be able to call in our views!
# is_authenticated()
# is_active()
# is_anonymous()
# get_id()


# The user_loader decorator allows flask-login to load the
# current user and grab their id, specific to the login id.
@login_manager.user_loader # builtin decorator
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin): # inherited from multiple classes

    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    #                            v   limits the length of the string (e.g., spams)
    email = db.Column(db.String(64), unique=True, index=True) # no 2 users with the same e-mail address
    username = db.Column(db.String(64), unique=True, index=True) # no 2 users with the same username
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        # we don't save the actual password passed in but its hash
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
        return check_password_hash(self.password_hash, password)
