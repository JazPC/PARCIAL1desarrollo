from app.models import Departamento
from app import db

class DepartamentoRepository:

  @staticmethod
  def crear_departamento(departamento: Departamento):
    db.session.add(departamento)
    db.session.commit()
    return departamento
  
  @staticmethod
  def buscar_departamento(id: int) -> Departamento:
    return db.session.query(Departamento).filter(Departamento.id == id).one_or_none()
  
  @staticmethod
  def listar_departamentos() -> list[Departamento]:
    return db.session.query(Departamento).all()

  @staticmethod
  def actualizar_departamento(departamento: Departamento, id: int) -> Departamento:
    entity = DepartamentoRepository.buscar_departamento(id)
    entity.nombre = departamento.nombre
    db.session.commit()
    return entity
  
  @staticmethod
  def eliminar_departamento(id: int) -> None:
    entity = DepartamentoRepository.buscar_departamento(id)
    db.session.delete(entity)
    db.session.commit()