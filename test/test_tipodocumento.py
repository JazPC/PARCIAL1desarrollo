import unittest
from flask import current_app
from app import create_app
from app.models import TipoDocumento
from app import db
from app.services import TipoDocumentoService
import os

class TipodocumentoTestCase(unittest.TestCase):

  def setUp(self):
    os.environ['FLASK_CONTEXT'] = 'testing'
    self.app = create_app()
    self.app_context = self.app.app_context()
    self.app_context.push()
    db.create_all()

  def tearDown(self):
    db.session.remove()
    db.drop_all()
    self.app_context.pop()  

  def test_tipodocumento(self):
    tipodocumento = self.__crear_tipodocumento()
    self.assertEqual(tipodocumento.codigo, "DNI")
    self.assertEqual(tipodocumento.descripcion, "Documento Nacional de Identidad")

  def test_guardar_tipodocumento(self):
    tipodocumento = self.__crear_tipodocumento()
    tipodocumento_guardado = TipoDocumentoService.guardar_tipodocumento(tipodocumento)
    self.assertIsNotNone(tipodocumento_guardado)
    self.assertIsNotNone(tipodocumento.id)
    self.assertEqual(tipodocumento.codigo, "DNI")
    self.assertEqual(tipodocumento.descripcion, "Documento Nacional de Identidad")

  def test_listar_tipodocumentos(self):
    tipodocumento = self.__crear_tipodocumento()
    tipodocumento_guardado = TipoDocumentoService.guardar_tipodocumento(tipodocumento)
    tipodocumentos = TipoDocumentoService.listar_tipodocumentos()
    self.assertIsNotNone(tipodocumentos)
    self.assertEqual(len(tipodocumentos), 1)

  def test_buscar_tipodocumento(self):
    tipodocumento = self.__crear_tipodocumento()
    TipoDocumentoService.guardar_tipodocumento(tipodocumento)
    tipodocumento_encontrado = TipoDocumentoService.buscar_tipodocumento(tipodocumento.id)
    self.assertIsNotNone(tipodocumento_encontrado)
    self.assertEqual(tipodocumento.id, tipodocumento_encontrado.id)
    self.assertEqual(tipodocumento.codigo, tipodocumento_encontrado.codigo)
    self.assertEqual(tipodocumento.descripcion, tipodocumento_encontrado.descripcion)

  

  def __crear_tipodocumento(self):
    tipodocumento = TipoDocumento()
    tipodocumento.codigo = "DNI"
    tipodocumento.descripcion = "Documento Nacional de Identidad"
    return tipodocumento