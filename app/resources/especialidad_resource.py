from flask import jsonify, Blueprint, request
from app.mapping.especialidad_mapping import EspecialidadMapping            
from app.services.especilidad_service import EspecialidadService
from markupsafe import escape   

especialidad_bp = Blueprint('especialidad', __name__)
especialidad_mapping = EspecialidadMapping()    

@ especialidad_bp.route('/especialidad/<int:id>', methods=['GET'])
def buscar_por_id(id):
    especialidad = EspecialidadService.buscar_especialidad(id)
    return especialidad_mapping.dump(especialidad), 200 

@especialidad_bp.route('/especialidad', methods=['POST'])
def crear():
    especialidad = especialidad_mapping.load(request.get_json())
    EspecialidadService.crear_especialidad(especialidad)
    return jsonify("Especialidad creada exitosamente"), 201

@especialidad_bp.route('/especialidad/<int:id>', methods=['PUT'])
def actualizar(id):
    especialidad = especialidad_mapping.load(request.get_json())
    EspecialidadService.actualizar_especialidad(especialidad, id)
    return jsonify("Especialidad actualizada exitosamente"), 200        

@especialidad_bp.route('/especialidad/<int:id>', methods=['DELETE'])
def borrar_por_id(id):
    EspecialidadService.eliminar_especialidad(id)
    return jsonify("Especialidad borrada exitosamente"), 200    

def sanitizar_especialidad_entrada(request):
    especialidad = especialidad_mapping.load(request.get_json())
    especialidad.nombre = escape(especialidad.nombre)
    especialidad.letra = escape(especialidad.letra)
    especialidad.observacion = escape(especialidad.observacion)
    return especialidad 


