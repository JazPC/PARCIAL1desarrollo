from flask import jsonify, Blueprint, request 
from app.mapping.cargo_mapping import CargoMapping
from app.services.cargo_service import CargoService
from app.validators import validate_with

cargo_bp = Blueprint('cargo', __name__)
cargo_mapping = CargoMapping()

@cargo_bp.route('/cargo', methods=['GET'])
def buscar_todos():
    cargos = CargoService.buscar_todos()
    return cargo_mapping.dump(cargos, many=True), 200 

@cargo_bp.route('/cargo/<hashid:id>', methods=['GET']) 
def buscar_por_id(id):
    cargo = CargoService.buscar_por_id(id)
    return cargo_mapping.dump(cargo), 200

@cargo_bp.route('/cargo', methods=['POST']) 
@validate_with(CargoMapping)
def crear():
    cargo = cargo_mapping.load(request.get_json())
    CargoService.crear(cargo)
    return jsonify("Cargo creado exitosamente"), 201 

@cargo_bp.route('/cargo/<hashid:id>', methods=['PUT'])  
@validate_with(CargoMapping)
def actualizar(id):
    cargo = cargo_mapping.load(request.get_json())
    actualizado = CargoService.actualizar(id, cargo)
    if actualizado is None:
        return jsonify("Cargo no encontrado"), 404
    return jsonify("Cargo actualizado exitosamente"), 200