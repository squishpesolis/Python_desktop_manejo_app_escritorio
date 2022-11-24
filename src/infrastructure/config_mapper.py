from typing import Dict, Optional
from dotenv import dotenv_values, load_dotenv
from src.domain.configuration_data_base import ConfigurationDataBase
from src.domain.configuration_entity import ConfigurationEntity
import json
import os
from pathlib import Path
class ConfigurationMapper:
    def __init__(self, env: str) -> None:

        env = env.lower()

        src_path = Path(__file__).parent.parent
        path_root = src_path.parent
        name_env = ".env." + env

        path_env = os.path.join(path_root,name_env)

        load_dotenv(dotenv_path=path_env)

        #__config_raw: Dict[str, Optional[str]] = dotenv_values(".env.{}".format(env))

        config_data_base_programas = ConfigurationDataBase(os.getenv("DATA_BASE_SERVER_NAME"),
                                                os.getenv("DATA_BASE_NAME"),
                                                os.getenv("DATABASE_USER"),
                                                os.getenv("DATABASE_PASSWORD"),
                                                env                                              
                                                )

       

        if config_data_base_programas.db_server_name is None or config_data_base_programas.db_name is None or config_data_base_programas.db_user is None or config_data_base_programas.db_password is None:
            raise Exception("Erro al cargar el archivo de configuración: ", os.getcwd(), os.getenv("DATA_BASE_SERVER_NAME"), json.dumps(config_data_base_programas.__dict__))

        self.config = ConfigurationEntity(config_data_base_programas, env)

    def get_config(self) -> ConfigurationEntity:
        return self.config
