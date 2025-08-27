import unittest
from flask import current_app
from app import create_app, db
from app.models import TipoEspecialidad
from app.services import TipoespecialidadService
import os

class TipoEspecialidadTestCase(unittest.TestCase):

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

    def test_crear_tipoespecialidad(self):
        tipo = self.__crear_tipoespecialidad()
        tipo_guardado = TipoespecialidadService.crear_tipoespecialidad(tipo)
        self.assertIsNotNone(tipo_guardado)
        self.assertIsNotNone(tipo_guardado.id)
        self.assertEqual(tipo_guardado.nombre, tipo.nombre)
        self.assertEqual(tipo_guardado.nivel, tipo.nivel)

    def test_buscar_tipoespecialidad(self):
        tipo = self.__crear_tipoespecialidad()
        TipoespecialidadService.crear_tipoespecialidad(tipo)

        tipo_encontrado = TipoespecialidadService.buscar_tipoespecialidad(1)
        self.assertIsNotNone(tipo_encontrado)
        self.assertEqual(tipo.nombre, tipo_encontrado.nombre)
        self.assertEqual(tipo.nivel, tipo_encontrado.nivel)

    def test_actualizar_tipoespecialidad(self):
        tipo = self.__crear_tipoespecialidad()
        TipoespecialidadService.crear_tipoespecialidad(tipo)

        nuevos_datos = TipoEspecialidad()
        nuevos_datos.nombre = 'Nuevo nombre'
        nuevos_datos.nivel = 'Nuevo nivel'

        tipo_modificado = TipoespecialidadService.actualizar_tipoespecialidad(nuevos_datos, tipo.id)
        tipo_encontrado = TipoespecialidadService.buscar_tipoespecialidad(tipo.id)

        self.assertEqual(tipo_encontrado.nombre, tipo_modificado.nombre)
        self.assertEqual(tipo_encontrado.nivel, tipo_modificado.nivel)

    def test_eliminar_tipoespecialidad(self):
        tipo = self.__crear_tipoespecialidad()
        TipoespecialidadService.crear_tipoespecialidad(tipo)

        TipoespecialidadService.eliminar_tipoespecialidad(tipo.id)
        tipo_eliminado = TipoespecialidadService.buscar_tipoespecialidad(tipo.id)

        self.assertIsNone(tipo_eliminado)

    def __crear_tipoespecialidad(self):
        tipo = TipoEspecialidad()
        tipo.nombre = 'Nombre del tipo de especialidad'
        tipo.nivel = 'Nivel del Tipo de especialidad'
        return tipo

if __name__ == '__main__':
    unittest.main()
