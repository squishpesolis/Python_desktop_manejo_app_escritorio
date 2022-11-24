from unittest.mock import MagicMock
import unittest
from src.adapter.spi.db.programa_repository import ProgramaRepository
from src.application.usecases.obtener_todos_programas_usecase import ObtenerTodosLosProgramasUseCase
from src.domain.api_excepion import ApiException
from src.domain.programa_entity import ProgramasEntity

class ObtenerTodosLosProgramasUseCaseTest(unittest.TestCase):

    def test_debe_devolver_un_mensaje_genérico_cuando_se_produce_una_excepción_de_repositorio_inesperada(self):
        # obtenemos todos los programas, el usecase repo con una excepción inesperada
        mensaje_randon_exception = "random exception"
        programa_repository = ProgramaRepository()
        
        programa_repository.obtener_programas = MagicMock(side_effect=Exception(mensaje_randon_exception))

        
        todos_los_programas_usecase: ObtenerTodosLosProgramasUseCase = ObtenerTodosLosProgramasUseCase(programa_repository)

        # Luego  Excepción

        with self.assertRaises(ApiException) as context:
            
            todos_los_programas_usecase.execute()
        self.assertEqual("Error: No se pudo obtener los programas", str(context.exception.message))

    def test_debe_devolver_un_mensaje_customizado_cuando_se_produce_una_excepción_inesperada_en_el_repositorio(self):
        
        mensaje_exep_custom = "exception in repositorio"

        programa_repository = ProgramaRepository()
        programa_repository.obtener_programas = MagicMock(side_effect=ApiException(mensaje_exep_custom))

        todos_los_programas_usecase: ObtenerTodosLosProgramasUseCase = ObtenerTodosLosProgramasUseCase(programa_repository)

        # Luego  Excepción

        with self.assertRaises(ApiException) as context:
            
            todos_los_programas_usecase.execute()
        self.assertEqual(mensaje_exep_custom, str(context.exception.message))

    def test_debe_retornar_una_lista_vacia(self):
        programa_repository = ProgramaRepository()
        programa_repository.obtener_programas = MagicMock(return_value=[])

        obtener_programas_usecase: ObtenerTodosLosProgramasUseCase = ObtenerTodosLosProgramasUseCase(programa_repository)
        data = obtener_programas_usecase.execute()

        # then assert the result is an empty list
        self.assertEqual(len(data), 0)

    def test_debe_retornar_una_lista(self):
        
        programa_repository = ProgramaRepository()
        programa_repository.obtener_programas = MagicMock(return_value=[ProgramasEntity(1, "Zoom","Zoom"), ProgramasEntity(2,"Teams","Teams")])

        
        obtener_programas_usecase: ObtenerTodosLosProgramasUseCase = ObtenerTodosLosProgramasUseCase(programa_repository)
        data = obtener_programas_usecase.execute()

        
        self.assertEqual(len(data), 2)