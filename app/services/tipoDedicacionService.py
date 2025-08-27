from app.models import TipoDedicacion
from app.repositories import TipoDedicacionRepository

class TipoDedicacionService:
    
    @staticmethod
    def crear_tipo_dedicacion(tipo_dedicacion: TipoDedicacion):
        """Crea un nuevo tipo de dedicación en la base de datos."""
        TipoDedicacionRepository.crear_tipo_dedicacion(tipo_dedicacion)
        return tipo_dedicacion
    
    @staticmethod
    def buscar_por_id(id: int):
        return TipoDedicacionRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todas():
        return TipoDedicacionRepository.buscar_todas()
    
    @staticmethod
    def actualizar_tipo_dedicacion(id: int, tipo_dedicacion: TipoDedicacion):
        return TipoDedicacionRepository.actualizar_tipo_dedicacion(id, tipo_dedicacion)
    
    @staticmethod
    def borrar_tipo_dedicacion(id: int):
        return TipoDedicacionRepository.borrar_tipo_dedicacion(id)
