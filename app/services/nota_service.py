from app.models import Nota
from app.repositories import NotaRepository

class NotaService:
  @staticmethod
  def guardar_nota(nota: Nota):
    return NotaRepository.guardar_nota(nota)
  
  @staticmethod
  def buscar_nota(alumno_id: int):
    return NotaRepository.buscar_nota(alumno_id)
  