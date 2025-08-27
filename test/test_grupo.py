import unittest
from flask import current_app
from app import create_app
from app.models import Grupo
from app.services import GrupoService
from app import db
import os

class GrupoTestCase(unittest.TestCase):

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
  

    def test_grupo(self):
        grupo = self.__crear_grupo()
        self.assertEqual(grupo.nombre, 'Nombre del grupo')
    
    def test_crear_grupo(self):
        grupo = self.__crear_grupo()
        grupo_guardado = GrupoService.crear_grupo(grupo)
        self.assertIsNotNone(grupo_guardado)
        self.assertIsNotNone(grupo_guardado.id)
        self.assertGreaterEqual(grupo_guardado.id, 1)
        self.assertEqual(grupo_guardado.nombre, grupo.nombre)

    def test_buscar_facultad(self):
        grupo = self.__crear_grupo()
        GrupoService.crear_grupo(grupo)

        grupo_encontrado = GrupoService.buscar_grupo_por_id(1)
        self.assertIsNotNone(grupo)
        self.assertIsNotNone(grupo.id)
        self.assertGreaterEqual(grupo.id, 1)
        self.assertEqual(grupo.nombre, grupo_encontrado.nombre)

    def test_actualizar_grupo(self):
        grupo = self.__crear_grupo()
        GrupoService.crear_grupo(grupo)
        nuevosdatosgrupo = Grupo()
        nuevosdatosgrupo.nombre = 'Nombre grupo'
        grupomodeficado = GrupoService.actualizar_grupo(nuevosdatosgrupo, grupo.id)
        grupoencontrado = GrupoService.buscar_grupo_por_id(grupo.id)
        self.assertIsNotNone(grupoencontrado)
        self.assertIsNotNone(grupoencontrado.id)
        self.assertGreaterEqual(grupoencontrado.id, 1)
        self.assertEqual(grupoencontrado.nombre, grupomodeficado.nombre)

    def test_eliminar_grupo(self):
        grupo = self.__crear_grupo()
        GrupoService.crear_grupo(grupo)
        GrupoService.eliminar_grupo(grupo.id)
        grupo_encontrado = GrupoService.buscar_grupo_por_id(grupo.id)
        self.assertIsNone(grupo_encontrado)

    def __crear_grupo(self):
        grupo = Grupo()
        grupo.nombre = 'Nombre del grupo'
        return grupo

if __name__ == '__main__':
    unittest.main()