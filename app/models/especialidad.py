from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq=True)
class Especialidad(db.Model):
    __tablename__ = 'especialidades'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    letra = db.Column(db.String(100), nullable=False)
    observacion = db.Column(db.String(100), nullable=False)
    alumnos = db.relationship('Alumno', back_populates = 'especialidad')
    facultad_id = db.Column(db.Integer, db.ForeignKey('facultades.id'))
    facultad = db.relationship('Facultad', back_populates = 'especialidades')


  

