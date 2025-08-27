from app import db
from app.models import TipoDedicacion

class TipoDedicacionRepository:
    @staticmethod
    def crear_tipo_dedicacion(tipo_dedicacion: TipoDedicacion):
        db.session.add(tipo_dedicacion)
        db.session.commit()
        return tipo_dedicacion

    @staticmethod
    def buscar_por_id(id: int) -> TipoDedicacion:
        return db.session.query(TipoDedicacion).filter(TipoDedicacion.id == id).one_or_none()
    
    @staticmethod
    def buscar_todas():
        return TipoDedicacion.query.all()
    
    @staticmethod
    def actualizar_tipo_dedicacion(id: int,tipo_dedicacion: TipoDedicacion) -> TipoDedicacion:
        entity = TipoDedicacionRepository.buscar_por_id(id)
        if entity is None:
            return None 
        entity.nombre = tipo_dedicacion.nombre
        entity.observacion = tipo_dedicacion.observacion
        db.session.commit()
        return entity
    
    @staticmethod
    def borrar_tipo_dedicacion(id: int) -> None:
        entity = TipoDedicacionRepository.buscar_por_id(id)
        db.session.delete(entity)
        db.session.commit()