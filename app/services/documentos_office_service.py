from io import BytesIO
import os
from flask import current_app, render_template, url_for
import jinja2
from python_odt_template import ODTTemplate
from xhtml2pdf import pisa
from python_odt_template.jinja import get_odt_renderer
from docxtpl import DocxTemplate
from abc import ABC, abstractmethod

class Documents(ABC):
   @staticmethod
   @abstractmethod
   def generar(carpeta: str, plantilla: str, context : dict) -> BytesIO:
    pass
   
class PDFDocument(Documents):
  @staticmethod
  def generar(carpeta: str, plantilla: str, context : dict) -> BytesIO:
    
    html_string = render_template(f'{carpeta}/{plantilla}.html', **context)
    pdf_io = BytesIO()
    pisa_status = pisa.CreatePDF(src=html_string, dest=pdf_io)

    if pisa_status.err:
        raise Exception("Error al generar PDF")

    pdf_io.seek(0)
    return pdf_io
  

class ODTDocument(Documents):
  @staticmethod
  def generar(carpeta: str, plantilla: str, context : dict) -> BytesIO:
    odt_renderer = get_odt_renderer(media_path=url_for('static', filename='media'))
    path_template = os.path.join(current_app.root_path, 'carpeta',f'{plantilla}.odt')
    
    
    odt_io = BytesIO()
    import tempfile
    with tempfile.NamedTemporaryFile(suffix='.odt', delete=False) as temp_file:
        temp_path = temp_file.name

    with ODTTemplate(path_template) as template:
        odt_renderer.render( template,
            context=context
        )
        template.pack(temp_path)
        with open(temp_path, 'rb') as f:
            odt_io.write(f.read())
        
    os.unlink(temp_path)
    odt_io.seek(0)
    return odt_io
  
class DOCXDocument(Documents):
  @staticmethod
  def generar(carpeta: str, plantilla: str, context : dict) -> BytesIO:
    path_template = os.path.join(current_app.root_path, f'{carpeta}', f'{plantilla}.docx')
    doc = DocxTemplate(path_template)
    
    docx_io = BytesIO()
    import tempfile
    with tempfile.NamedTemporaryFile(suffix='.odt', delete=False) as temp_file:
        temp_path = temp_file.name

    jinja_env = jinja2.Environment()
    doc.render(context, jinja_env)
    doc.save(temp_path)
    with open(temp_path, 'rb') as f:
            docx_io.write(f.read())
        
    os.unlink(temp_path)
    docx_io.seek(0)
    return docx_io
  

def obtener_tipo_documento(tipo: str) -> Documents:
  tipos ={
      "pdf": PDFDocument,
      "odt": ODTDocument,
      "docx": DOCXDocument
  } 
  return tipos.get(tipo)