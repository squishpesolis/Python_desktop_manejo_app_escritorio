from tkinter import ttk
from tkinter import *

from fastapi_injector import Injected
from injector import Injector, SingletonScope
from src.adapter.spi.db.programa_repository import ProgramaRepository

from src.infrastructure.gui.program_view import ProgramView
from src.domain.programa_entity import ProgramasEntity
from src.adapter.spi.repositories_factory import RepositoriesFactory
from src.application.repositories.programa_repository_abstract import ProgramaRepositoryAbstract
from src.application.usecases.obtener_todos_programas_usecase import ObtenerTodosLosProgramasUseCase


def iniciar_gui(injector: Injector):
    try:

        injector.get(RepositoriesFactory) is injector.get(RepositoriesFactory)
        factory = injector.get(RepositoriesFactory)

        program_repo: ProgramaRepositoryAbstract = factory.get_repository("program_repository")
        obtener_programas_usecase: ObtenerTodosLosProgramasUseCase = ObtenerTodosLosProgramasUseCase(program_repo)

        programas = obtener_programas_usecase.execute()

        window = Tk()
        application = ProgramView(window, programas)
        window.mainloop()

    except Exception as exception:
        raise Exception("Exepcion en Cargar la vista", exception)
