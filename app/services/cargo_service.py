from app.models import Cargo
from app.repositories import CargoRepository

class CargoService:
    
    @staticmethod
    def crear(cargo: Cargo) -> Cargo:
        return CargoRepository.crear(cargo)
    
    @staticmethod
    def buscar_por_id(id: int) -> Cargo | None:
        return CargoRepository.buscar_por_id(id)  
    
    @staticmethod
    def buscar_todos() -> list[Cargo]:
        return CargoRepository.buscar_todos()
    
    @staticmethod
    def actualizar(id: int, cargo: Cargo) -> Cargo | None:
        cargo_existente = CargoRepository.buscar_por_id(id)
        if not cargo_existente:
            return None
        cargo_existente.nombre = cargo.nombre
        cargo_existente.puntos = cargo.puntos
        cargo_existente.categoria_cargo_id = cargo.categoria_cargo_id
    
        return CargoRepository.guardar(cargo_existente)