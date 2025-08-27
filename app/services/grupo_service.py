from app.models import Grupo
from app.repositories import GrupoRepository

class GrupoService:

    @staticmethod
    def crear_grupo(grupo: Grupo):
        GrupoRepository.crear_grupo(grupo)
        return grupo

    @staticmethod
    def buscar_grupos_todos() -> list[Grupo]:
        return GrupoRepository.buscar_todos()

    @staticmethod
    def buscar_grupo_por_id(id: int):
        grupo = GrupoRepository.buscar_grupo_por_id(id)
        return grupo

    @staticmethod
    def actualizar_grupo(grupo: Grupo, id: int):
        GrupoRepository.actualizar_grupo(grupo, id)
        return grupo

    @staticmethod
    def eliminar_grupo(id: int):
        return GrupoRepository.eliminar_grupo(id)


