from flask_hashids import HashidMixin
from dataclasses import dataclass
from app import db

@dataclass
class Autoridad(HashidMixin,db.Model):
    __tablename__ = "autoridades"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    telefono: str = db.Column(db.String(20), nullable=False)
    email: str = db.Column(db.String(100), nullable=False)

    notas = db.relationship("Nota", back_populates="autoridad")

    cargo_id: int = db.Column(db.Integer, db.ForeignKey('cargos.id'), nullable=False)
    cargo = db.relationship("Cargo", back_populates="autoridades", lazy="joined")
    