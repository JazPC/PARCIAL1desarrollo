import unittest
import os
from app import db
from flask import current_app
from app import create_app
from app.models import Area
from app.services import AreaService

class AreaTestCase(unittest.TestCase):

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

    def test_area_creation(self):
        area = self._nuevoArea()
        self.assertIsNotNone(area)
        self.assertEqual(area.nombre, 'Materias Basicas')

    def test_crear_area(self):
        area = self._nuevoArea()
        AreaService.crear_area(area)
        self.assertIsNotNone(area)
        self.assertIsNotNone(area.id)
        self.assertGreaterEqual(area.id, 1)
        self.assertEqual(area.nombre, 'Materias Basicas')

    def test_buscar_area(self):
        area= self._nuevoArea()
        AreaService.crear_area(area)
        area_encontrado = AreaService.buscar_area_por_id(area.id)
        self.assertIsNotNone(area_encontrado)
        self.assertEqual(area_encontrado.nombre, 'Materias Basicas')

    def test_listar_area(self):
        area1 = self._nuevoArea()
        area2 = self._nuevoArea()
        area2.nombre = 'Electivas'
        AreaService.crear_area(area1)
        AreaService.crear_area(area2)
        areas = AreaService.listar_area()
        self.assertEqual(len(areas), 2)
        self.assertIn(area1, areas)
        self.assertIn(area2, areas)

    def test_actualizar_areas(self):
        area = self._nuevoArea()
        AreaService.crear_area(area)
        area.nombre = 'area Actualizado'
        area_actualizado = AreaService.actualizar_area(area.id, area)
        self.assertIsNotNone(area_actualizado)
        self.assertEqual(area_actualizado.nombre, 'area Actualizado')

    def test_borrar_area(self):
        area= self._nuevoArea()
        AreaService.crear_area(area)
        area_borrado = AreaService.borrar_por_id(area.id)
        self.assertIsNotNone(area_borrado)
        self.assertEqual(area_borrado.nombre, 'Materias Basicas')
        area_buscado = AreaService.buscar_area_por_id(area.id)
        self.assertIsNone(area_buscado)

    def _nuevoArea(self):
        area = Area()
        area.nombre = 'Materias Basicas'
        return area

if __name__ == '__main__':
    unittest.main()

