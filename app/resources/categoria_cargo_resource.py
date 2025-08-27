from flask import jsonify, Blueprint, request
from app.mapping.categoria_cargo_mapping import CategoriaCargoMapping
from app.services.categoria_cargo_service import CategoriaCargoService
from app.validators import validate_with

categoria_cargo_bp = Blueprint('categoria_cargo', __name__)
categoria_cargo_mapping = CategoriaCargoMapping()

@categoria_cargo_bp.route('/categoria_cargo', methods=['GET'])
def buscar_todas():
    categorias = CategoriaCargoService.buscar_todos()
    return categoria_cargo_mapping.dump(categorias, many=True), 200

@categoria_cargo_bp.route('/categoria_cargo/<hashid:id>', methods=['GET'])
def buscar_por_id(id):
    categoria = CategoriaCargoService.buscar_por_id(id)
    return categoria_cargo_mapping.dump(categoria), 200

@categoria_cargo_bp.route('/categoria_cargo', methods=['POST'])
@validate_with(CategoriaCargoMapping)
def crear():
    categoria = categoria_cargo_mapping.load(request.get_json())
    CategoriaCargoService.crear(categoria)
    return jsonify("Categoría creada exitosamente"), 201

@categoria_cargo_bp.route('/categoria_cargo/<hashid:id>', methods=['PUT'])
@validate_with(CategoriaCargoMapping)
def actualizar(id):
    categoria = categoria_cargo_mapping.load(request.get_json())
    actualizado = CategoriaCargoService.actualizar(id, categoria)
    if actualizado is None:
        return jsonify("Categoría no encontrada"), 404
    return jsonify("Categoría actualizada exitosamente"), 200

