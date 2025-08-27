import unittest
from flask import current_app
from app import create_app, db
from app.models import Universidad, Facultad
from app.services import UniversidadService,  FacultadService
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

    def test_Universidad(self):
        universidad = self.__crear_universidad()
        self.assertEqual(universidad.nombre, 'Universidad Tecnologica Nacional')
        self.assertEqual(universidad.sigla, "UTN")
        self.assertEqual(universidad.tipo, "publica")

    def test_crear_universidad(self):
        universidad = self.__crear_universidad()
        universidad_guardada = UniversidadService.crear_universidad(universidad)
        self.assertIsNotNone(universidad_guardada)
        self.assertIsNotNone(universidad.id)
        self.assertGreaterEqual(universidad_guardada.id, 1)
        self.assertEqual(universidad_guardada.nombre, universidad.nombre)
        self.assertEqual(universidad_guardada.sigla, universidad.sigla)
        self.assertEqual(universidad_guardada.tipo, universidad.tipo)

    def test_listar_universidades(self):
        universidad = self.__crear_universidad()
        UniversidadService.crear_universidad(universidad)
        universidades = UniversidadService.listar_universidades()
        self.assertIsNotNone(universidades)
        self.assertGreaterEqual(len(universidades), 1)

    def test_buscar_universidad(self):
        universidad = self.__crear_universidad()
        UniversidadService.crear_universidad(universidad)

        universidad_encontrada = UniversidadService.buscar_universidad(1)
        self.assertIsNotNone(universidad)
        self.assertIsNotNone(universidad.id)
        self.assertGreaterEqual(universidad.id, 1)
        self.assertEqual(universidad.nombre, universidad_encontrada.nombre)
        self.assertEqual(universidad.sigla, universidad_encontrada.sigla)
        self.assertEqual(universidad.tipo, universidad_encontrada.tipo)

    def test_actualizar_universidad(self):
        universidad = self.__crear_universidad()
        UniversidadService.crear_universidad(universidad)

        nuevosdatosuniversidad = Universidad()
        nuevosdatosuniversidad.nombre = "Universidad Tecnologica Nacional Modificada"
        nuevosdatosuniversidad.sigla = "UTN Modificada"
        nuevosdatosuniversidad.tipo = 'privada'

        universidadmodificada = UniversidadService.actualizar_universidad(nuevosdatosuniversidad, universidad.id)
        universidadencontrada = UniversidadService.buscar_universidad(universidad.id)

        self.assertIsNotNone(universidadencontrada)
        self.assertIsNotNone(universidadencontrada.id)
        self.assertGreaterEqual(universidadencontrada.id, 1)
        self.assertEqual(universidadencontrada.nombre, universidadmodificada.nombre)
        self.assertEqual(universidadencontrada.sigla, universidadmodificada.sigla)
        self.assertEqual(universidadencontrada.tipo, universidadmodificada.tipo)

    def test_eliminar_universidad(self):
        universidad = self.__crear_universidad()
        UniversidadService.crear_universidad(universidad)
        UniversidadService.eliminar_universidad(universidad.id)

        universidad_encontrada = UniversidadService.buscar_universidad(universidad.id)
        self.assertIsNone(universidad_encontrada)

    def test_universidad_con_facultades(self):
        universidad = self.__crear_universidad()
        UniversidadService.crear_universidad(universidad)

        facultad = Facultad(
            nombre='Facultad Regional Mendoza',
            abreviatura='FRM',
            directorio='directorio',
            sigla='sigla',
            codigoPostal='5500',
            ciudad='Mendoza',
            domicilio='Calle Falsa 123',
            telefono='12345678',
            contacto='Juan Pérez',
            email='contacto@frm.utn.edu.ar',
            universidad_id=universidad.id
        )
        FacultadService.crear_facultad(facultad)
        universidad_con_facultades = UniversidadService.buscar_universidad(universidad.id)
        self.assertIsNotNone(universidad_con_facultades.facultades)
        self.assertEqual(len(universidad_con_facultades.facultades), 1)
        self.assertEqual(universidad_con_facultades.facultades[0].nombre, 'Facultad Regional Mendoza')

    def __crear_universidad(self):
        universidad = Universidad()
        universidad.nombre = "Universidad Tecnologica Nacional"
        universidad.sigla = "UTN"
        universidad.tipo = "publica"
        return universidad


if __name__ == '__main__':
    unittest.main()
