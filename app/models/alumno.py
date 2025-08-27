from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Alumno(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    nroDocumento = db.Column(db.String(20), nullable=False, unique=True)
    tipoDocumento = db.Column(db.String(20), nullable=False)
    fechaNacimiento = db.Column(db.String(20), nullable=False) #aque deberia ser db.Date
    sexo = db.Column(db.String(10), nullable=False)
    nroLegajo = db.Column(db.Integer, nullable=False, unique=True)
    fechaIngreso = db.Column(db.String(20), nullable=False)
    carrera = db.Column(db.String(100), nullable=False)
    
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), unique = True, nullable = False)
    usuario = db.relationship('Usuario', back_populates='alumno')

    #relacion de alumno con notas
    notas = db.relationship("Nota")

    #relacion de alumno con universidad
    universidad_id = db.Column(db.Integer, db.ForeignKey('universidades.id'))
    universidad = db.relationship('Universidad', back_populates='alumnos')

    #relacion de alumno con especialidad
    especialidad_id : int =db.Column(db.Integer, db.ForeignKey('especialidades.id'), nullable = False)
    especialidad = db.relationship('Especialidad', back_populates = 'alumnos')


    #TODO: relacionar con tipo de documento
    #TODO: aplicar ley de demeter
