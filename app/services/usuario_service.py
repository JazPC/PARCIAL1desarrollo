from app.models import Usuario
from app.repositories import UsuarioRepository

class UsuarioService:
  @staticmethod
  def guardar_usuario(usuario):
    usuario_guardado = UsuarioRepository.guardar_usuario(usuario)
    return usuario_guardado
  
  @staticmethod
  def listar_usuarios():
    return UsuarioRepository.listar_usuarios()
  
  @staticmethod
  def buscar_usuario(id):
    return UsuarioRepository.buscar_usuario(id)
  
  @staticmethod
  def eliminar_usuario(id):
    return UsuarioRepository.eliminar_usuario(id)
  
  @staticmethod
  def actualizar_usuario(id, usuario):
    return UsuarioRepository.actualizar_usuario(id, usuario)
  
  @staticmethod
  def buscar_usuario_por_nombre(nombre):
    return UsuarioRepository.buscar_usuario_por_nombre(nombre)