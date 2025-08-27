from marshmallow import Schema, fields, post_load, validate 
from app.models.categoria_cargo import CategoriaCargo

class CategoriaCargoMapping(Schema):
    hashids = fields.String(attribute="hashid", dump_only=True)
    nombre = fields.String(required=True, validate = validate.Length(min=1, max=100)) 
    
    @post_load
    def nuevo_categoria_cargo(self, data, **kwargs):
        for key in ['nombre']:
            if key in data:
                data[key] = escape(data[key])
        return CategoriaCargo(**data)