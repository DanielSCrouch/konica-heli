from flask_restful import Resource
from flask_jwt import jwt_required

from models.heliport import Heliport


# POST /robots data: {name:}
class Heliport(Resource):
    heliport = Heliport(5) 

    # /heli
    @jwt_required()
    def get(self, name):
        """Return if space avliable"""
        pad_id = self.heliport.request_land()
        if pad_id: 
            return {'message': f"cleared to land", "pad_id": pad_id}, 200
        else:
            return {'message': f"request denied"}, 400 
    
    # '/heli/<string:pad_id>'
    @jwt_required()
    def post(self, pad_id):
        """Land on helipad"""
        if self.heliport.land(pad_id):
            return {'message': "land successful"}, 201
        else: 
            return {'crash landing': "landing did'nt go so well"}, 500
    
    # /heli
    @jwt_required()
    def delete(self, pad_id):
        """Request to leave helipad"""
        if self.heliport.leave(pad_id): 
            return {'message': "helli has left the building!"}, 204
        else: 
            return {'error': "couldn't find your helicopter"}, 400


