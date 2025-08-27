from app import db
from app.models import Cargo

class CargoRepository:
  @staticmethod
  def crear(cargo: Cargo) -> Cargo:
    db.session.add(cargo)
    db.session.commit()
    return cargo

  @staticmethod
  def buscar_por_id(id: int) -> Cargo | None:
    return db.session.query(Cargo).filter_by(id=id).one_or_none()
    
  @staticmethod
  def buscar_todos() -> list[Cargo]:
    return db.session.query(Cargo).all()
    
  @staticmethod
  def guardar(cargo: Cargo) -> Cargo:
    db.session.commit()
    return cargo