from app.models import TipoEspecialidad
from app import db


class TipoEspecialidadRepository:

  @staticmethod
  def crear_tipoespecialidad(tipoespecialidad: TipoEspecialidad):
    db.session.add(tipoespecialidad)
    db.session.commit()
    return tipoespecialidad
  
  @staticmethod
  def buscar_tipoespecialidad(id: int) -> TipoEspecialidad:
    return db.session.query(TipoEspecialidad).filter(TipoEspecialidad.id == id).one_or_none()
  
  @staticmethod
  def actualizar_tipoespecialidad(tipoespecialidad: TipoEspecialidad, id: int) -> TipoEspecialidad:
    entity = TipoEspecialidadRepository.buscar_tipoespecialidad(id)
    entity.nombre = tipoespecialidad.nombre
    entity.nivel = tipoespecialidad.nivel
    db.session.commit()
    return entity
  
  @staticmethod
  def eliminar_tipoespecialidad(id: int) -> None:
    entity = TipoEspecialidadRepository.buscar_tipoespecialidad(id)
    db.session.delete(entity)
    db.session.commit()
  
  