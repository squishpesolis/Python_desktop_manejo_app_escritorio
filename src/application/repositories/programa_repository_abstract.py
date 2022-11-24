from abc import ABC, abstractmethod
import typing

from src.domain.programa_entity import ProgramasEntity

class ProgramaRepositoryAbstract(ABC):

   
    @abstractmethod
    def obtener_programas(self) -> typing.List[ProgramasEntity]:
        pass

        