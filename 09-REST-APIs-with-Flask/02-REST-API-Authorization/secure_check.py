from user import User

# realistically this would be a database table!
users = [
    User(1, 'Jose', 'mypassword'),
    User(2, 'Mimi', 'secret')
]

# mapping users to usernames (dict comprehension)
username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    # check if user exists, otherwise return None
    user = username_table.get(username, None)
    if user and password == user.password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
