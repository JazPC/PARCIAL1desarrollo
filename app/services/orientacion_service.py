from app.models import Orientacion
from app.repositories.orientacion_repositorio import OrientacionRepository

class OrientacionService:
  @staticmethod
  def crear_orientacion(orientacion: Orientacion):
    OrientacionRepository.crear_orientacion(orientacion)
    return orientacion

  @staticmethod
  def buscar_orientacion(id: int):
    orientacion = OrientacionRepository.buscar_orientacion(id)
    return orientacion
  
  @staticmethod
  def listar_orientaciones() -> list[Orientacion]:
    return OrientacionRepository.listar_orientaciones()

  @staticmethod
  def actualizar_orientacion(orientacion: Orientacion, id: int):
    OrientacionRepository.actualizar_orientacion(orientacion, id)
    return orientacion
  
  @staticmethod
  def eliminar_orientacion(id: int):
    return OrientacionRepository.eliminar_orientacion(id)
    
  