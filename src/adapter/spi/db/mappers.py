from typing import Any
from src.application.mappers.db_mapper import DbMapper, DbModel
from src.domain.programa_entity import ProgramasEntity


class ProgramaDbMapper(DbMapper):

    def to_db(self, entity: ProgramasEntity) -> DbModel:
        raise Exception("not implemented")

    def to_entity(self, model: Any) -> ProgramasEntity:
        return ProgramasEntity(model[0], model[1])
