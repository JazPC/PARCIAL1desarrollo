from app.models import Universidad
from app.repositories import UniversidadRepository
from typing import Optional
import logging
class UniversidadService:

  @staticmethod
  def crear_universidad(universidad: Universidad):
    UniversidadRepository.crear_universidad(universidad)
    return universidad

  @staticmethod
  def listar_universidades(page: int = 1, per_page: int = 10, filters: Optional[list] = None):
    logging.info("page: {}, per_page: {}, filters: {}".format(page, per_page, filters))
    universidades = UniversidadRepository.listar_universidades(page, per_page, filters)
    return universidades

  def buscar_universidad(id: int):
    universidad = UniversidadRepository.buscar_universidad(id)
    return universidad
    
  def actualizar_universidad(universidad: Universidad, id: int):
    UniversidadRepository.actualizar_universidad(universidad, id)
    return universidad
  
  def eliminar_universidad(id: int):
    universidad= UniversidadRepository.eliminar_universidad(id)