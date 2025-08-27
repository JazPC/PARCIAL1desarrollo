from flask import jsonify, Blueprint, request 
from app.mapping.autoridad_mapping import AutoridadMapping
from app.services.autoridad_service import AutoridadService
from markupsafe import escape

autoridad_bp = Blueprint('autoridad', __name__)
autoridad_mapping = AutoridadMapping()

@autoridad_bp.route('/autoridad/<hashid:id>', methods=['GET']) 
def buscar_por_id(id):
    autoridad =AutoridadService.buscar_por_id(id)
    return autoridad_mapping.dump(autoridad), 200

@autoridad_bp.route('/autoridad', methods=['GET'])
def obtener_todas():
    autoridades = AutoridadService.buscar_todas() 
    resultado = autoridad_mapping.dump(autoridades, many=True)  # Serializa la lista
    return jsonify(resultado), 200

@autoridad_bp.route('/autoridad', methods=['POST'])
def crear():
    autoridad = autoridad_mapping.load(request.get_json())
    AutoridadService.crear_autoridad(autoridad)
    return jsonify("autoridad creada exitosamente"), 201 

@autoridad_bp.route('/autoridad/<hashid:id>', methods=['PUT']) 
def actualizar(id):
    autoridad = autoridad_mapping.load(request.get_json()) 
    AutoridadService.actualizar_autoridad (id,autoridad)
    return jsonify("autoridad actualizada exitosamente"), 200 

@autoridad_bp.route('/autoridad/<hashid:id>', methods=['DELETE'])
def borrar_por_id(id):
    autoridad = AutoridadService.borrar_autoridad(id)
    return jsonify("autoridad borrada exitosamente"), 200 

def sanitizar_autoridad_entrada(request):
    autoridad = autoridad_mapping.load(request.get_json())
    autoridad.nombre = escape(autoridad.nombre)
    autoridad.telefono = escape(autoridad.telefono)
    autoridad.email = escape(autoridad.email) 
    return autoridad





