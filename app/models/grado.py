from dataclasses import dataclass
from app import db

from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class Grado(HashidMixin, db.Model):
  __tablename__ = 'grados'
  id: int = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
  nombre: str = db.Column(db.String(100), nullable=False)
