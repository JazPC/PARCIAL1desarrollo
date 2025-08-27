from app.models import Area
from app.repositories import AreaRepository

class AreaService:
    
    @staticmethod
    def crear_area(area: Area) -> Area:
        return AreaRepository.crearArea(area)
    
    @staticmethod
    def buscar_area_por_id(id: int) -> Area | None:
        return AreaRepository.buscar_area_por_id(id)  
    
    @staticmethod
    def listar_area() -> list[Area]:
        return AreaRepository.listar_area()
    
    @staticmethod
    def actualizar_area(id: int, area: Area):
        area_existente = AreaRepository.buscar_area_por_id(id)
        if not area_existente:
            return None
        area_existente.nombre = area.nombre
        area_actualizado = AreaRepository.guardar_area(area_existente)
        return area_actualizado
    
    @staticmethod
    def borrar_por_id(id: int) -> Area | None:
        return AreaRepository.borrar_por_id(id)
    