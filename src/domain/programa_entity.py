from src.domain.base_entity import BaseEntity


class ProgramasEntity(BaseEntity):
    def __init__(self, id: int, nombre: str, nombre_programa: str) -> None:
        super().__init__()
        self.id = id
        self.nombre = nombre
        self.nombre_programa = nombre_programa
        