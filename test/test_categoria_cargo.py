import unittest
import os
from app import db
from flask import current_app
from app import create_app
from app.models import CategoriaCargo, Cargo
from app.services import CategoriaCargoService, CargoService

class CategoriaCargoTestCase(unittest.TestCase):

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

    def test_categoria_cargo_creation(self):
        categoria_cargo = self._nuevaCategoriaCargo()
        self.assertIsNotNone(categoria_cargo)
        self.assertEqual(categoria_cargo.nombre, 'Administrativo')
    
    def test_crear_categoria_cargo(self):
        categoria_cargo = self._nuevaCategoriaCargo()
        CategoriaCargoService.crear(categoria_cargo)
        self.assertIsNotNone(categoria_cargo)
        self.assertIsNotNone(categoria_cargo.id)
        self.assertGreaterEqual(categoria_cargo.id, 1)
        self.assertEqual(categoria_cargo.nombre, 'Administrativo')
    
    def test_buscar_categoria_cargo(self):
        categoria_cargo = self._nuevaCategoriaCargo()
        CategoriaCargoService.crear(categoria_cargo)
        categoria_encontrada = CategoriaCargoService.buscar_por_id(categoria_cargo.id)
        self.assertIsNotNone(categoria_encontrada)
        self.assertEqual(categoria_encontrada.nombre, 'Administrativo')
    
    def test_buscar_categorias_cargos(self):
        categoria1 = self._nuevaCategoriaCargo()
        categoria2 = self._nuevaCategoriaCargo()
        categoria2.nombre = 'Docente'
        CategoriaCargoService.crear(categoria1)
        CategoriaCargoService.crear(categoria2)
        categorias = CategoriaCargoService.buscar_todos()
        self.assertEqual(len(categorias), 2)
        self.assertIn(categoria1, categorias)
        self.assertIn(categoria2, categorias)
    
    def test_actualizar_categoria_cargo(self):
        categoria_cargo = self._nuevaCategoriaCargo()
        CategoriaCargoService.crear(categoria_cargo)
        categoria_cargo.nombre = 'Administrativo Actualizado'
        categoria_actualizada = CategoriaCargoService.actualizar(categoria_cargo.id, categoria_cargo)
        self.assertIsNotNone(categoria_actualizada)
        self.assertEqual(categoria_actualizada.nombre, 'Administrativo Actualizado')

    def test_categoria_cargo_con_cargos(self):
        categoria_cargo = self._nuevaCategoriaCargo()
        CategoriaCargoService.crear(categoria_cargo)

        cargo = Cargo(
            nombre='Decano', 
            puntos=2, 
            categoria_cargo_id=categoria_cargo.id)
        CargoService.crear(cargo)

        categoria_con_cargos = CategoriaCargoService.buscar_por_id(categoria_cargo.id)
        self.assertIsNotNone(categoria_con_cargos.cargos)
        self.assertEqual(len(categoria_con_cargos.cargos), 1)
        self.assertEqual(categoria_con_cargos.cargos[0].nombre, 'Decano')

    def _nuevaCategoriaCargo(self):
        categoria_cargo = CategoriaCargo(nombre='Administrativo')
        return categoria_cargo

if __name__ == '__main__':
    unittest.main()

