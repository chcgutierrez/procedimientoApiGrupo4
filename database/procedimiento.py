from .db import db

class Procedimiento(db.Document):
    procedim_id = db.StringField(required=True, unique=True)
    nombre = db.StringField(required=True)
    sexo = db.StringField(required=True)
    edad = db.ListField(db.StringField(), required=True)
    finalidad = db.ListField(db.StringField(), required=True)
    observacion = db.ListField(db.StringField(), required=False)
