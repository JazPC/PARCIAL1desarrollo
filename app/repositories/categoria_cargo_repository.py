from app import db
from app.models import CategoriaCargo

class CategoriaCargoRepository:
    
  @staticmethod
  def crear(categoria_cargo: CategoriaCargo) -> CategoriaCargo:
    db.session.add(categoria_cargo)
    db.session.commit()
    return categoria_cargo
  
  @staticmethod
  def buscar_por_id(id: int) -> CategoriaCargo | None:
    return db.session.query(CategoriaCargo).filter_by(id=id).one_or_none()
    
  @staticmethod
  def buscar_todos() -> list[CategoriaCargo]:
    return db.session.query(CategoriaCargo).all()
  
  @staticmethod
  def guardar(categoria_cargo: CategoriaCargo) -> CategoriaCargo:
    db.session.commit()
    return categoria_cargo