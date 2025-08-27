from marshmallow import Schema, fields, post_load, validate 
from app.models.universidad import Universidad
from markupsafe import escape


class UniversidadMapping(Schema):
    hashids = fields.String(attribute="hashid", dump_only=True)
    nombre = fields.String(required=True, validate = validate.Length(min=1, max=100)) #max de la base de datos
    sigla = fields.String(required=True, validate = validate.Length(min=1, max=10))
    tipo = fields.Str(required=True) 

    @post_load
    def nueva_universidad(self, data, **kwargs):
        for key in ['nombre', 'sigla', 'tipo']:
            if key in data:
                data[key] = escape(data[key])
        return Universidad(**data)


#json discriminan entre valores enteros y strings
#**kwargs el tercero es tipo clave valor
