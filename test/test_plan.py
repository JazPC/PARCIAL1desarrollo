import unittest
import os
from app import db
from flask import current_app
from app import create_app
from app.models import Plan
from app.services import PlanService

class PlanTestCase(unittest.TestCase):

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

    def test_plan_creation(self):
        plan = self.__nuevo_plan()
        self.assertIsNotNone(plan)
        self.assertEqual(plan.nombre, 'Sistemas')
        self.assertEqual(plan.fechaInicio, '12 de noviembre 2024')
        self.assertEqual(plan.fechaFin, '12 de diciembre 2024')
        self.assertEqual(plan.observacion, 'Se dicta solo un mes')

    def test_crear_plan(self):
        plan = self.__nuevo_plan()
        PlanService.crear(plan)
        self.assertIsNotNone(plan)
        self.assertIsNotNone(plan.id)
        self.assertGreaterEqual(plan.id, 1)
        self.assertEqual(plan.nombre, 'Sistemas')
    
    def test_plan_busqueda(self):
        plan = self.__nuevo_plan()
        PlanService.crear(plan)
        plan_buscado = PlanService.buscar_por_id(plan.id)
        self.assertIsNotNone(plan_buscado)
        self.assertEqual(plan_buscado.nombre, 'Sistemas')
        self.assertEqual(plan_buscado.fechaInicio, '12 de noviembre 2024')
        self.assertEqual(plan_buscado.fechaFin, '12 de diciembre 2024')
    
    def test_buscar_planes(self):
        plan1 = self.__nuevo_plan()
        plan2 = self.__nuevo_plan()
        plan2.nombre = 'Redes'
        PlanService.crear(plan1)
        PlanService.crear(plan2)
        planes = PlanService.buscar_todos()
        self.assertEqual(len(planes), 2)
        self.assertIn(plan1, planes)
        self.assertIn(plan2, planes)

    def test_actualizar_plan(self):
        plan = self.__nuevo_plan()
        PlanService.crear(plan)
        plan.nombre = 'Sistemas Avanzados'
        plan_actualizado = PlanService.actualizar(plan.id, plan)
        self.assertIsNotNone(plan_actualizado)
        self.assertEqual(plan_actualizado.nombre, 'Sistemas Avanzados') 

    def test_borrar_plan(self): 
        plan = self.__nuevo_plan()
        PlanService.crear(plan)
        plan_borrado = PlanService.borrar_por_id(plan.id)
        self.assertIsNotNone(plan_borrado)
        self.assertEqual(plan_borrado.nombre, 'Sistemas')
        plan_buscado = PlanService.buscar_por_id(plan.id)
        self.assertIsNone(plan_buscado)

    def __nuevo_plan(self):
        plan = Plan()
        plan.nombre = 'Sistemas'
        plan.fechaInicio = '12 de noviembre 2024'
        plan.fechaFin = '12 de diciembre 2024'
        plan.observacion = 'Se dicta solo un mes'
        return plan
    
if __name__ == '__main__':
    unittest.main()

