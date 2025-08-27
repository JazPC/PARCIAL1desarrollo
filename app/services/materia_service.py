from app.models import Materia
from app.repositories import MateriaRepository

class MateriaService:
    
    @staticmethod
    def crear_materia(materia: Materia):
        "crea una nueva materia en la base de datos."
        MateriaRepository.crear_materia(materia)
        return materia
    
    @staticmethod
    def buscar_por_id(id: int):
        return MateriaRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todas():
        return MateriaRepository.buscar_todas()
    
    @staticmethod
    def actualizar_materia( id: int,materia: Materia):
        return MateriaRepository.actualizar_materia(id,materia)
    
    @staticmethod
    def borrar_materia(id: int):
        return MateriaRepository.borrar_materia(id)