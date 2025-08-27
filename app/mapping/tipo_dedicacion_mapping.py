from marshmallow import Schema, fields, post_load, validate 
from app.models.tipoDedicacion import TipoDedicacion
from markupsafe import escape

class Tipo_dedicacionMapping(Schema):
    hashids = fields.String(attribute='hashid', dump_only=True) 
    nombre = fields.String(required=True, validate = validate.Length(min=1, max=100))
    observacion = fields.String(required=True, validate = validate.Length(min=1, max=100))
    
    @post_load
    def nueva_tipo_dedicacion(self, data, **kwargs):
        for key in ['nombre', 'observacion']:
            if key in data:
                data[key] = escape(data[key])
        return TipoDedicacion(**data)

