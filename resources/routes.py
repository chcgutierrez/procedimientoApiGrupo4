from .client import ClientsApi, ClientApi
from .paciente import PacienteApi
from .procedimiento import ProcedimientoApi

def initialize_routes(api):
    api.add_resource(ClientsApi, '/api/clients')
    api.add_resource(ClientApi, '/api/client/<id>')

    api.add_resource(PacienteApi, '/api/paciente')
    api.add_resource(ProcedimientoApi, '/api/procedimiento')
