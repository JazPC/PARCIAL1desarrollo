from app.models import Alumno
from app import db


class AlumnoRepository:

  @staticmethod
  def crear_alumno(alumno: Alumno) -> Alumno:
    db.session.add(alumno)
    db.session.commit()
    return alumno
  
  @staticmethod
  def buscar_alumno(id: int) -> Alumno:
    return db.session.query(Alumno).filter(Alumno.id == id).one_or_none()
  
  @staticmethod
  def actualizar_alumno(alumno: Alumno , id: int) -> Alumno:
    entity = AlumnoRepository.buscar_alumno(id)
    entity.nombre = alumno.nombre
    entity.apellido = alumno.apellido
    entity.nroDocumento= alumno.nroDocumento
    entity.fechaNacimiento = alumno.fechaNacimiento
    entity.tipoDocumento = alumno.tipoDocumento
    entity.sexo = alumno.sexo
    entity.nroLegajo = alumno.nroLegajo
    entity.fechaIngreso = alumno.fechaIngreso
    entity.carrera = alumno.carrera
  

    db.session.commit()
    return entity
  
  @staticmethod
  def eliminar_alumno(id: int) -> None:
    entity = AlumnoRepository.buscar_alumno(id)
    db.session.delete(entity)
    db.session.commit()