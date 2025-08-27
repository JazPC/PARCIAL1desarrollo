from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq=True)
class Nota(db.Model):
  __tablename__ = 'notas' 
  id : int  = db.Column(db.Integer, primary_key=True, autoincrement=True)
  alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'))
  autoridad_id: int = db.Column(db.Integer)
  nota: float = db.Column(db.Float)

  materia_id = db.Column(db.Integer, db.ForeignKey('materias.id'))
  materia = db.relationship("Materia", back_populates="notas")

  #Relacion de nota con autoridad
  
  autoridad_id = db.Column(db.Integer, db.ForeignKey('autoridades.id'))
  autoridad = db.relationship("Autoridad", back_populates="notas")