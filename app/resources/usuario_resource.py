from flask import Blueprint, request, jsonify
from app.mapping import UsuarioMapping
from app.services import UsuarioService



usuario_mapping = UsuarioMapping()
usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/usuario', methods=['GET'])
def listar():
  return usuario_mapping.dump(UsuarioService.listar_usuarios(), many=True), 200

@usuario_bp.route('/usuario/<int:id>', methods=['GET'])
def buscar(id):
  usuario = UsuarioService.buscar_usuario(id)
  return usuario_mapping.dump(usuario), 200

@usuario_bp.route('/usuario', methods=['POST'])
def crear():
  usuario = usuario_mapping.load(request.get_json())
  UsuarioService.guardar_usuario(usuario)
  return jsonify("Usuario creado exitosamente"), 201  

@usuario_bp.route('/usuario/<int:id>', methods=['PUT'])
def actualizar(id):
  usuario = usuario_mapping.load(request.get_json())
  UsuarioService.actualizar_usuario(id, usuario)
  return jsonify("Usuario actualizado exitosamente"), 200

@usuario_bp.route('/usuario/<int:id>', methods=['DELETE'])
def borrar(id):
  UsuarioService.eliminar_usuario(id)
  return jsonify("Usuario borrado exitosamente"), 200

@usuario_bp.route('/usuario/<string:nombre>', methods=['GET'])
def buscar_por_nombre(nombre):
  usuario = UsuarioService.buscar_usuario_por_nombre(nombre)
  return usuario_mapping.dump(usuario), 200


