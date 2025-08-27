from app.models import TipoEspecialidad
from app.repositories import TipoEspecialidadRepository

class TipoespecialidadService:

    @staticmethod
    def crear_tipoespecialidad(tipoespecialidad: TipoEspecialidad):
        TipoEspecialidadRepository.crear_tipoespecialidad(tipoespecialidad)
        return tipoespecialidad
    
    def buscar_tipoespecialidad(id: int):
        tipoespecialidad = TipoEspecialidadRepository.buscar_tipoespecialidad(id)
        return tipoespecialidad
    
    def actualizar_tipoespecialidad(tipoespecialidad: TipoEspecialidad, id: int):
        TipoEspecialidadRepository.actualizar_tipoespecialidad(tipoespecialidad, id)
        return tipoespecialidad
    
    def eliminar_tipoespecialidad(id: int):
        tipoespecialidad = TipoEspecialidadRepository.eliminar_tipoespecialidad(id)
    

        