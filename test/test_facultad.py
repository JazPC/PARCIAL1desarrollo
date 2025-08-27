import unittest
from flask import current_app
from app import create_app
from app.models import Facultad, Universidad
from app.services import FacultadService, UniversidadService
from app import db
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

    def test_facultad(self):
        facultad= self.__crear_facultad()
        self.assertEqual(facultad.nombre, 'Facultad de Ingenieria')
        self.assertEqual(facultad.abreviatura, 'FI')
        self.assertEqual(facultad.directorio, "directorio")
        self.assertEqual(facultad.sigla, "sigla")
        self.assertEqual(facultad.codigoPostal, "codigoPostal")
        self.assertEqual(facultad.ciudad, "ciudad")
        self.assertEqual(facultad.domicilio, "domicilio")
        self.assertEqual(facultad.telefono, "telefono")
        self.assertEqual(facultad.contacto, "contacto")
        self.assertEqual(facultad.email, "email")
        self.assertEqual(facultad.universidad_id, 1)
        
    def test_crear_facultad(self):
        facultad= self.__crear_facultad()
        facultad_guardada = FacultadService.crear_facultad(facultad)
        self.assertIsNotNone(facultad_guardada)
        self.assertIsNotNone(facultad_guardada.id)
        self.assertGreaterEqual(facultad_guardada.id, 1)
        self.assertEqual(facultad_guardada.nombre, facultad.nombre) 
        self.assertEqual(facultad_guardada.abreviatura, facultad.abreviatura) 
        self.assertEqual(facultad_guardada.directorio, facultad.directorio)
        self.assertEqual(facultad_guardada.sigla, facultad.sigla)
        self.assertEqual(facultad_guardada.codigoPostal, facultad.codigoPostal)
        self.assertEqual(facultad_guardada.ciudad, facultad.ciudad)
        self.assertEqual(facultad_guardada.domicilio, facultad.domicilio)
        self.assertEqual(facultad_guardada.telefono, facultad.telefono)
        self.assertEqual(facultad_guardada.contacto, facultad.contacto)
        self.assertEqual(facultad_guardada.email, facultad.email)
        self.assertEqual(facultad_guardada.universidad_id, 1)

    def test_buscar_facultad(self):
        
        facultad = self.__crear_facultad()
        FacultadService.crear_facultad(facultad)

        facultad_encontrada= FacultadService.buscar_facultad(1)
        self.assertIsNotNone(facultad)
        self.assertIsNotNone(facultad.id)
        self.assertGreaterEqual(facultad.id, 1)
        self.assertEqual(facultad.nombre, facultad_encontrada.nombre)
        self.assertEqual(facultad.abreviatura, facultad_encontrada.abreviatura)
        self.assertEqual(facultad.directorio, facultad_encontrada.directorio)
        self.assertEqual(facultad.sigla, facultad_encontrada.sigla)
        self.assertEqual(facultad.codigoPostal, facultad_encontrada.codigoPostal)
        self.assertEqual(facultad.ciudad, facultad_encontrada.ciudad)
        self.assertEqual(facultad.domicilio, facultad_encontrada.domicilio)
        self.assertEqual(facultad.telefono, facultad_encontrada.telefono)
        self.assertEqual(facultad.contacto, facultad_encontrada.contacto)
        self.assertEqual(facultad.email, facultad_encontrada.email) 

    def test_actualizar_facultad(self):
        facultad = self.__crear_facultad()
        FacultadService.crear_facultad(facultad)
        nuevosdatosfacultad = Facultad()
        nuevosdatosfacultad.nombre = 'Facultad de Ingenieriaa'
        nuevosdatosfacultad.abreviatura = 'FI'
        nuevosdatosfacultad.directorio = "directorio"
        nuevosdatosfacultad.sigla = "sigla"
        nuevosdatosfacultad.codigoPostal = "codigoPostal"
        nuevosdatosfacultad.ciudad = "ciudad"
        nuevosdatosfacultad.domicilio = "domicilio"
        nuevosdatosfacultad.telefono = "telefono"
        nuevosdatosfacultad.contacto = "contacto"
        nuevosdatosfacultad.email = "email"
        facultadmodificada = FacultadService.actualizar_facultad(nuevosdatosfacultad, facultad.id)
        facultadencontrada = FacultadService.buscar_facultad(facultad.id)
        self.assertIsNotNone(facultadencontrada)
        self.assertIsNotNone(facultadencontrada.id)
        self.assertGreaterEqual(facultadencontrada.id, 1)
        self.assertEqual(facultadencontrada.nombre, facultadmodificada.nombre)
        self.assertEqual(facultadencontrada.abreviatura, facultadmodificada.abreviatura)
        self.assertEqual(facultadencontrada.directorio, facultadmodificada.directorio)
        self.assertEqual(facultadencontrada.sigla, facultadmodificada.sigla)
        self.assertEqual(facultadencontrada.codigoPostal, facultadmodificada.codigoPostal)        
        self.assertEqual(facultadencontrada.ciudad, facultadmodificada.ciudad)
        self.assertEqual(facultadencontrada.domicilio, facultadmodificada.domicilio)        
        self.assertEqual(facultadencontrada.telefono, facultadmodificada.telefono)
        self.assertEqual(facultadencontrada.contacto, facultadmodificada.contacto)        
        self.assertEqual(facultadencontrada.email, facultadmodificada.email) 

    def test_eliminar_facultad(self):
        facultad = self.__crear_facultad()
        FacultadService.crear_facultad(facultad)
        FacultadService.eliminar_facultad(facultad.id)
        facultad_encontrada = FacultadService.buscar_facultad(facultad.id)
        self.assertIsNone(facultad_encontrada)
    
    def test_facultad_tiene_universidad(self):
        facultad = self.__crear_facultad()
        FacultadService.crear_facultad(facultad)

        facultad_guardada = FacultadService.buscar_facultad(facultad.id)
        self.assertIsNotNone(facultad_guardada.universidad)
        self.assertEqual(facultad_guardada.universidad.nombre, "Universidad Tecnologica Nacional")


    def __crear_facultad(self):
        universidad = Universidad(
        nombre="Universidad Tecnologica Nacional",
        sigla="UTN",
        tipo="publica"
        )
        UniversidadService.crear_universidad(universidad)
        facultad = Facultad()
        facultad.nombre = 'Facultad de Ingenieria'
        facultad.abreviatura = 'FI'
        facultad.directorio = "directorio"
        facultad.sigla = "sigla"
        facultad.codigoPostal = "codigoPostal"
        facultad.ciudad = "ciudad"
        facultad.domicilio = "domicilio"
        facultad.telefono = "telefono"
        facultad.contacto = "contacto"
        facultad.email = "email"
        facultad.universidad_id = universidad.id
        return facultad 
    
if __name__ == '__main__':
    unittest.main()