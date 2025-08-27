from app import db
from app.models import Autoridad


#a parte del CRUD tiene consultas a la base de datos

class AutoridadRepository:
    @staticmethod
    def crear_autoridad(autoridad):
        db.session.add(autoridad)
        db.session.commit()
        return autoridad

    @staticmethod
    def buscar_por_id(id: int) -> Autoridad:
        return db.session.query(Autoridad).filter(Autoridad.id == id).one_or_none()
    
    @staticmethod
    def buscar_todas():
        return Autoridad.query.all()
    
    @staticmethod
    def guardar_autoridad(id: int,autoridad: Autoridad) -> Autoridad:
        db.session.commit()
        return autoridad
    
    @staticmethod
    def borrar_autoridad(id: int) -> None:
        entity = AutoridadRepository.buscar_por_id(id)
        db.session.delete(entity)
        db.session.commit()