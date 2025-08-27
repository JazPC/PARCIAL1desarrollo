from flask import jsonify, Blueprint, request
from app.mapping.orientacion_mapping import OrientacionMapping
from app.services.orientacion_service import OrientacionService
from markupsafe import escape
from app.validators import validate_with

orientacion_bp = Blueprint('orientacion', __name__)

orientacion_mapping = OrientacionMapping()

@orientacion_bp.route('/orientacion/<hashid:id>', methods=['GET'])
def buscar_por_id(id):
    orientacion = OrientacionService.buscar_orientacion(id)
    return orientacion_mapping.dump(orientacion), 200

@orientacion_bp.route('/orientacion', methods=['GET'])
def listar_orientaciones():
    orientaciones = OrientacionService.listar_orientaciones()
    return orientacion_mapping.dump(orientaciones, many=True), 200

@orientacion_bp.route('/orientacion', methods=['POST'])
@validate_with(OrientacionMapping)
def crear():
    orientacion = orientacion_mapping.load(request.get_json())
    OrientacionService.crear_orientacion(orientacion)
    return jsonify("Orientación creada exitosamente"), 201

@orientacion_bp.route('/orientacion/<hashid:id>', methods=['PUT'])
@validate_with(OrientacionMapping)
def actualizar(id):
    orientacion = orientacion_mapping.load(request.get_json())
    OrientacionService.actualizar_orientacion(orientacion, id)
    return jsonify("Orientación actualizada exitosamente"), 200 

@orientacion_bp.route('/orientacion/<hashid:id>', methods=['DELETE'])
def borrar_por_id(id):
    OrientacionService.eliminar_orientacion(id)
    return jsonify("Orientación borrada exitosamente"), 200

