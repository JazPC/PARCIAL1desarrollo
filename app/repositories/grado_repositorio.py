from app.models import Grado
from app import db

class GradoRepository:

  @staticmethod
  def crear_grado(grado: Grado):
    db.session.add(grado)
    db.session.commit()
    return grado
  
  @staticmethod
  def buscar_grado(id: int) -> Grado:
    return db.session.query(Grado).filter(Grado.id == id).one_or_none()
  
  @staticmethod
  def listar_grados() -> list[Grado]:
    return db.session.query(Grado).all()

  @staticmethod
  def actualizar_grado(grado: Grado, id: int) -> Grado:
    entity = GradoRepository.buscar_grado(id)
    entity.nombre = grado.nombre
    db.session.commit()
    return entity
  
  @staticmethod
  def eliminar_grado(id: int) -> None:
    entity = GradoRepository.buscar_grado(id)
    db.session.delete(entity)
    db.session.commit()