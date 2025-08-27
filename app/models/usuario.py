from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Usuario(db.Model):
  __tablename__ = 'usuarios'
  id : int = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nombredeusuario: str = db.Column(db.String(100), unique=True, nullable=False)
  password: str = db.Column(db.String(255), nullable=False)

  alumno = db.relationship('Alumno', back_populates='usuario', uselist=False)
  actividad: bool =  db.Column(db.Boolean, nullable=False)
