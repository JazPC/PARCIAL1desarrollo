from marshmallow import Schema, fields, post_load, validate 
from app.models.facultad import Facultad
from markupsafe import escape


class FacultadMapping(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.String(required=True, validate = validate.Length(min=1, max=100)) #max de la base de datos
    sigla = fields.String(required=True, validate = validate.Length(min=1, max=10))
    codigoPostal = fields.String(required=True, validate = validate.Length(min=1, max=100))
    ciudad = fields.String(required=True, validate = validate.Length(min=1, max=100))   
    domicilio = fields.String(required=True, validate = validate.Length(min=1, max=100))
    telefono = fields.String(required=True, validate = validate.Length(min=1, max=100))
    contacto = fields.String(required=True, validate = validate.Length(min=1, max=100))
    email = fields.String(required=True, validate = validate.Length(min=1, max=100))
    abreviatura = fields.String(required=True, validate = validate.Length(min=1, max=100))
    directorio = fields.String(required=True, validate = validate.Length(min=1, max=100)) 

    @post_load
    def nueva_facultad(self, data, **kwargs):
        for key in ['nombre', 'sigla', 'codigoPostal', 'ciudad', 'domicilio', 'telefono', 'contacto', 'email', 'abreviatura', 'directorio']:
            if key in data:
                data[key] = escape(data[key])
        return Facultad(**data)


#json discriminan entre valores enteros y strings
#**kwargs el tercero es tipo clave valor
