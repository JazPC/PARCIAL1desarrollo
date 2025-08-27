from app.models import Grupo
from app import db

class GrupoRepository:

    @staticmethod
    def crear_grupo(grupo: Grupo):
        db.session.add(grupo)
        db.session.commit()
        return grupo
    
    @staticmethod
    def buscar_grupo_por_id(id: int) -> Grupo:
        return db.session.query(Grupo).filter(Grupo.id == id).one_or_none()

    @staticmethod
    def buscar_todos() -> list[Grupo]:
        return db.session.query(Grupo).all()

    @staticmethod
    def actualizar_grupo(grupo: Grupo, id: int) ->Grupo:
        entity= GrupoRepository.buscar_grupo_por_id(id)
        entity.nombre = grupo.nombre
        db.session.commit()
        return entity
    
    @staticmethod
    def eliminar_grupo(id: int):
        entity = GrupoRepository.buscar_grupo_por_id(id)
        db.session.delete(entity)
        db.session.commit()
        


