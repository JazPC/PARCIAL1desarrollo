from app.models import Nota
from app import db

class NotaRepository:

  @staticmethod
  def guardar_nota(nota):
    db.session.add(nota)
    db.session.commit()
    return nota
  
  @staticmethod
  def buscar_nota(alumno_id):
    return db.session.query(Nota).filter(Nota.alumno_id == alumno_id).first()