from flask import jsonify, Blueprint, request
from app.mapping.grado_mapping import GradoMapping
from app.services.grado_service import GradoService
from markupsafe import escape
from app.validators import validate_with

grado_bp = Blueprint('grado', __name__)

grado_mapping = GradoMapping()

@grado_bp.route('/grado/<hashid:id>', methods=['GET'])
def buscar_por_id(id):
    grado = GradoService.buscar_grado(id)
    return grado_mapping.dump(grado), 200

@grado_bp.route('/grado', methods=['GET'])
def listar_grados():
    grados = GradoService.listar_grados()
    return grado_mapping.dump(grados, many=True), 200

@grado_bp.route('/grado', methods=['POST'])
@validate_with(GradoMapping)
def crear():
    grado = grado_mapping.load(request.get_json())
    GradoService.crear_grado(grado)
    return jsonify("Grado creado exitosamente"), 201

@grado_bp.route('/grado/<hashid:id>', methods=['PUT'])
@validate_with(GradoMapping)
def actualizar(id):
    grado = grado_mapping.load(request.get_json())
    GradoService.actualizar_grado(grado, id)
    return jsonify("Grado actualizado exitosamente"), 200

@grado_bp.route('/grado/<hashid:id>', methods=['DELETE'])
def borrar_por_id(id):
    GradoService.eliminar_grado(id)
    return jsonify("Grado borrado exitosamente"), 200

def sanitizar_grado_entrada(request):
    grado = grado_mapping.load(request.get_json())
    grado.nombre = escape(grado.nombre)
    return grado