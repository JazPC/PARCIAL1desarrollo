from marshmallow import Schema, fields, post_load, validate 
from app.models.materia import Materia
from markupsafe import escape

class MateriaMapping(Schema):
    hashid = fields.String(attribute="hashid",dump_only=True) 
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    diseno_curricular = fields.String(required=True, validate=validate.Length(min=1, max=100))
    horas_dictadas = fields.String(required=True, validate=validate.Length(min=1, max=50))
    promocional = fields.Boolean(required=True)
    nivel = fields.String(required=True, validate=validate.Length(min=1, max=50))
    area_id = fields.Integer(required=False)
    
    @post_load
    def nueva_materia(self, data, **kwargs):
        # Escapar solo los strings
        for key in ['nombre', 'diseno_curricular', 'horas_dictadas', 'nivel']:
            if key in data and isinstance(data[key], str):
                data[key] = escape(data[key])
        return Materia(**data)

