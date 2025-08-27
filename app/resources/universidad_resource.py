from flask import jsonify, Blueprint, request 
from app.mapping import UniversidadMapping
from app.services.universidad_service import UniversidadService
from markupsafe import escape
import json
import logging
from app.validators import validate_with


universidad_bp = Blueprint('universidad', __name__)

universidad_mapping = UniversidadMapping()
#from app.validators import validate_with


@universidad_bp.route('/universidad/<hashid:id>', methods=['GET'])
def buscar_por_id(id):
    universidad = UniversidadService.buscar_universidad(id)
    return universidad_mapping.dump(universidad), 200

@universidad_bp.route('/universidad', methods=['GET'])
def listar_universidades():
    page: int = request.headers.get('X-page', 1, type=int)
    per_page: int = request.headers.get('X-per-page', 10, type=int) 
    filters_str : str|None = request.headers.get('X-filters', None, type=str) 
    logging.info("page: {}, per_page: {}, filters: {}".format(page, per_page, filters_str))
    if filters_str:
        filters = json.loads(filters_str)
        universidades = UniversidadService.listar_universidades(page=page, per_page=per_page, filters=filters)
    else:
        universidades = UniversidadService.listar_universidades(page=page, per_page=per_page)
    return universidad_mapping.dump(universidades, many=True), 200

@universidad_bp.route('/universidad', methods=['POST']) 
@validate_with(UniversidadMapping)
def crear(universidad):
    UniversidadService.crear_universidad(universidad)
    return jsonify("Universidad creada exitosamente"), 201 

@universidad_bp.route('/universidad/<hashid:id>', methods=['PUT'])
@validate_with(UniversidadMapping) #validar acciones con marshmallow, validate_with en carpeta validators
def actualizar(universidad, id):
    UniversidadService.actualizar_universidad(universidad, id)
    return jsonify("Universidad actualizada exitosamente"), 200 

@universidad_bp.route('/universidad/<hashid:id>', methods=['DELETE'])
def borrar_por_id(id):
    universidad = UniversidadService.eliminar_universidad(id)
    return jsonify("Universidad borrada exitosamente"), 200 


def sanitizar_universidad_entrada(request):
  universidad = universidad_mapping.load(request.get_json())
  universidad.nombre = escape(universidad.nombre)
  universidad.sigla = escape(universidad.sigla)
  universidad.tipo = escape(universidad.tipo) 
  return universidad






#crea un objeto json que se le va a devolver al usuario
#para ejecutar para probarlo desde el postman por ej, hay que crear las tablas y un migrate
#abrio el pgadmin para ver las tablas
#en consola:
#flask db migrate 
#hay que modificar las variables de flask context para que la base sea PROD
#flask db init
#migraciones en env.py:
#from app .models import *
#flask db upgrade
#flask app.py
