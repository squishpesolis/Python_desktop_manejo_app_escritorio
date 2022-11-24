import typing

from src.application.repositories.programa_repository_abstract import ProgramaRepositoryAbstract
from src.domain.programa_entity import ProgramasEntity
from src.adapter.spi.db.mappers import ProgramaDbMapper
from src.adapter.spi.db.db_connection import DbConnection
from src.domain.api_excepion import ApiException

class ProgramaRepository(ProgramaRepositoryAbstract):

    def __init__(self, db_connection: DbConnection) -> None:
        self.mapper = ProgramaDbMapper()
        self.db_connection = db_connection
        

    def obtener_programas(self) -> typing.List[ProgramasEntity]:
        # Se puede llamar a la base de datos
        
        list_programas: typing.List[ProgramasEntity] = []
        """ p1 = ProgramasEntity(1, "Zoom")
        p2 = ProgramasEntity(2, "Skype")
        p3 = ProgramasEntity(3, "Teams")
        list_programas.append( p1 )
        list_programas.append( p2 )
        list_programas.append(p3 ) """

        self.db_connection.cur.execute("select * from programas")
        res = self.db_connection.cur.fetchall()
        if not res:
            raise ApiException("No se pudo obteners los programas")
        for data in res:
            list_programas.append(data)

        return list_programas
