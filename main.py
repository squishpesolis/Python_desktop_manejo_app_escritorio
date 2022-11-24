from injector import Injector
from src.infrastructure.app import create_app
from src.infrastructure.gui.main_view import iniciar_gui

if __name__ == "__main__":
    injector = Injector()
    create_app(injector)
    iniciar_gui(injector)