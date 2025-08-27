from dataclasses import dataclass
from app import db
@dataclass(init=False, repr=True, eq=True)
class Facultad(db.Model):
  __tablename__ = 'facultades'
  id : int = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nombre: str = db.Column(db.String(100), nullable=False)
  abreviatura: str = db.Column(db.String(100), nullable=False)
  directorio: str =  db.Column(db.String(100), nullable=False)
  sigla: str = db.Column(db.String(100), nullable=False)
  codigoPostal: str = db.Column(db.String(100), nullable=False)
  ciudad: str = db.Column(db.String(100), nullable=False)
  domicilio: str = db.Column(db.String(100), nullable=False)
  telefono: str = db.Column(db.String(100), nullable=False)
  contacto: str = db.Column(db.String(100), nullable=False)
  email: str = db.Column(db.String(100), nullable=False)

 
  universidad_id = db.Column(db.Integer, db.ForeignKey('universidades.id'))
  universidad = db.relationship("Universidad", back_populates="facultades") 

  especialidades = db.relationship("Especialidad", back_populates="facultad")


#def asociar_autoridad(self, autoridad):
#    if autoridad not in self.autoridades:
#        self.autoridades.append(autoridad)