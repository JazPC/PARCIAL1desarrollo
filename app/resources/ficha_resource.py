from flask import Blueprint, send_file
from app.services import AlumnoService

certificado_bp=Blueprint('ficha del alumno', __name__)

@certificado_bp.route('/ficha_del_alumno/<int:id>/pdf', methods=['GET'])
def ficha_en_pdf(id: int):
    pdf_io = AlumnoService.generar_ficha(id, 'pdf')
    return send_file(pdf_io, mimetype='application/pdf', as_attachment=False)


