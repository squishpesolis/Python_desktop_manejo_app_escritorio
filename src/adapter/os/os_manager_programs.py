import subprocess
import typing

from AppOpener import run, give_appnames
from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess, Process

from src.application.os.os_programs_interface import OSProgramInterface


class OSManagerProgram(OSProgramInterface):

    def __init__(self) -> None:
        pass

    def get_list_app_installed(self):
        apps = give_appnames()
        return apps

    def check_if_app_exist(self, program_name: str) -> bool:
        exist: bool = False
        dict_app = self.get_list_app_installed()
        if program_name in dict_app:
            exist = True

        return exist

    def open_program(self, program_name: str):
        run(program_name)

    def run_comman_power_shell_windows(self, cmd):
        completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
        return completed

    def get_list_proccess_running(self):

        try:
            return process_iter()
        except (AccessDenied, ZombieProcess) as error:
            raise Exception("Error al obtener los procesos", error)

    def get_process_running_by_name(self, name_program_running: str) -> typing.List[Process]:

        process_running = self.get_list_proccess_running()
        list_programs: typing.List[Process] = []

        for resul in process_running:
            name_process: str = resul.name()
            name_process = name_process.lower()
            name_process_split = name_process.split(".")
            split_name = name_process_split[0]

            name_program_running = name_program_running.lower()

            if split_name == name_program_running:
                list_programs.append(resul)

        return list_programs

    def kill_process_programs_windows(self, list_programs: typing.List[Process]):

        if len(list_programs) > 0:
            for result in list_programs:
                pdi = str(result.pid)
                command_kill_ps = "Stop-Process -ID pdi -Force".replace("pdi", pdi)
                exist_process_will_kill = self.validate_if_process_exist_after_delete_other_proccess_windows(pdi)
                if exist_process_will_kill:
                    self.run_comman_power_shell_windows(command_kill_ps)

    def validate_if_process_exist_after_delete_other_proccess_windows(self, pdi) -> bool:
        exist_process = False
        command = "get-process -ID <PID> | select-object id".replace("<PID>", str(pdi))
        response_ps = self.run_comman_power_shell_windows(command)
        if response_ps.returncode == 0:
            exist_process = True

        return exist_process
