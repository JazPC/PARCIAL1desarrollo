from app.models import CategoriaCargo
from app.repositories import CategoriaCargoRepository

class CategoriaCargoService:
    @staticmethod
    def crear(categoria_cargo: CategoriaCargo) -> CategoriaCargo:
        return CategoriaCargoRepository.crear(categoria_cargo)

    @staticmethod
    def buscar_por_id(id: int) -> CategoriaCargo | None:
        return CategoriaCargoRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[CategoriaCargo]:
        return CategoriaCargoRepository.buscar_todos()

    @staticmethod
    def actualizar(id: int, categoria_cargo: CategoriaCargo) -> CategoriaCargo | None:
        categoria_existente = CategoriaCargoRepository.buscar_por_id(id)
        if not categoria_existente:
            return None
        categoria_existente.nombre = categoria_cargo.nombre
        return CategoriaCargoRepository.guardar(categoria_existente)