from app.models import Grado
from app.repositories.grado_repositorio import GradoRepository

class GradoService:
  @staticmethod
  def crear_grado(grado: Grado):
    GradoRepository.crear_grado(grado)
    return grado

  @staticmethod
  def buscar_grado(id: int):
    grado = GradoRepository.buscar_grado(id)
    return grado

  @staticmethod
  def listar_grados() -> list[Grado]:
    return GradoRepository.listar_grados()

  @staticmethod
  def actualizar_grado(grado: Grado, id: int):
    GradoRepository.actualizar_grado(grado, id)
    return grado
  
  @staticmethod
  def eliminar_grado(id: int):
    return GradoRepository.eliminar_grado(id)
    
    
    