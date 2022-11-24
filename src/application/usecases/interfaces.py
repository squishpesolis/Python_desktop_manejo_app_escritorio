from abc import ABC, abstractmethod
from typing import Generic, Iterable, TypeVar
from src.domain.base_entity import BaseEntity

Entity = TypeVar("Entity")

class GenericUseCase(ABC, Generic[Entity]):
    @abstractmethod
    def execute(self) -> Entity:
        """Ejecutar un caso de uso y devolver un tipo genérico"""

class UseCaseOneEntity(GenericUseCase):
    @abstractmethod
    def execute(self) -> BaseEntity:
        """Ejecutar un caso de uso y devolver un objeto de entidad"""

class UseCaseMultipleEntities(GenericUseCase):
    @abstractmethod
    def execute(self) -> Iterable[BaseEntity]:
        """Ejecutar un caso de uso y devolver múltiples objetos de entidad"""