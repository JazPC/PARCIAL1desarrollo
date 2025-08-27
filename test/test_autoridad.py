import unittest
import os
from flask import current_app
from app import create_app, db
from app.models import Autoridad, Cargo, CategoriaCargo
from app.services import AutoridadService, CargoService, CategoriaCargoService

class AutoridadTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.categoria = CategoriaCargo(nombre="Administrativo")
        CategoriaCargoService.crear(self.categoria)

        self.cargo = Cargo(nombre="Decano", puntos=2, categoria_cargo_id=self.categoria.id)
        CargoService.crear(self.cargo)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_autoridad_creation(self):
        autoridad = Autoridad(
            nombre="Dra. Ana Perez",
            telefono="123456789",
            email="ana.perez@universidad.edu",
            cargo_id=self.cargo.id
        )
        self.assertEqual(autoridad.nombre, "Dra. Ana Perez")
        self.assertEqual(autoridad.telefono, "123456789")
        self.assertEqual(autoridad.email, "ana.perez@universidad.edu")
        self.assertEqual(autoridad.cargo_id, self.cargo.id)

    def test_crear_autoridad(self):
        autoridad = self._nueva_autoridad(self.cargo.id)
        guardada = AutoridadService.crear_autoridad(autoridad)

        self.assertIsNotNone(guardada.id)
        self.assertGreaterEqual(guardada.id, 1)
        self.assertEqual(guardada.nombre, "Dra. Ana Perez")
        self.assertEqual(guardada.cargo_id, self.cargo.id)

    def test_buscar_autoridad_por_id(self):
        autoridad = self._nueva_autoridad(self.cargo.id)
        guardada = AutoridadService.crear_autoridad(autoridad)

        encontrada = AutoridadService.buscar_por_id(guardada.id)
        self.assertIsNotNone(encontrada)
        self.assertEqual(encontrada.nombre, "Dra. Ana Perez")
        self.assertEqual(encontrada.cargo_id, self.cargo.id)

    def test_buscar_autoridades(self):
        a1 = self._nueva_autoridad(self.cargo.id)
        a2 = self._nueva_autoridad(self.cargo.id)
        a2.nombre = "Dra. Beatriz"

        AutoridadService.crear_autoridad(a1)
        AutoridadService.crear_autoridad(a2)

        autoridades = AutoridadService.buscar_todas()
        self.assertEqual(len(autoridades), 2)
        self.assertIn(a1, autoridades)
        self.assertIn(a2, autoridades)

    def test_actualizar_autoridad(self):
        guardada = AutoridadService.crear_autoridad(self._nueva_autoridad(self.cargo.id))

        categoria2 = CategoriaCargo(nombre="Académico")
        CategoriaCargoService.crear(categoria2)

        nuevo_cargo = Cargo(nombre="Vicedecano", puntos=3, categoria_cargo_id=categoria2.id)
        CargoService.crear(nuevo_cargo)

        data_update = Autoridad(
            nombre="Dra. Belén",
            telefono="2604567688",
            email="belen@universidad.edu",
            cargo_id=nuevo_cargo.id
        )
        AutoridadService.actualizar_autoridad(guardada.id, data_update)

        encontrada = AutoridadService.buscar_por_id(guardada.id)
        self.assertEqual(encontrada.nombre, "Dra. Belén")
        self.assertEqual(encontrada.telefono, "2604567688")
        self.assertEqual(encontrada.email, "belen@universidad.edu")
        self.assertEqual(encontrada.cargo_id, nuevo_cargo.id)

    def test_borrar_autoridad(self):
        guardada = AutoridadService.crear_autoridad(self._nueva_autoridad(self.cargo.id))
        AutoridadService.borrar_autoridad(guardada.id)
        self.assertIsNone(AutoridadService.buscar_por_id(guardada.id))

    def test_autoridad_tiene_cargo(self):
        guardada = AutoridadService.crear_autoridad(self._nueva_autoridad(self.cargo.id))
        encontrada = AutoridadService.buscar_por_id(guardada.id)

        self.assertIsNotNone(encontrada.cargo)
        self.assertEqual(encontrada.cargo.id, self.cargo.id)
        self.assertEqual(encontrada.cargo.nombre, self.cargo.nombre)

    def _nueva_autoridad(self, cargo_id: int) -> Autoridad:
        return Autoridad(
            nombre="Dra. Ana Perez",
            telefono="123456789",
            email="ana.perez@universidad.edu",
            cargo_id=cargo_id
        )

if __name__ == '__main__':
    unittest.main()
