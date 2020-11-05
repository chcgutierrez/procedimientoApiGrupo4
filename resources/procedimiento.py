from flask import Response, request
from database.procedimiento import Procedimiento
from flask_restful import Resource

class ProcedimientoApi(Resource):
    def get(self):
        procedimiento = Procedimiento.objects().to_json()
        return Response(procedimiento, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        procedimiento = Procedimiento(**body).save()
        procedim_id = procedimiento.id
        return {'id': str(id)}, 200
