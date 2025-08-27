import os
import unittest
from app import create_app, db
from app.models import Nota, Materia, Alumno, Autoridad, Cargo, CategoriaCargo, Universidad, Especialidad, Usuario
from app.services import ( NotaService, MateriaService, AlumnoService, 
    UniversidadService, EspecialidadService, UsuarioService,
    AutoridadService, CargoService, CategoriaCargoService
)

class NotaTestCase(unittest.TestCase):

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

    def test_nota(self):
        nota = self.__crear_nota()
        self.assertEqual(nota.alumno_id, 1)
        self.assertEqual(nota.materia_id, 1)
        self.assertEqual(nota.autoridad_id, 1)
        self.assertEqual(nota.nota, 10)

    def test_guardar_nota(self):
        nota = self.__crear_nota()
        nota_guardada = NotaService.guardar_nota(nota)
        alumno = AlumnoService.buscar_alumno(1)

        self.assertIsNotNone(nota_guardada)
        self.assertIsNotNone(nota_guardada.id)
        self.assertGreaterEqual(nota_guardada.id, 1)
        self.assertEqual(nota_guardada.alumno_id, alumno.id)
        self.assertEqual(nota_guardada.materia_id, 1)
        self.assertEqual(nota_guardada.autoridad_id, 1)
        self.assertEqual(nota_guardada.nota, 10)

    def test_buscar_nota(self):
        nota = self.__crear_nota()
        alumno = AlumnoService.buscar_alumno(1)
        NotaService.guardar_nota(nota)

        nota_encontrada = NotaService.buscar_nota(alumno.id)

        self.assertIsNotNone(nota_encontrada)
        self.assertIsNotNone(nota_encontrada.id)
        self.assertGreaterEqual(nota_encontrada.id, 1)
        self.assertEqual(nota_encontrada.alumno_id, alumno.id)
        self.assertEqual(nota_encontrada.materia_id, 1)
        self.assertEqual(nota_encontrada.autoridad_id, 1)
        self.assertEqual(nota_encontrada.nota, 10)

    def test_relacion_nota_autoridad(self):
        nota = self.__crear_nota()
        nota_guardada = NotaService.guardar_nota(nota)
        autoridad_recargada = AutoridadService.buscar_por_id(nota_guardada.autoridad_id)

        self.assertEqual(nota_guardada.autoridad_id, autoridad_recargada.id)
        self.assertEqual(nota_guardada.autoridad.nombre, autoridad_recargada.nombre)
        self.assertIn(nota_guardada, autoridad_recargada.notas)

    def __crear_nota(self):
        materia = Materia(
            nombre='Algebra y geometria',
            diseno_curricular='diseno curricular',
            horas_dictadas='36',
            promocional=True,
            nivel='1',
        )
        MateriaService.crear_materia(materia)  

        alumno = self.__crear_alumno()
        alumno_guardado = AlumnoService.crear_alumno(alumno)  

        autoridad = self.__crear_autoridad()  

        nota = Nota()
        nota.alumno_id = alumno_guardado.id
        note_materia_id = materia.id
        nota.materia_id = note_materia_id
        nota.autoridad_id = autoridad.id
        nota.nota = 10
        return nota

    def __crear_alumno(self):
        universidad = Universidad()
        universidad.nombre = "Universidad Tecnologica Nacional"
        universidad.sigla = "UTN"
        universidad.tipo = "publica"
        UniversidadService.crear_universidad(universidad)

        especialidad = Especialidad()
        especialidad.nombre = "Ingenieria en Sistemas"
        especialidad.letra = "IS"
        especialidad.observacion = "Ingenieria en Sistemas"
        EspecialidadService.crear_especialidad(especialidad)

        usuario = Usuario()
        usuario.nombredeusuario = "alguien"
        usuario.password = "alguien.123"
        usuario.actividad = True
        UsuarioService.guardar_usuario(usuario)

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
        alumno.universidad_id = universidad.id
        alumno.especialidad_id = especialidad.id
        alumno.usuario_id = usuario.id
        return alumno

    def __crear_autoridad(self):
        categoria = CategoriaCargo(nombre="Docente Universitario")
        CategoriaCargoService.crear(categoria)  

        cargo = Cargo(nombre="Titular", puntos=10, categoria_cargo_id=categoria.id)
        CargoService.crear(cargo)  

        autoridad = Autoridad(
            nombre="Profe test",
            telefono="123456789",
            email="profetest@test.com",
            cargo_id=cargo.id
        )
        AutoridadService.crear_autoridad(autoridad) 
        return autoridad


if __name__ == '__main__':
    unittest.main()
