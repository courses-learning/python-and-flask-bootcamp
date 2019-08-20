from user import User
users = [User(1, 'David', 'mypassword'),
         User(2, 'Nicola', 'secret')]

user_name_table = {u.username: u for u in users}
user_id_table = {u.id: u for u in users}


def authenticate(username, password):
    user = user_name_table.get(username, None)
    if user and password == user.password:
        return user


def identity(payload):
    user_id = payload['identity']
    return user_id_table.get(user_id, None)
