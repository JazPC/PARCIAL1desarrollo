from app.models import TipoDocumento
from app.repositories import TipoDocumentoRepository

class TipoDocumentoService:
  @staticmethod
  def listar_tipodocumentos():
    return TipoDocumentoRepository.listar_tipodocumentos()
  
  def guardar_tipodocumento(tipodocumento:TipoDocumento)->TipoDocumento:
    return TipoDocumentoRepository.guardar(tipodocumento)
  
  @staticmethod
  def buscar_tipodocumento(id:int):
    return TipoDocumentoRepository.buscar_tipodocumento(id)
  