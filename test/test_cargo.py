import unittest
import os
from app import db
from flask import current_app
from app import create_app
from app.models import Cargo, CategoriaCargo
from app.services import CargoService, CategoriaCargoService

class CargoTestCase(unittest.TestCase):

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

    def test_cargo_creation(self):
        cargo = self._nuevoCargo()
        self.assertIsNotNone(cargo)
        self.assertEqual(cargo.nombre, 'Decano')
        self.assertEqual(cargo.puntos, 2)

    def test_crear_cargo(self):
        cargo = self._nuevoCargo()
        CargoService.crear(cargo)
        self.assertIsNotNone(cargo)
        self.assertIsNotNone(cargo.id)
        self.assertGreaterEqual(cargo.id, 1)
        self.assertEqual(cargo.nombre, 'Decano')
        self.assertEqual(cargo.puntos, 2)

    def test_buscar_cargo(self):
        cargo = self._nuevoCargo()
        CargoService.crear(cargo)
        cargo_encontrado = CargoService.buscar_por_id(cargo.id)
        self.assertIsNotNone(cargo_encontrado)
        self.assertEqual(cargo_encontrado.nombre, 'Decano')
        self.assertEqual(cargo_encontrado.puntos, 2)

    def test_buscar_cargos(self):
        cargo1 = self._nuevoCargo()
        cargo2 = self._nuevoCargo()
        cargo2.nombre = 'Profesor'
        cargo2.puntos = 1
        CargoService.crear(cargo1)
        CargoService.crear(cargo2)
        cargos = CargoService.buscar_todos()
        self.assertEqual(len(cargos), 2)
        self.assertIn(cargo1, cargos)
        self.assertIn(cargo2, cargos)

    def test_actualizar_cargo(self):
        cargo = self._nuevoCargo()
        CargoService.crear(cargo)
        cargo.nombre = 'Decano Actualizado'
        cargo.puntos = 3
        cargo_actualizado = CargoService.actualizar(cargo.id, cargo)
        self.assertIsNotNone(cargo_actualizado)
        self.assertEqual(cargo_actualizado.nombre, 'Decano Actualizado')
        self.assertEqual(cargo_actualizado.puntos, 3)

    def test_cargo_tiene_categoria(self):
        cargo = self._nuevoCargo()
        CargoService.crear(cargo)

        cargo_guardada = CargoService.buscar_por_id(cargo.id)
        self.assertIsNotNone(cargo_guardada.categoria)
        self.assertEqual(cargo_guardada.categoria.nombre, 'Administrativo')

    def _nuevoCargo(self):
        categoria = CategoriaCargo(nombre='Administrativo')
        CategoriaCargoService.crear(categoria)

        cargo = Cargo()
        cargo.nombre = 'Decano'
        cargo.puntos = 2
        cargo.categoria_cargo_id = categoria.id
        return cargo

if __name__ == '__main__':
    unittest.main()

