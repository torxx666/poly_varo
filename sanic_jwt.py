from sanic import Sanic
from sanic_jwt import exceptions
from sanic_jwt import initialize

"""
I take from here :https://sanic-jwt.readthedocs.io/en/latest/pages/simpleusage.html

just copy/past and this not working with :


Traceback (most recent call last):
  File "sanic_jwt.py", line 2, in <module>
    from sanic_jwt import exceptions
  File "/Users/dany/Working/score/polyrise/poly_varo/sanic_jwt.py", line 2, in <module>
    from sanic_jwt import exceptions
ImportError: cannot import name 'exceptions' from partially initialized module 'sanic_jwt' 
(most likely due to a circular import) (/Users/dany/Working/score/polyrise/poly_varo/sanic_jwt.py)

env :
Package       Version
------------- -------
aiofiles      0.7.0
httptools     0.3.0
multidict     5.2.0
pip           20.2.3
PyJWT         2.1.0
sanic         21.9.1
sanic-jwt     1.7.0
sanic-routing 0.7.2
setuptools    49.2.1
ujson         4.2.0
uvloop        0.16.0
websockets    10.1


"""




class User:

    def __init__(self, id, username, password):
        self.user_id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return "User(id='{}')".format(self.user_id)

    def to_dict(self):
        return {"user_id": self.user_id, "username": self.username}


users = [User(1, "user1", "abcxyz"), User(2, "user2", "abcxyz")]

username_table = {u.username: u for u in users}
userid_table = {u.user_id: u for u in users}


async def authenticate(request, *args, **kwargs):
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    user = username_table.get(username, None)
    if user is None:
        raise exceptions.AuthenticationFailed("User not found.")

    if password != user.password:
        raise exceptions.AuthenticationFailed("Password is incorrect.")

    return user


app = Sanic()
initialize(app, authenticate=authenticate)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8888)



