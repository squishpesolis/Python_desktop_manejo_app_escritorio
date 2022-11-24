from src.domain.configuration_entity import ConfigurationEntity
from src.adapter.spi.db.programa_repository import ProgramaRepository
from src.adapter.spi.db.db_connection import DbConnection

class RepositoriesFactory:

    def __init__(self, db_connection: DbConnection) -> None:
        self.__repositories: dict = {
            "program_repository": ProgramaRepository(db_connection)
        }

    def get_repository(self, repository_name: str):
        if repository_name in self.__repositories:
            return self.__repositories[repository_name]
        else:
            raise Exception("Repositorio no existe")