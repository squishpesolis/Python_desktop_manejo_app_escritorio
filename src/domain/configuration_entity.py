from src.domain.configuration_data_base import ConfigurationDataBase
class ConfigurationEntity:
    def __init__(self, config_data_base_programas: ConfigurationDataBase,env: str) -> None:
        self.config_data_base_programas = config_data_base_programas
        self.env = env