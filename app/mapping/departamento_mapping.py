from marshmallow import fields, Schema, post_load, validate
from app.models.departamento import Departamento
from markupsafe import escape

class DepartamentoMapping(Schema):
    hashids = fields.String(attribute="hashid", dump_only=True)
    nombre = fields.String(required=True, validate = validate.Length(min=1, max=100))
    
    @post_load
    def nuevo_departamento(self, data, **kwargs):
        for key in ['nombre']:
            if key in data:
                data[key] = escape(data[key])
        return Departamento(**data)
    
    
    
    