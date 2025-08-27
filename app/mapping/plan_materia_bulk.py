# schemas/plan_materia_bulk.py
from marshmallow import Schema, fields
from app.mapping import PlanMateriaMapping

class BulkMateriasMapping(Schema):
    materias = fields.List(fields.Nested(PlanMateriaMapping), required=True)
