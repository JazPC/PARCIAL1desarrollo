from app.models import TipoDocumento
from app import db

class TipoDocumentoRepository:
  
  @staticmethod
  def listar_tipodocumentos():
    return db.session.query(TipoDocumento).all()
  
  @staticmethod
  def guardar(tipodocumento:TipoDocumento)->TipoDocumento:
    db.session.add(tipodocumento)
    db.session.commit()
    return tipodocumento
  
  @staticmethod
  def buscar_tipodocumento(id:int):
    return db.session.query(TipoDocumento).filter(TipoDocumento.id == id).one_or_none()
  
