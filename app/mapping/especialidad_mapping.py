from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models.especialidad import Especialidad

class EspecialidadMapping(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    letra = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    observacion = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    facultad_id = fields.Int(load_only=True, allow_none=True)  # No es requerido

    @post_load
    def nueva_especialidad(self, data, **kwargs):
        for campo in ['nombre', 'letra', 'observacion']:
            if isinstance(data.get(campo), str):
                data[campo] = escape(data[campo])
        return Especialidad(**data)
