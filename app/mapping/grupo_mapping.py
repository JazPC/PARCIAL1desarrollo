from marshmallow import Schema, fields, post_load, validate
from markupsafe import escape
from app.models import Grupo

class GrupoMapping(Schema):
    hashids = fields.String(attribute="hashid", dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=100))

    @post_load
    def nuevo_grupo(self, data, **kwargs):  
        for campo in ['nombre']:
            if isinstance(data.get(campo), str):
                data[campo] = escape(data[campo])
        return Grupo(**data)

