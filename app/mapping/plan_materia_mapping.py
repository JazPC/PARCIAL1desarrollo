from marshmallow import Schema, fields, post_load, validate 
from app.models.plan_materia import PlanMateria

class PlanMateriaMapping(Schema):
    hashids = fields.String(attribute="hashid", dump_only=True)
    materia_id = fields.Integer(required=True, load_only=True)
    materia_hashid = fields.String(attribute="materia.hashid", dump_only=True)  # solo salida
    materia_nombre = fields.String(attribute="materia.nombre", dump_only=True)
    anio = fields.Integer(required=True, validate=validate.Range(min=1, max=12))
    dictado = fields.String(required=True, validate=validate.Length(max=10))
    se_cursa = fields.Boolean(load_default=True)
    se_rinde = fields.Boolean(load_default=True)
    orden = fields.Integer(load_default=0)
    
    @post_load
    def nuevo_plan_materia(self, data, **kwargs):
        return PlanMateria(**data)