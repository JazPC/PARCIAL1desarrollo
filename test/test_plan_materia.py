import unittest
import os
from app import db
from flask import current_app
from app import create_app
from app.models import Plan, Materia, PlanMateria, plan
from app.services import PlanService

class PlanMateriaTestCase(unittest.TestCase):

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
    
    def test_agregar_materias_al_plan(self):
        plan = self.__nuevo_plan()
        materia1 = self.__nueva_materia('Álgebra I')
        materia2 = self.__nueva_materia('Análisis I')
        db.session.add_all([plan, materia1, materia2])
        db.session.commit() 

        plan_materia_1 = self.__planes_materias(materia1, anio=1, dictado='1c', orden=20)
        plan_materia_2 = self.__planes_materias(materia2, anio=1, dictado='1c', orden=30)

        plan_result = PlanService.agregar_materias(plan.id, [plan_materia_1, plan_materia_2])

        self.assertIsNotNone(plan_result)
        self.assertIsNotNone(plan_result.id)
        self.assertEqual(plan_result.id, plan.id)
        pr = PlanService.buscar_por_id(plan.id)
        self.assertEqual(len(pr.materias), 2)
        self.assertEqual({plan_materia.materia.nombre for plan_materia in pr.materias}, {'Álgebra I', 'Análisis I'})

    def test_buscar_todos_plan_materia(self):
        plan = self.__nuevo_plan()
        materia1 = self.__nueva_materia('Álgebra I')
        materia2 = self.__nueva_materia('Análisis I')
        db.session.add_all([plan, materia1, materia2])
        db.session.commit()

        plan_materia_1 = self.__planes_materias(materia1, anio=1, dictado='1c', orden=20)
        plan_materia_2 = self.__planes_materias(materia2, anio=2, dictado='2c', se_rinde=True, orden=30)

        PlanService.agregar_materias(plan.id, [plan_materia_1, plan_materia_2])

        todos = PlanService.buscar_todos_plan_materia()
        self.assertGreaterEqual(len(todos), 2)
        nombres = [t.materia.nombre for t in todos]
        self.assertIn('Álgebra I', nombres)
        self.assertIn('Análisis I', nombres)    

    def __nuevo_plan(self, nombre='Ingeniería en Sistemas'):
        plan = Plan(
            nombre=nombre,
            fechaInicio='2024-11-12',
            fechaFin='2024-12-12',
            observacion='Plan de prueba'
        )
        return plan

    def __nueva_materia(self, nombre='Álgebra I'):
        materia = Materia(
            nombre=nombre,
            diseno_curricular='DC',
            horas_dictadas='64',
            promocional=True,
            nivel='Inicial'
        )
        return materia

    def __planes_materias(self, materia: Materia, anio=1, dictado='1c', se_cursa=True, se_rinde=False, orden=10):
        return PlanMateria(
            materia=materia,
            anio=anio,
            dictado=dictado,
            se_cursa=se_cursa,
            se_rinde=se_rinde,
            orden=orden
        )

if __name__ == '__main__':
    unittest.main()
