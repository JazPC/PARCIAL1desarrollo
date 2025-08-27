from marshmallow import Schema, fields, post_load, validate
from app.models.tipoEspecialidad import TipoEspecialidad
from markupsafe import escape       

class TipoEspecialidadMapping(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    nivel = fields.String(required=True, validate=validate.Length(min=1, max=50))   

    @post_load
    def nuevo_tipo_especialidad(self, data, **kwargs):          
        for key in ['nombre', 'nivel']:
            if key in data and isinstance(data[key], str):
                data[key] = escape(data[key])
        return TipoEspecialidad(**data)     
    