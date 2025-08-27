from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class Cargo(HashidMixin ,db.Model):
    __tablename__ = 'cargos'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre: str = db.Column(db.String(100), nullable=False)
    puntos: int = db.Column(db.Integer, nullable=False)
    categoria_cargo_id: int = db.Column(db.Integer, db.ForeignKey('categorias_cargo.id'), nullable=False)

    categoria = db.relationship('CategoriaCargo', back_populates='cargos', lazy='joined')
    autoridades = db.relationship("Autoridad", back_populates="cargo", lazy="select")