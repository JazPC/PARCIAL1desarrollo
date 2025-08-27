from flask import jsonify, Blueprint, request
from app.mapping.departamento_mapping import DepartamentoMapping
from app.services.departamento_service import DepartamentoService
from markupsafe import escape

from app.validators import validate_with

departamento_bp = Blueprint('departamento', __name__)

departamento_mapping = DepartamentoMapping()

@departamento_bp.route('/departamento/<hashid:id>', methods=['GET'])
def buscar_por_id(id):
    departamento = DepartamentoService.buscar_departamento(id)
    return departamento_mapping.dump(departamento), 200 

@departamento_bp.route('/departamento', methods=['GET'])
def listar_departamentos(): 
    departamentos = DepartamentoService.listar_departamentos()
    return departamento_mapping.dump(departamentos, many=True), 200

@departamento_bp.route('/departamento', methods=['POST'])
@validate_with(DepartamentoMapping)
def crear():
    departamento = departamento_mapping.load(request.get_json())
    DepartamentoService.crear_departamento(departamento)
    return jsonify("Departamento creado exitosamente"), 201 

@departamento_bp.route('/departamento/<hashid:id>', methods=['PUT'])
@validate_with(DepartamentoMapping)
def actualizar(id): 
    departamento = departamento_mapping.load(request.get_json())
    DepartamentoService.actualizar_departamento(departamento, id)
    return jsonify("Departamento actualizado exitosamente"), 200        

@departamento_bp.route('/departamento/<hashid:id>', methods=['DELETE'])
def borrar_por_id(id):
    DepartamentoService.eliminar_departamento(id)
    return jsonify("Departamento borrado exitosamente"), 200

def sanitizar_departamento_entrada(request):
    departamento = departamento_mapping.load(request.get_json())
    departamento.nombre = escape(departamento.nombre)
    return departamento