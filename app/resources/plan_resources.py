from flask import jsonify, Blueprint, request 
from app.mapping import PlanMapping, PlanMateriaMapping, BulkMateriasMapping
from app.services.plan_service import PlanService
from app.validators import validate_with

from marshmallow import ValidationError

plan_bp = Blueprint('plan', __name__)
plan_mapping = PlanMapping()
plan_materia_mapping = PlanMateriaMapping()
bulk_mapping = BulkMateriasMapping()

@plan_bp.route('/plan', methods=['GET'])
def buscar_todos():
    planes = PlanService.buscar_todos()
    return plan_mapping.dump(planes, many=True), 200 

@plan_bp.route('/plan/materias', methods=['GET'])
def buscar_todas_las_materias():
    materias = PlanService.buscar_todos_plan_materia()
    return plan_materia_mapping.dump(materias, many=True), 200

@plan_bp.route('/plan/<hashid:id>', methods=['GET']) 
def buscar_por_id(id):
    plan = PlanService.buscar_por_id(id)
    return plan_mapping.dump(plan), 200

@plan_bp.route('/plan', methods=['POST']) 
@validate_with(PlanMapping)
def crear():
    plan = plan_mapping.load(request.get_json())
    PlanService.crear(plan)
    return jsonify("Plan creado exitosamente"), 201 

@plan_bp.route('/plan/<hashid:id>/materias', methods=['POST'])
def agregar_materias(id):
    try:
        data = bulk_mapping.load(request.get_json() or {})
        pms = data["materias"]  # lista de PlanMateria
    except ValidationError as e:
        return jsonify({"errors": e.messages}), 400

    PlanService.agregar_materias(id, pms)
    return jsonify({"message": "Materias agregadas exitosamente"}), 201

@plan_bp.route('/plan/<hashid:id>', methods=['PUT'])  
@validate_with(PlanMapping)
def actualizar(id):
    plan = plan_mapping.load(request.get_json())
    actualizado = PlanService.actualizar(id, plan)
    if actualizado is None:
        return jsonify("Plan no encontrado"), 404
    return jsonify("Plan actualizado exitosamente"), 200

@plan_bp.route('/plan/<hashid:id>', methods=['DELETE'])
def borrar_por_id(id):
    plan = PlanService.borrar_por_id(id)
    if plan is None:
        return jsonify("Plan no encontrado"), 404
    return jsonify("Plan borrado exitosamente"), 200