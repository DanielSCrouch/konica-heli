from flask_restful import Resource
from flask_jwt import jwt_required

from models.heliport import Heliport


# POST /robots data: {name:}
class Heliport(Resource):
    heliport = Heliport(5)

    # /heli
    # @jwt_required()
    def get(self, name):
        """Return if space avliable"""
        pad_id = self.heliport.request_land()
        if pad_id:
            return {'message': "cleared to land", "pad_id": pad_id}, 200
        else:
            return {'message': "request denied"}, 400

    # '/heli/<string:name>'
    @jwt_required()
    def post(self, name):
        """Land on helipad"""
        if self.heliport.land(name):
            return {'message': "land successful"}, 201
        else:
            return {'crash landing': "landing did'nt go so well"}, 500

    # /heli/<string:name>'
    @jwt_required()
    def delete(self, name):
        """Request to leave helipad"""
        print('pad id is:', name)
        if self.heliport.leave(name):
            return {'message': "helli has left the building!"}, 201
        else:
            return {'error': "couldn't find your helicopter"}, 400
