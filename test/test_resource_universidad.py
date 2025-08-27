# import unittest
# import os
# from app import db
# from flask import current_app
# from app import create_app
# from mapping 

# class PlanTestCase(unittest.TestCase):

#     def setUp(self):
#         os.environ['FLASK_CONTEXT'] = 'testing'
#         self.app = create_app()
#         self.app_context = self.app.app_context()
#         self.app_context.push()
#         db.create_all()

#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()
#         self.app_context.pop()
        
#     def test_obtener_todos(self):
#         client = self.app.test_client(use_cookies=True)
#         universidad1 = nuevaUniversidad()
#         universidad2 = nuevaUniversidad()
#         universidad_mapping = UniversidadMapping() #json a objeto
#         response = client.get('http://localhost:5000/api/v1/universidad')
#         universidades = universidad_mapping.load(response.get_json(), many=True)
#         self.assertEqual(len(universidades), 2)
#         self.assertEqual(response.status_code, 200)
#         self.assertIsNotNone(response.get_json())
        