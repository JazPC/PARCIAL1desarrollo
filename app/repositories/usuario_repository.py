from app.models import Usuario
from app import db 

class UsuarioRepository():
  @staticmethod
  def guardar_usuario(usuario: Usuario):
    db.session.add(usuario)
    db.session.commit()
    return usuario
  
  @staticmethod
  def listar_usuarios():
    return Usuario.query.all()
  
  @staticmethod
  def buscar_usuario(id):
    return Usuario.query.filter_by(id=id).first()
  
  @staticmethod
  def eliminar_usuario(id):
    usuario = Usuario.query.filter_by(id=id).first()
    if not usuario:
      return None
    db.session.delete(usuario)
    db.session.commit()
    return usuario
  

  @staticmethod
  def actualizar_usuario(id, usuario):
    usuario = Usuario.query.filter_by(id=id).first()
    if not usuario:
      return None
    usuario.nombredeusuario = usuario.nombredeusuario
    usuario.password = usuario.password
    usuario.actividad = usuario.actividad
    db.session.commit()
    return usuario
  
  @staticmethod
  def buscar_usuario_por_nombre(nombre):
    return Usuario.query.filter_by(nombredeusuario=nombre).first()
  
