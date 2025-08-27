from marshmallow import Schema, fields, post_load, validate 
from app.models.plan import Plan

class PlanMapping(Schema):
    hashids = fields.String(attribute="hashid", dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    fechaInicio = fields.String(required=True, validate=validate.Length(min=1, max=100))
    fechaFin = fields.String(required=True, validate=validate.Length(min=1, max=50))
    observacion = fields.String(required=True, validate=validate.Length(min=1, max=50))
    
    @post_load
    def nuevo_plan(self, data, **kwargs):
        return Plan(**data)