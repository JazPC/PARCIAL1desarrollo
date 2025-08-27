from app import db

from dataclasses import dataclass
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class PlanMateria(HashidMixin, db.Model):
    __tablename__ = "planes_materias"
    id : int = db.Column(db.Integer, primary_key=True, autoincrement=True)

    plan_id : int = db.Column(db.Integer, db.ForeignKey("planes.id", ondelete="CASCADE"), nullable=False)
    materia_id : int = db.Column(db.Integer, db.ForeignKey("materias.id"), nullable=False)

    anio = db.Column(db.SmallInteger, nullable=False)           
    dictado : str = db.Column(db.String(10), nullable=True)          
    se_cursa : bool = db.Column(db.Boolean(), nullable=False, default=True)
    se_rinde : bool = db.Column(db.Boolean(), nullable=True)
    orden : int = db.Column(db.Integer(), nullable=True, default=0)

    plan = db.relationship("Plan", back_populates="materias")
    materia = db.relationship("Materia", back_populates="planes")
    
    __table_args__ = (
        db.UniqueConstraint("plan_id", "materia_id", name="uq_plan_materia"),
        db.Index("ix_pm_plan_anio_orden", "plan_id", "anio", "orden"),
    )