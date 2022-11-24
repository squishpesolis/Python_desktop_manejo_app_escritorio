
import sqlite3
from src.application.spi.db_interface import DbInterface
from src.domain.api_excepion import ApiException
from src.domain.configuration_entity import ConfigurationEntity

class DbConnection(DbInterface):
    def __init__(self, config: ConfigurationEntity) -> None:
        try:
            self.connection(config)
            print("---------------------->CONEXION DB EXITOSA<--------------------", config.env)
            if config.env != "test":
                self.migration()
        except Exception as error:
            raise ApiException(
                "error initializing connection to DB: {}".format(str(error))) from error

    def connection(self, config: ConfigurationEntity) -> None:
        self.con = sqlite3.connect(config.config_data_base_programas.db_name + ".sqlite3", check_same_thread=False)
        self.cur = self.con.cursor()

    def migration(self):
        try:
            self.cur.execute("DROP TABLE IF EXISTS programas")
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS programas (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT,nombre_programa TEXT, nombre_proceso)")
            self.cur.execute(
                "INSERT INTO programas (nombre, nombre_programa, nombre_proceso) VALUES ('Zoom', 'Zoom','Zoom'), ('Teams','Microsoft Teams','Teams'), ('Skype','Skype','Skype')")
            self.con.commit()
        except Exception as error:
            raise ApiException("error running migration to DB: {}".format(str(error))) from error