





"""
from dataclasses import dataclass
from app.models import Cargo

from app import db

@dataclass(init=False,repr=True, eq=True)
class Autoridad(db.Model):
    __tablaname__ = 'autotidades'
    id: int = db.Column(db.Intenger, primary_key, autoincrement=True)
    nombre:str = db.Column(db.String(100), nullable=False)
    telefono:str = db.Column(db.String(20), nullable=True)
    email:str = db.Column(db.String(100), nullable=True)

    cargo_id: int = db.Column(db.Intenger, db.ForeingKey('cargos.id'))
    cargo = db.relationship('Cargo')

    materias = db.relatioship('Materia', secondary= 'autoridad_materias', backref='autoridades')
    def __post_init__(self):
        self.cargo = Cargo.query.get(self.cargo_id) if self.cargo_id else None
"""