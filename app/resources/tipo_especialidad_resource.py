from flask import jsonify, Blueprint, request
from app.mapping.tipo_especialidad_mapping import TipoEspecialidadMapping
from app.services.tipoespecialidad_service import TipoespecialidadService      
from markupsafe import escape   

tipo_especialidad_bp = Blueprint('tipo_especialidad', __name__)
tipo_especialidad_mapping = TipoEspecialidadMapping()

@tipo_especialidad_bp.route('/tipo_especialidad/<int:id>', methods=['GET'])
def buscar_por_id(id):
    tipo_especialidad = TipoespecialidadService.buscar_tipoespecialidad(id)
    return tipo_especialidad_mapping.dump(tipo_especialidad), 200

@tipo_especialidad_bp.route('/tipo_especialidad', methods=['POST'])
def crear():
    tipo_especialidad = tipo_especialidad_mapping.load(request.get_json())
    TipoespecialidadService.crear_tipoespecialidad(tipo_especialidad)
    return jsonify("Tipo de especialidad creado exitosamente"), 201     

@tipo_especialidad_bp.route('/tipo_especialidad/<int:id>', methods=['PUT'])
def actualizar(id):
    tipo_especialidad = tipo_especialidad_mapping.load(request.get_json())
    TipoespecialidadService.actualizar_tipoespecialidad(tipo_especialidad, id)
    return jsonify("Tipo de especialidad actualizado exitosamente"), 200

@tipo_especialidad_bp.route('/tipo_especialidad/<int:id>', methods=['DELETE'])
def borrar_por_id(id):
    tipo_especialidad = TipoespecialidadService.eliminar_tipoespecialidad(id)
    return jsonify("Tipo de especialidad borrado exitosamente"), 200

def sanitizar_tipo_especialidad_entrada(request):
    tipo_especialidad = tipo_especialidad_mapping.load(request.get_json())
    tipo_especialidad.nombre = escape(tipo_especialidad.nombre)
    tipo_especialidad.nivel = escape(tipo_especialidad.nivel)
    return tipo_especialidad
