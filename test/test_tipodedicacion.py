import unittest
from flask import current_app
from app import create_app, db
from app.models import TipoDedicacion
from app.services import TipoDedicacionService
import os
class TipoDedicacionTestCase(unittest.TestCase):  

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

    def test_crear_tipo_dedicacion(self):
        tipo_dedicacion = self.__nueva_dedicacion()
        tipo_dedicacion_guardada = TipoDedicacionService.crear_tipo_dedicacion(tipo_dedicacion)
        
        self.assertIsNotNone(tipo_dedicacion_guardada)
        self.assertIsNotNone(tipo_dedicacion_guardada.id)
        self.assertGreaterEqual(tipo_dedicacion_guardada.id, 1)
        self.assertEqual(tipo_dedicacion_guardada.nombre, tipo_dedicacion.nombre)
        self.assertEqual(tipo_dedicacion_guardada.observacion, tipo_dedicacion.observacion)

    def test_buscar_tipo_dedicacion_por_id(self):
        tipo_dedicacion = self.__nueva_dedicacion()
        tipo_dedicacion_guardada = TipoDedicacionService.crear_tipo_dedicacion(tipo_dedicacion)
        resultado = TipoDedicacionService.buscar_por_id(tipo_dedicacion_guardada.id)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre,'Exclusiva')
    
    def test_actualizar_tipo_dedicacion(self):
        tipo_dedicacion = self.__nueva_dedicacion()  
        tipo_dedicacion_guardada = TipoDedicacionService.crear_tipo_dedicacion(tipo_dedicacion)

        tipo_dedicacion_actualizada = TipoDedicacion(
            nombre = 'Exclusiva',
            observacion = 'dedicacion exclusiva',
        )


        tipo_dedicacion_modificada = TipoDedicacionService.actualizar_tipo_dedicacion(tipo_dedicacion_guardada.id, tipo_dedicacion_actualizada)

        tipo_dedicacion_encontrada = TipoDedicacionService.buscar_por_id(tipo_dedicacion_guardada.id)
        
        self.assertIsNotNone(tipo_dedicacion_encontrada)
        self.assertIsNotNone(tipo_dedicacion_encontrada.id)
        self.assertGreaterEqual(tipo_dedicacion_encontrada.id, 1)
        self.assertEqual(tipo_dedicacion_encontrada.nombre, tipo_dedicacion_modificada.nombre)
        self.assertEqual(tipo_dedicacion_encontrada.observacion, tipo_dedicacion_modificada.observacion)
        
    def test_borrar_tipo_dedicacion(self):
        tipo_dedicacion = self.__nueva_dedicacion()
        tipo_dedicacion_guardada = TipoDedicacionService.crear_tipo_dedicacion(tipo_dedicacion)
        TipoDedicacionService.borrar_tipo_dedicacion(tipo_dedicacion_guardada.id)
        tipo_dedicacion_encontrada = TipoDedicacionService.buscar_por_id(tipo_dedicacion_guardada.id)
        self.assertIsNone(tipo_dedicacion_encontrada)

    def __nueva_dedicacion(self):
        return TipoDedicacion(nombre='Exclusiva', observacion='Dedicación exclusiva')

    

if __name__ == '__main__':
    unittest.main()