from flask import jsonify, Blueprint, request
from app.mapping.grupo_mapping import GrupoMapping
from app.services.grupo_service import GrupoService 
from markupsafe import escape
from app.validators import validate_with

grupo_bp = Blueprint('grupo', __name__)
grupo_mapping = GrupoMapping()  

@grupo_bp.route('/grupo', methods=['GET'])
def buscar_todos():
    grupos = GrupoService.buscar_grupos_todos()
    return grupo_mapping.dump(grupos, many=True), 200

@grupo_bp.route('/grupo/<hashid:id>', methods=['GET'])
def buscar_por_id(id):
    grupo = GrupoService.buscar_grupo_por_id(id)
    return grupo_mapping.dump(grupo), 200

@grupo_bp.route('/grupo', methods=['POST'])
@validate_with(GrupoMapping)
def crear():    
    grupo = grupo_mapping.load(request.get_json())
    GrupoService.crear_grupo(grupo)
    return jsonify("Grupo creado exitosamente"), 201

@grupo_bp.route('/grupo/<hashid:id>', methods=['PUT'])
@validate_with(GrupoMapping)
def actualizar(id):
    grupo = grupo_mapping.load(request.get_json())
    GrupoService.actualizar_grupo(grupo, id)
    return jsonify("Grupo actualizado exitosamente"), 200   

@grupo_bp.route('/grupo/<hashid:id>', methods=['DELETE'])
def borrar_por_id(id):
    GrupoService.eliminar_grupo(id)
    return jsonify("Grupo borrado exitosamente"), 200

def sanitizar_grupo_entrada(request):
    grupo = grupo_mapping.load(request.get_json())
    grupo.nombre = escape(grupo.nombre)
    return grupo