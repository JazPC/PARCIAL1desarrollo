from app.models import Departamento
from app.repositories import DepartamentoRepository

class DepartamentoService:
  @staticmethod
  def crear_departamento(departamento: Departamento):
    DepartamentoRepository.crear_departamento(departamento)
    return departamento

  @staticmethod
  def buscar_departamento(id: int):
    departamento = DepartamentoRepository.buscar_departamento(id)
    return departamento
  
  @staticmethod
  def listar_departamentos() -> list[Departamento]:
    return DepartamentoRepository.listar_departamentos()
    
  @staticmethod
  def actualizar_departamento(departamento: Departamento, id: int):
    DepartamentoRepository.actualizar_departamento(departamento, id)
    return departamento
  
  @staticmethod
  def eliminar_departamento(id: int):
    return DepartamentoRepository.eliminar_departamento(id)
    
  