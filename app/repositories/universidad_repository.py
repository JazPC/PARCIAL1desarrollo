from app.models import Universidad
from app import db
from sqlalchemy_filters import apply_filters
import logging
from typing import Optional

class UniversidadRepository:

  @staticmethod
  def crear_universidad(universidad: Universidad) -> Universidad:
    db.session.add(universidad)
    db.session.commit()
    return universidad
  
  @staticmethod
  def listar_universidades(page: int, per_page: int, filters: Optional[list] = None) -> list[Universidad]:
    logging.info("page: {}, per_page: {}, filters: {}".format(page, per_page, filters))
    query = db.session.query(Universidad)
    if filters and isinstance(filters, list):
        query = apply_filters(query, filters)
    paginated_query = query.offset((page - 1) * per_page).limit(per_page)
    return paginated_query.all()
  
  @staticmethod
  def buscar_universidad(id: int) -> Universidad:
    return Universidad.query.get(id)
  
  @staticmethod
  def actualizar_universidad(universidad: Universidad, id: int) -> Universidad:
    entity = UniversidadRepository.buscar_universidad(id)
    entity.nombre = universidad.nombre
    entity.sigla = universidad.sigla
    entity.tipo = universidad.tipo
    db.session.commit()
    return entity
  
  @staticmethod
  def eliminar_universidad(id: int) -> None:
    entity = UniversidadRepository.buscar_universidad(id)
    db.session.delete(entity)
    db.session.commit()