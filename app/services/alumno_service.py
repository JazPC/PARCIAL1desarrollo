from flask import render_template
from app.models import Alumno
from app.repositories import AlumnoRepository
from datetime import datetime
import datetime
from io import BytesIO
from app.services.documentos_office_service import obtener_tipo_documento
import base64

def imagen_a_base64(ruta: str) -> str:
    with open(ruta, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return f"data:image/png;base64,{encoded_string}"
class AlumnoService:

  @staticmethod
  def crear_alumno(alumno: Alumno):
    AlumnoRepository.crear_alumno(alumno)
    return alumno
  def buscar_alumno(id: int):
    alumno = AlumnoRepository.buscar_alumno(id)
    return alumno
  def actualizar_alumno(alumno: Alumno, id: int):
    AlumnoRepository.actualizar_alumno(alumno, id)
    return alumno
  def eliminar_alumno(id: int):
    alumno = AlumnoRepository.eliminar_alumno(id)

  @staticmethod
  def generar_certificado_alumno_regular(id: int, tipo: str) -> BytesIO:
      alumno = AlumnoRepository.buscar_alumno(id)
      if not alumno:
          return None
      context=AlumnoService.__obtener_alumno(alumno)

      documento = obtener_tipo_documento(tipo)

      if not documento:
         return None
      return documento.generar(
         carpeta='certificados',
         plantilla=f'certificado_{tipo}',
         context=context
      )
     
  @staticmethod
  def __obtener_fecha_actual():
    fecha_actual = datetime.datetime.now()
    fecha_str = fecha_actual.strftime('%d de %B de %Y')
    return fecha_str
  @staticmethod
  def __obtener_alumno(alumno: Alumno) -> dict:
     especialidad = alumno.especialidad
     facultad = especialidad.facultad
     universidad = facultad.universidad
     fecha = AlumnoService.__obtener_fecha_actual()
     logo_ministerio = imagen_a_base64('app/static/img/logo-ministerio.png')
     logo_utn = imagen_a_base64('app/static/img/logo-utn.png')
     return {
        "alumno":alumno,
        "especialidad": especialidad,
        "facultad": facultad,
        "universidad": universidad,
        "fecha": fecha,
        "logo_ministerio": logo_ministerio,
        "logo_utn": logo_utn
     }
