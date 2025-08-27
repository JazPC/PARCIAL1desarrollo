from app.models import Facultad
from app.repositories import FacultadRepository
class FacultadService:

  @staticmethod
  def crear_facultad(facultad: Facultad):
    FacultadRepository.crear_facultad(facultad)
    return facultad
  
  @staticmethod
  def listar_facultades():
    facultades= FacultadRepository.listar_facultades()
    return facultades

  def buscar_facultad(id: int):
    facultad = FacultadRepository.buscar_facultad(id)
    return facultad
    
  def actualizar_facultad(facultad: Facultad, id: int):
    FacultadRepository.actualizar_facultad(facultad, id)
    return facultad
  
  def eliminar_facultad(id: int):
    facultad = FacultadRepository.eliminar_facultad(id)
    
    
    