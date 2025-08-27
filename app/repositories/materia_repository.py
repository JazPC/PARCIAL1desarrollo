from app import db
from app.models import Materia

class MateriaRepository:
    @staticmethod
    def crear_materia(materia):
        db.session.add(materia)
        db.session.commit()
        return materia

    @staticmethod
    def buscar_por_id(id: int) -> Materia:
        return db.session.query(Materia).filter(Materia.id == id).one_or_none()
    
    @staticmethod
    def buscar_todas():
        return Materia.query.all()
    
    @staticmethod
    def actualizar_materia(id: int,materia: Materia) -> Materia:
        entity = MateriaRepository.buscar_por_id(id)
        if entity is None:
            return None 
        entity.nombre = materia.nombre
        entity.diseno_curricular = materia.diseno_curricular
        entity.horas_dictadas = materia.horas_dictadas
        entity.promocional = materia.promocional
        entity.nivel = materia.nivel
        db.session.commit()
        return entity
    
    @staticmethod
    def borrar_materia(id: int) -> None:
        entity = MateriaRepository.buscar_por_id(id)
        db.session.delete(entity)
        db.session.commit()