from app import db

from dataclasses import dataclass
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class Plan(HashidMixin, db.Model):
    __tablename__ = "planes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    fechaInicio = db.Column(db.String, nullable=False)
    fechaFin = db.Column(db.String, nullable=False)
    observacion = db.Column(db.String(100), nullable=False)

    materias = db.relationship("PlanMateria", back_populates="plan", cascade="all, delete-orphan", lazy="select")
