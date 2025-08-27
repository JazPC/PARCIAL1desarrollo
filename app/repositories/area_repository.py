from app import db
from app.models import Area

class AreaRepository:
  @staticmethod
  def crearArea(area: Area) -> Area:
    db.session.add(area)
    db.session.commit()
    return area

  @staticmethod
  def buscar_area_por_id(id: int) -> Area | None:
    return db.session.query(Area).filter_by(id=id).one_or_none()
    
  @staticmethod
  def listar_area() -> list[Area]:
    return db.session.query(Area).all()
    
  @staticmethod
  def guardar_area(area: Area) -> Area:
    area_existente = db.session.merge(area)
    db.session.commit()
    return area_existente
  
  @staticmethod
  def borrar_por_id(id: int):
    area = db.session.query(Area).filter_by(id=id).first()
    if not area:
      return None
    db.session.delete(area)
    db.session.commit()
    return area
