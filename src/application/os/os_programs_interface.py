from abc import ABC, abstractmethod



class OSProgramInterface(ABC):

    @abstractmethod
    def check_if_app_exist(self, program_name: str):
        """Comprueba si esta instalado un programa"""

    @abstractmethod
    def open_program(self, program_name: str):
        """Comprueba si esta instalado un programa"""



