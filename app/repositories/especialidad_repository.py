from app.models import Especialidad
from app import db

class EspecialidadRepository:
    @staticmethod
    def crear_especialidad(especialidad: Especialidad):
        db.session.add(especialidad)
        db.session.commit()
        return especialidad 

    @staticmethod
    def buscar_especialidad(id: int) -> Especialidad:
        return db.session.query(Especialidad).filter(Especialidad.id == id).one_or_none()

    @staticmethod
    def actualizar_especialidad(id: int, especialidad: Especialidad) -> Especialidad:
        entity = EspecialidadRepository.buscar_especialidad(id)
        if not entity:
            return None  
        entity.nombre = especialidad.nombre
        entity.letra = especialidad.letra
        entity.observacion = especialidad.observacion
        db.session.commit()
        return entity

    @staticmethod
    def eliminar_especialidad(id: int) -> None:
        entity = EspecialidadRepository.buscar_especialidad(id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
