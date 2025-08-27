from marshmallow import Schema, fields, post_load, validate 
from app.models.cargo import Cargo

class CargoMapping(Schema):
    hashids = fields.String(attribute="hashid", dump_only=True)
    nombre = fields.String(required=True, validate = validate.Length(min=1, max=100))  
    puntos = fields.Integer(required=True, validate=validate.Range(min=0))
    categoria_cargo_id = fields.Integer(required=True, load_only=True) 
    categoria = fields.Nested('CategoriaCargoMapping', only=('hashids', 'nombre'), dump_only=True)
    autoridades = fields.List(fields.Nested('AutoridadMapping', only=('hashids', 'nombre')), dump_only=True)

    @post_load
    def nuevo_cargo(self, data, **kwargs):
        return Cargo(**data)