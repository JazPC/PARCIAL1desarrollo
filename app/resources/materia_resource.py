from flask import jsonify, Blueprint, request
from app.mapping.materia_mapping import MateriaMapping
from app.services.materia_service import MateriaService
from markupsafe import escape

materia_bp = Blueprint('materia', __name__)
materia_mapping = MateriaMapping()

@materia_bp.route('/materia/<hashid:id>', methods=['GET'])
def buscar_por_id(id):
    materia = MateriaService.buscar_por_id(id)
    return materia_mapping.dump(materia), 200

@materia_bp.route('/materia', methods=['GET'])
def obtener_todas():
    materias = MateriaService.buscar_todas()  # Método que devuelve todas las materias
    resultado = materia_mapping.dump(materias, many=True)  # Serializa la lista
    return jsonify(resultado), 200

@materia_bp.route('/materia', methods=['POST'])
def crear():
    materia = materia_mapping.load(request.get_json())
    MateriaService.crear_materia(materia)
    return jsonify("Materia creada exitosamente"), 201

@materia_bp.route('/materia/<hashid:id>', methods=['PUT'])
def actualizar(id):
    materia = materia_mapping.load(request.get_json())
    MateriaService.actualizar_materia(id, materia)
    return jsonify("Materia actualizada exitosamente"), 200

@materia_bp.route('/materia/<hashid:id>', methods=['DELETE'])
def borrar_por_id(id):
    MateriaService.borrar_materia(id)
    return jsonify("Materia borrada exitosamente"), 200

def sanitizar_materia_entrada(request):
    materia = materia_mapping.load(request.get_json())
    if isinstance(materia.nombre, str):
        materia.nombre = escape(materia.nombre)
    if isinstance(materia.diseno_curricular, str):
        materia.diseno_curricular = escape(materia.diseno_curricular)
    if isinstance(materia.horas_dictadas, str):
        materia.horas_dictadas = escape(materia.horas_dictadas)
    if isinstance(materia.nivel, str):
        materia.nivel = escape(materia.nivel)
    return materia

