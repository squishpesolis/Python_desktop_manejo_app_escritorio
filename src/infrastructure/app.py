import os
from injector import Injector, SingletonScope

from src.domain.configuration_entity import ConfigurationEntity
from src.infrastructure.config_mapper import ConfigurationMapper
from src.adapter.spi.db.db_connection import DbConnection
from src.adapter.spi.repositories_factory import RepositoriesFactory

config: ConfigurationEntity = ConfigurationMapper(os.getenv("ENV", "dev")).get_config()
db_connection: DbConnection = DbConnection(config)
repositories_factory = RepositoriesFactory(db_connection)

def create_app(injector: Injector):

    injector.binder.bind(RepositoriesFactory, to=repositories_factory, scope=SingletonScope)
    

