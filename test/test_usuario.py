import unittest
from flask import current_app
from app import create_app
from app.models import Usuario
from app.services import UsuarioService
from app import db
import os

class AppTestCase(unittest.TestCase):

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

    def test_usuario(self):
        usuario = self.__crear_usuario()
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario.nombredeusuario, 'alguien')
        self.assertEqual(usuario.password, 'alguien.123')
        self.assertEqual(usuario.actividad, True)

    def test_crear_usuario(self):
        usuario = self.__crear_usuario()
        usuario_guardado = UsuarioService.guardar_usuario(usuario)
        self.assertIsNotNone(usuario_guardado)

    def test_listar_usuarios(self):
        usuario = self.__crear_usuario()
        usuario_guardado = UsuarioService.guardar_usuario(usuario)
        usuarios = UsuarioService.listar_usuarios()
        self.assertIsNotNone(usuarios)

    def test_buscar_usuario(self):
        usuario = self.__crear_usuario()
        usuario_guardado = UsuarioService.guardar_usuario(usuario)
        usuario_encontrado = UsuarioService.buscar_usuario(usuario_guardado.id)
        self.assertIsNotNone(usuario_encontrado)
        self.assertEqual(usuario_encontrado.id, usuario_guardado.id)
        self.assertEqual(usuario_encontrado.nombredeusuario, usuario_guardado.nombredeusuario)
        self.assertEqual(usuario_encontrado.password, usuario_guardado.password)
        self.assertEqual(usuario_encontrado.actividad, usuario_guardado.actividad)

    def test_eliminar_usuario(self):
        usuario = self.__crear_usuario()
        UsuarioService.guardar_usuario(usuario)
        UsuarioService.eliminar_usuario(usuario.id)
        usuario_encontrado = UsuarioService.buscar_usuario(usuario.id)
        self.assertIsNone(usuario_encontrado)
        

    def __crear_usuario(self):
        usuario = Usuario()
        usuario.nombredeusuario = 'alguien'
        usuario.password = 'alguien.123'
        usuario.actividad = True
        return usuario
        
    