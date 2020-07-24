from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db

from security import authenticate, identity
from resource.user import UserRegister
from resource.heliportR import Heliport

app = Flask(__name__)  # module name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'xxxxx'
api = Api(app)
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()

app = Flask(__name__)  # module name

app.secret_key = 'xxxxx'
api = Api(app)

# authentication
# creates a new endpoint /auth that required a username and a password
jwt = JWT(app, authenticate, identity)


api.add_resource(Heliport, '/heli/<string:name>')


api.add_resource(UserRegister, '/register')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
