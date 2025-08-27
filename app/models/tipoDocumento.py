from dataclasses import dataclass
from app import db

dataclass(init=False,repr=True, eq=True)
class TipoDocumento(db.Model):
  __tablename__ = 'tipodocumentos'
  id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
  codigo: str = db.Column(db.String(6), nullable=False)
  descripcion: str = db.Column(db.String(100), nullable=False)

