from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="Must include a username")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="Must include a password")

    # /register
    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': f"Username {data['username']} \
                            not avaliable."}, 409

        user = UserModel(**data)
        user.save_to_db()

        return {'message': "User created successfully."}, 201
