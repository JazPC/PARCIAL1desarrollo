import unittest
from flask import current_app
from app import create_app
from app.models import Departamento
from app.services import DepartamentoService
from app import db
import os

class CartTestCase(unittest.TestCase):

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

    def test_app(self):
        self.assertIsNotNone(current_app)
  
    def test_departamento(self):
        departamento = Departamento()
        departamento.nombre = 'Ingenieria'
          
        self.assertEqual(departamento.nombre, 'Ingenieria')

    def test_crear_departamento(self):
        departamento = self.__crear_departamento()
        departamento_guardado = DepartamentoService.crear_departamento(departamento)
        self.assertIsNotNone(departamento_guardado)
        self.assertIsNotNone(departamento_guardado.id)
        self.assertGreaterEqual(departamento_guardado.id, 1)
        self.assertEqual(departamento_guardado.nombre, departamento.nombre)
        
    def test_buscar_departamento(self):
        departamento = self.__crear_departamento()
        DepartamentoService.crear_departamento(departamento)
        departamento_encontrado = DepartamentoService.buscar_departamento(departamento.id)
        self.assertIsNotNone(departamento_encontrado)
        self.assertEqual(departamento_encontrado.nombre, departamento.nombre)
        
    def test_actualizar_departamento(self):
        departamento = self.__crear_departamento()
        DepartamentoService.crear_departamento(departamento)
        nuevos_datos_departamento = Departamento()
        nuevos_datos_departamento.nombre = "Ingenieria Actualizada"
        departamento_modificado = DepartamentoService.actualizar_departamento(nuevos_datos_departamento, departamento.id)
        departamento_encontrado = DepartamentoService.buscar_departamento(departamento.id)
        self.assertIsNotNone(departamento_encontrado)
        self.assertIsNotNone(departamento_encontrado.id)
        self.assertGreaterEqual(departamento_encontrado.id, 1)
        self.assertEqual(departamento_encontrado.nombre, departamento_modificado.nombre)
        
    def test_eliminar_departamento(self):
        departamento = self.__crear_departamento()
        DepartamentoService.crear_departamento(departamento)
        DepartamentoService.eliminar_departamento(departamento.id)
        departamento_encontrado = DepartamentoService.buscar_departamento(departamento.id)
        self.assertIsNone(departamento_encontrado)    
    
    

    def __crear_departamento(self):
        departamento = Departamento()
        departamento.nombre = "Ingenieria"
        return departamento

if __name__ == '__main__':
    unittest.main()