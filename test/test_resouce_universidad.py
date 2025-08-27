import unittest
from flask import current_app
from app import create_app, db
from app.models import Universidad, Facultad
from app.services import UniversidadService,  FacultadService
import os
import json

class CartTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_crear_universidad(self):
        data = {
            "nombre": "Universidad Test",
            "sigla": "UT",
            "tipo": "Privada"
        }
        response = self.client.post(
            "/api/v1/universidad",
            data=json.dumps(data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("Universidad creada exitosamente", response.get_data(as_text=True))