from flask import Response, request
from database.procedimiento import Paciente
from flask_restful import Resource

class ProcedimientoApi(Resource):
    def get(self):
        procedimientos = Procedimiento.objects().to_json()
        return Response(procedimientos, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        procedimiento = Procedimiento(**body).save()
        procedim_id = procedimiento.id
        return {'id': str(id)}, 200
