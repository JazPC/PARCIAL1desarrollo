import unittest
from flask import current_app
from app import create_app
from app.models import Orientacion
from app.services import OrientacionService
from app import db
import os

class OrientacionTestCase(unittest.TestCase):

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
  
    def test_orientacion(self):
        orientacion = Orientacion()
        orientacion.nombre = 'Sistemas'
        
        self.assertEqual(orientacion.nombre, 'Sistemas')
        
    def test_crear_orientacion(self):
        orientacion = self.__crear_orientacion()
        orientacion_guardada = OrientacionService.crear_orientacion(orientacion)
        self.assertIsNotNone(orientacion_guardada)
        self.assertIsNotNone(orientacion_guardada.id)
        self.assertGreaterEqual(orientacion_guardada.id, 1)
        self.assertEqual(orientacion_guardada.nombre, orientacion.nombre)
        
    def test_buscar_orientacion(self):
        orientacion = self.__crear_orientacion()
        OrientacionService.crear_orientacion(orientacion)
        orientacion_encontrada = OrientacionService.buscar_orientacion(orientacion.id)
        self.assertIsNotNone(orientacion_encontrada)
        self.assertEqual(orientacion_encontrada.nombre, orientacion.nombre)
        
    def test_actualizar_orientacion(self):
        orientacion = self.__crear_orientacion()
        OrientacionService.crear_orientacion(orientacion)
        nuevos_datos_orientacion = Orientacion()
        nuevos_datos_orientacion.nombre = "Sistemas Actualizada"
        orientacion_modificada = OrientacionService.actualizar_orientacion(nuevos_datos_orientacion, orientacion.id)
        orientacion_encontrada = OrientacionService.buscar_orientacion(orientacion.id)
        self.assertIsNotNone(orientacion_encontrada)
        self.assertIsNotNone(orientacion_encontrada.id)
        self.assertGreaterEqual(orientacion_encontrada.id, 1)
        self.assertEqual(orientacion_encontrada.nombre, orientacion_modificada.nombre)
        
    def test_eliminar_orientacion(self):
        orientacion = self.__crear_orientacion()
        OrientacionService.crear_orientacion(orientacion)
        OrientacionService.eliminar_orientacion(orientacion.id)
        orientacion_encontrada = OrientacionService.buscar_orientacion(orientacion.id)
        self.assertIsNone(orientacion_encontrada)
        
    
    def __crear_orientacion(self):
        orientacion = Orientacion()
        orientacion.nombre = 'Sistemas'
        return orientacion

if __name__ == '__main__':
    unittest.main()