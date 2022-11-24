import typing

from src.application.repositories.programa_repository_abstract import ProgramaRepositoryAbstract
from src.application.usecases.interfaces import UseCaseMultipleEntities
from src.application.utils.error_handling_utils import ErrorHandlingUtils
from src.domain.programa_entity import ProgramasEntity

import traceback

class ObtenerTodosLosProgramasUseCase(UseCaseMultipleEntities):
    
    def __init__(self, repository: ProgramaRepositoryAbstract) -> None:
        self.repository = repository
        
    def execute(self) -> typing.Iterable[ProgramasEntity]:
        try:
            
            return self.repository.obtener_programas()
        except Exception as exception:
            raise ErrorHandlingUtils.application_error("Error: No se pudo obtener los programas", exception)    