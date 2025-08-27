import unittest
from flask import current_app
from app import create_app, db
from app.models import Materia
from app.services import MateriaService
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


    def test_materia(self):
        materia = Materia()
        materia.nombre = 'Algebra y geometria'
        materia.diseno_curricular = 'diseno curricular'
        materia.horas_dictadas = '36'
        materia.promocional = True
        materia.nivel = '1'
          
        self.assertEqual(materia.nombre, 'Algebra y geometria')
        self.assertEqual(materia.diseno_curricular, 'diseno curricular')
        self.assertEqual(materia.horas_dictadas, '36')
        self.assertEqual(materia.promocional, True)
        self.assertEqual(materia.nivel, '1')
          
    def test_crear_materia(self):
        materia = self.__nueva_materia()
        materia_guardada = MateriaService.crear_materia(materia)
        
        self.assertIsNotNone(materia_guardada)
        self.assertIsNotNone(materia_guardada.id)
        self.assertGreaterEqual(materia_guardada.id,1)
        self.assertEqual(materia_guardada.nombre, materia.nombre)
        
    def test_buscar_materia_por_id(self):
        materia = self.__nueva_materia()
        materia_guardada = MateriaService.crear_materia(materia)
        resultado = MateriaService.buscar_por_id(materia_guardada.id)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre,'Algebra y geometria')
    
    def test_actualizar_materia(self):
        materia = self.__nueva_materia()  
        materia_guardada = MateriaService.crear_materia(materia)

        materia_actualizada = Materia(
            nombre = 'Analisis Matematico',
            diseno_curricular = 'diseno curricular',
            horas_dictadas = '48',
            promocional = True,
            nivel = '1'
        )

        materia_modificada = MateriaService.actualizar_materia(materia_guardada.id, materia_actualizada)

        materia_encontrada = MateriaService.buscar_por_id(materia_guardada.id)
        self.assertIsNotNone(materia_encontrada)
        self.assertIsNotNone(materia_encontrada.id)
        self.assertGreaterEqual(materia_encontrada.id, 1)
        self.assertEqual(materia_encontrada.diseno_curricular, materia_modificada.diseno_curricular)
        self.assertEqual(materia_encontrada.horas_dictadas, materia_modificada.horas_dictadas)
        self.assertEqual(materia_encontrada.promocional, materia_modificada.promocional)
        self.assertEqual(materia_encontrada.nivel, materia_modificada.nivel)
        
    def test_borrar_materia(self):
        materia = self.__nueva_materia()
        materia_guardada = MateriaService.crear_materia(materia)
        MateriaService.borrar_materia(materia_guardada.id)
        materia_encontrada = MateriaService.buscar_por_id(materia_guardada.id)
        self.assertIsNone(materia_encontrada)

    def __nueva_materia(self):
        return Materia(
            nombre= 'Algebra y geometria',
            diseno_curricular = 'diseno curricular',
            horas_dictadas = '36',
            promocional = True,
            nivel = '1',
        )


if __name__ == '__main__':
    unittest.main()