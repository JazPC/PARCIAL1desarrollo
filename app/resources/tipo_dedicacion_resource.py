from flask import jsonify, Blueprint, request 
from app.mapping.tipo_dedicacion_mapping import Tipo_dedicacionMapping
from app.services.tipoDedicacionService import TipoDedicacionService
from markupsafe import escape

tipo_dedicacion_bp = Blueprint('tipo_dedicacion', __name__)
tipo_dedicacion_mapping = Tipo_dedicacionMapping()

@tipo_dedicacion_bp.route('/tipo_dedicacion/<hashid:id>', methods=['GET']) 
def buscar_por_id(id):
    tipo_dedicacion =TipoDedicacionService.buscar_por_id(id)
    return tipo_dedicacion_mapping.dump(tipo_dedicacion), 200

@tipo_dedicacion_bp.route('/tipo_dedicacion', methods=['GET'])
def obtener_todas():
    tipo_dedicacion = TipoDedicacionService.buscar_todas()  
    resultado = tipo_dedicacion_mapping.dump(tipo_dedicacion, many=True)  
    return jsonify(resultado), 200

@tipo_dedicacion_bp.route('/tipo_dedicacion', methods=['POST'])
def crear():
    tipo_dedicacion = tipo_dedicacion_mapping.load(request.get_json())
    TipoDedicacionService.crear_tipo_dedicacion(tipo_dedicacion)
    return jsonify("tipo_dedicacion creada exitosamente"), 201 

@tipo_dedicacion_bp.route('/tipo_dedicacion/<hashid:id>', methods=['PUT']) 
def actualizar(id):
    tipo_dedicacion = tipo_dedicacion_mapping.load(request.get_json()) 
    TipoDedicacionService.actualizar_tipo_dedicacion, id
    return jsonify("tipo_dedicacion actualizada exitosamente"), 200 

@tipo_dedicacion_bp.route('/tipo_dedicacion/<hashid:id>', methods=['DELETE'])
def borrar_por_id(id):
    tipo_dedicacion = TipoDedicacionService.borrar_tipo_dedicacion(id)
    return jsonify("tipo_dedicacion borrada exitosamente"), 200 

def sanitizar_tipo_dedicacion_entrada(request):
    tipo_dedicacion = tipo_dedicacion_mapping.load(request.get_json())
    tipo_dedicacion.nombre = escape(tipo_dedicacion.nombre)
    tipo_dedicacion.observacion = escape(tipo_dedicacion.observacion)
    return tipo_dedicacion





