import unittest
from flask import current_app
from app import create_app
from app.models import Grado
from app.services import GradoService
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
  
    def test_grado(self):
        grado = Grado()
        grado.nombre = 'Ingenieria en Sistemas'
          
        self.assertEqual(grado.nombre, 'Ingenieria en Sistemas')

    def test_crear_grado(self):
        grado = self.__crear_grado()
        grado_guardado = GradoService.crear_grado(grado)
        self.assertIsNotNone(grado_guardado)
        self.assertIsNotNone(grado_guardado.id)
        self.assertGreaterEqual(grado_guardado.id, 1)
        self.assertEqual(grado_guardado.nombre, grado.nombre)
        
    def test_buscar_grado(self):
        grado = self.__crear_grado()
        GradoService.crear_grado(grado)
        grado_encontrado = GradoService.buscar_grado(grado.id)
        self.assertIsNotNone(grado_encontrado)
        self.assertEqual(grado_encontrado.nombre, grado.nombre)
        
    def test_actualizar_grado(self):
        grado = self.__crear_grado()
        GradoService.crear_grado(grado)
        nuevos_datos_grado = Grado()
        nuevos_datos_grado.nombre = "Ingenieria en Sistemas Actualizada"
        grado_modificado = GradoService.actualizar_grado(nuevos_datos_grado, grado.id)
        grado_encontrado = GradoService.buscar_grado(grado.id)
        self.assertIsNotNone(grado_encontrado)
        self.assertIsNotNone(grado_encontrado.id)
        self.assertGreaterEqual(grado_encontrado.id, 1)
        self.assertEqual(grado_encontrado.nombre, grado_modificado.nombre)
              
    def test_eliminar_grado(self):
        grado = self.__crear_grado()
        GradoService.crear_grado(grado)
        GradoService.eliminar_grado(grado.id)
        
    def __crear_grado(self):
        grado = Grado()
        grado.nombre = 'Ingenieria en Sistemas'
        return grado
    
if __name__ == '__main__':
    unittest.main()