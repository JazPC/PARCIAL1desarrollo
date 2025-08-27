from app.models import Especialidad
from app.repositories import EspecialidadRepository

class EspecialidadService:

    @staticmethod
    def crear_especialidad(especialidad: Especialidad):
        EspecialidadRepository.crear_especialidad(especialidad)
        return especialidad

    @staticmethod
    def buscar_especialidad(id: int):
        especialidad = EspecialidadRepository.buscar_especialidad(id)
        return especialidad

    @staticmethod
    def actualizar_especialidad(id: int, especialidad: Especialidad):
        EspecialidadRepository.actualizar_especialidad(id, especialidad)
        return especialidad

    @staticmethod
    def eliminar_especialidad(id: int):
        EspecialidadRepository.eliminar_especialidad(id)
