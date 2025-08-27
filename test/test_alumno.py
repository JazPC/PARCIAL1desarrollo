import unittest
from flask import current_app
from app import create_app
from app.services import AlumnoService
from app.services import UsuarioService
from app.models import Alumno, Universidad, Especialidad, Facultad, Usuario
from app.services import AlumnoService, UniversidadService, EspecialidadService, FacultadService, UsuarioService
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

    def test_Alumno(self):
        alumno= self.__crear_alumno()
        self.assertEqual(alumno.nombre, 'Agostina')
        self.assertEqual(alumno.apellido, "Gualpa")
        self.assertEqual(alumno.nroDocumento, "12345678")
        self.assertEqual(alumno.fechaNacimiento, "2005-03-30")
        self.assertEqual(alumno.tipoDocumento, "DNI")
        self.assertEqual(alumno.sexo, "F")
        self.assertEqual(alumno.nroLegajo, 10066)
        self.assertEqual(alumno.fechaIngreso, "2020-01-01")
        self.assertEqual(alumno.carrera, "Ingenieria en Sistemas")
        self.assertEqual(alumno.universidad_id, 1)


    def test_crear_alumno(self):

        
        alumno= self.__crear_alumno()
        alumno_guardada = AlumnoService.crear_alumno(alumno)
        self.assertIsNotNone(alumno_guardada)
        self.assertIsNotNone(alumno.id)
        self.assertGreaterEqual(alumno_guardada.id, 1)
        self.assertEqual(alumno_guardada.nombre, alumno.nombre)
        self.assertEqual(alumno_guardada.apellido, alumno.apellido)
        self.assertEqual(alumno_guardada.nroDocumento, alumno.nroDocumento)
        self.assertEqual(alumno_guardada.fechaNacimiento, alumno.fechaNacimiento)
        self.assertEqual(alumno_guardada.tipoDocumento, alumno.tipoDocumento)
        self.assertEqual(alumno_guardada.sexo, alumno.sexo)
        self.assertEqual(alumno_guardada.nroLegajo, alumno.nroLegajo)
        self.assertEqual(alumno_guardada.fechaIngreso, alumno.fechaIngreso)
        self.assertEqual(alumno_guardada.carrera, alumno.carrera)      


    def test_buscar_alumno(self):
        
        alumno = self.__crear_alumno()
        AlumnoService.crear_alumno(alumno)

        alumno_encontrada= AlumnoService.buscar_alumno(1)
        self.assertIsNotNone(alumno)
        self.assertIsNotNone(alumno.id)
        self.assertGreaterEqual(alumno.id, 1)
        self.assertEqual(alumno.nombre, alumno_encontrada.nombre)
        self.assertEqual(alumno.apellido, alumno_encontrada.apellido)
        self.assertEqual(alumno.nroDocumento, alumno_encontrada.nroDocumento)
        self.assertEqual(alumno.fechaNacimiento, alumno_encontrada.fechaNacimiento)
        self.assertEqual(alumno.tipoDocumento, alumno_encontrada.tipoDocumento)
        self.assertEqual(alumno.sexo, alumno_encontrada.sexo)
        self.assertEqual(alumno.nroLegajo, alumno_encontrada.nroLegajo)
        self.assertEqual(alumno.fechaIngreso, alumno_encontrada.fechaIngreso)   
        self.assertEqual(alumno.carrera, alumno_encontrada.carrera)


    def test_actualizar_alumno(self):
        alumno = self.__crear_alumno()
        AlumnoService.crear_alumno(alumno)
        nuevosdatosalumno= Alumno()
        nuevosdatosalumno.nombre = "cele"
        nuevosdatosalumno.apellido = "Gomez"
        nuevosdatosalumno.nroDocumento = "43287405"
        nuevosdatosalumno.fechaNacimiento = "2005-02-10"
        nuevosdatosalumno.tipoDocumento = "DNI"
        nuevosdatosalumno.sexo = "F"
        nuevosdatosalumno.nroLegajo = 10069
        nuevosdatosalumno.fechaIngreso = "2020-01-01"
        nuevosdatosalumno.carrera = "Ingenieria en Sistemas"

        alumnomodificada = AlumnoService.actualizar_alumno(nuevosdatosalumno, alumno.id)
        alumnoencontrada = AlumnoService.buscar_alumno(alumno.id)
        self.assertIsNotNone(alumnoencontrada)
        self.assertIsNotNone(alumnoencontrada.id)
        self.assertGreaterEqual(alumnoencontrada.id, 1)
        self.assertEqual(alumnoencontrada.nombre, alumnomodificada.nombre)
        self.assertEqual(alumnoencontrada.apellido, alumnomodificada.apellido)
        self.assertEqual(alumnoencontrada.nroDocumento, alumnomodificada.nroDocumento)
        self.assertEqual(alumnoencontrada.fechaNacimiento, alumnomodificada.fechaNacimiento)
        self.assertEqual(alumnoencontrada.tipoDocumento, alumnomodificada.tipoDocumento)
        self.assertEqual(alumnoencontrada.sexo, alumnomodificada.sexo)
        self.assertEqual(alumnoencontrada.nroLegajo, alumnomodificada.nroLegajo)
        self.assertEqual(alumnoencontrada.fechaIngreso, alumnomodificada.fechaIngreso)
        self.assertEqual(alumnoencontrada.carrera, alumnomodificada.carrera)

    

    def test_eliminar_alumno(self):
        alumno = self.__crear_alumno()
        AlumnoService.crear_alumno(alumno)
        AlumnoService.eliminar_alumno(alumno.id)
        alumno_encontrada = AlumnoService.buscar_alumno(alumno.id)
        self.assertIsNone(alumno_encontrada)


    def __crear_alumno (self):
        usuario = Usuario()

        usuario.nombredeusuario = "alguien"
        usuario.password = "alguien.123"
        usuario.actividad = True
        UsuarioService.guardar_usuario(usuario)
        
        universidad = Universidad()
        universidad.nombre = "Universidad Tecnologica Nacional"
        universidad.sigla = "UTN"
        universidad.tipo = "publica"
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
        FacultadService.crear_facultad(facultad)

        especialidad = Especialidad()
        especialidad.nombre = "Ingenieria en Sistemas"
        especialidad.letra = "IS"
        especialidad.observacion = "Ingenieria en Sistemas"
        especialidad.facultad_id = facultad.id
        EspecialidadService.crear_especialidad(especialidad)

        alumno = Alumno()
        alumno.nombre = "Agostina"
        alumno.apellido = "Gualpa"
        alumno.nroDocumento = "12345678"
        alumno.fechaNacimiento = "2005-03-30"
        alumno.tipoDocumento = "DNI"
        alumno.sexo = "F"
        alumno.nroLegajo = 10066
        alumno.fechaIngreso = "2020-01-01"
        alumno.carrera = "Ingenieria en Sistemas"
        alumno.usuario_id = usuario.id
        alumno.universidad_id = universidad.id
        alumno.especialidad_id = especialidad.id
        alumno.usuario_id = usuario.id
        

        return alumno
    
if __name__ == '__main__':
    unittest.main()