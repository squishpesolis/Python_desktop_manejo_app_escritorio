import typing
from tkinter import Button, messagebox
import tkinter as tk

from typing import List
from src.domain.programa_entity import ProgramasEntity
from src.infrastructure.gui.custom_styles import *

from src.adapter.os.os_manager_programs import OSManagerProgram
from psutil import Process
from tktooltip import ToolTip

class ProgramView:
    def __init__(self, windows, programas: List[ProgramasEntity]) -> None:

        self.wind = windows
        style = ttk.Style(self.wind)
        style.configure = CustomStyle()

        # para que la aplicación siempre se mantenga en primer plano
        self.wind.attributes("-topmost", True)

        self.wind['bg'] = color_windows

        self.wind.resizable(False, False)
        self.wind.overrideredirect(True)

        height_of_the_screen = self.wind.winfo_screenheight()  # height of the screen

        frame_main = ttk.Frame(self.wind, style="F-LEFT.TFrame")
        frame_main.pack(side="left", expand=1, fill="both")

        # Cuanto maximiza desde la barra de tareas
        frame_main.bind("<Map>", self.frame_main_mapped_maximize)

        row_position_frame_name = 0

        self.create_minimize_and_close_button(frame_main, row_position_frame_name)
        row_position_frame_name += 1

        self.create_floating_window(frame_main, row_position_frame_name)
        row_position_frame_name += 1

        # self.create_list_programs_buttons(frame_main, programas, row_position_frame_name)

        for program in programas:
            nombre_mostrar = str(program[1])
            nombre = str(program[2])
            background_programa = GetColorPrograma(nombre_mostrar.lower())
            row_position_frame_name = row_position_frame_name + 1
            frame_container_btn = ttk.Frame(frame_main, width=width_frame_btn, height=height_frame_btn)

            btn = Button(frame_container_btn, text=str(nombre_mostrar), background=background_programa,
                         foreground=color_text_button, command=lambda nombre=nombre: self.abrirPrograma(nombre.lower())
                         )
            btn.pack()
            frame_container_btn.rowconfigure(0, weight=1)
            frame_container_btn.columnconfigure(0, weight=1)
            frame_container_btn.grid_propagate(0)
            frame_container_btn.grid(row=row_position_frame_name, column=0, pady=(5, 5), padx=(1, 1))
            btn.grid(sticky="NWSE")

        # Reset

        row_position_frame_name = row_position_frame_name + 1
        self.create_reset_button(frame_main, row_position_frame_name, programas)

        self.wind.geometry('%dx%d+%d+%d' % (
        width_frame_btn, ((row_position_frame_name * height_frame_btn) + height_frame_btn), 0,
        (height_of_the_screen * 0.50)))

    def create_reset_button(self, frame_left, row, programas: List[ProgramasEntity]):
        frame_container_btn_reset = ttk.Frame(frame_left, width=width_frame_btn, height=(height_frame_btn / 2))
        btn = Button(frame_container_btn_reset, text=str("RESET"), background=color_btn_warning,
                     foreground=color_text_button, command=lambda: self.close_applications(programas))
        btn.pack()
        frame_container_btn_reset.rowconfigure(0, weight=1)
        frame_container_btn_reset.columnconfigure(0, weight=1)
        frame_container_btn_reset.grid_propagate(0)

        frame_container_btn_reset.grid(row=row, column=0, pady=(10, 0))
        btn.grid(sticky="NWSE")

    def create_minimize_and_close_button(self, frame_left, row):

        frame = ttk.Frame(frame_left, width=20, height=20)

        minimize_btn = Button(frame, text=str("—"), background="gray",
                              foreground=color_text_button)

        close_btn = Button(frame, text=str(" X "), background="gray",
                           foreground=color_text_button, command=self.wind.destroy)

        minimize_btn.columnconfigure(0, weight=1)
        close_btn.columnconfigure(1, weight=1)

        minimize_btn.grid(row=0, column=0, sticky=tk.W + tk.E)
        close_btn.grid(row=0, column=1, sticky=tk.W + tk.E)

        frame.grid(row=row, column=0, pady=(1, 10))

        minimize_btn.bind("<Button-1>", self.minimize_windows)

    def create_floating_window(self, frame_left, row):

        frame_floating_windows = ttk.Frame(frame_left, width=20, height=20)
        frame_floating_windows.rowconfigure(0, weight=1)
        frame_floating_windows.columnconfigure(0, weight=1)
        frame_floating_windows.grid_propagate(0)
        frame_floating_windows.grid(row=row, column=0, pady=(1, 10))

        self.grip = tk.Label(frame_floating_windows, bitmap="gray75", cursor="diamond_cross")
        self.grip.pack(side="left", fill="y")
        ToolTip(self.grip, msg="MOVER", delay=0,
        parent_kwargs={"bg": "black", "padx": 15, "pady": 1},
        fg="#ffffff", bg="#1c1c1c", padx=10, pady=10)

        self.grip.grid(sticky="NWSE")

        self.grip.bind("<ButtonPress-1>", self.start_move_windows)
        self.grip.bind("<ButtonRelease-1>", self.stop_move_windows)
        self.grip.bind("<B1-Motion>", self.do_move_windows)

    def start_move_windows(self, event):
        self.wind.x = event.x
        self.wind.y = event.y

    def stop_move_windows(self, event):
        self.wind.x = None
        self.wind.y = None

    def do_move_windows(self, event):
        deltax = event.x - self.wind.x
        deltay = event.y - self.wind.y
        x = self.wind.winfo_x() + deltax
        y = self.wind.winfo_y() + deltay
        self.wind.geometry(f"+{x}+{y}")
        # self.wind.resizable(False, False)

    def abrirPrograma(self, programa: str):

        os_program = OSManagerProgram()
        exist_program = os_program.check_if_app_exist(programa)

        if not exist_program:
            messagebox.showwarning(message="! " + programa.capitalize() + " no instalado", title="Aplicación")

        os_program.open_program(programa)

    def close_applications(self, programs: List[ProgramasEntity]):
        os_program = OSManagerProgram()

        for program in programs:
            name_processing = str(program[3])

            list_programs: typing.List[Process] = os_program.get_process_running_by_name(name_processing)
            os_program.kill_process_programs_windows(list_programs)
            print("Ok Close")

    def minimize_windows(self, event):
        self.wind.update_idletasks()
        self.wind.overrideredirect(False)
        # root.state('withdrawn')
        self.wind.state('iconic')

    def frame_main_mapped_maximize(self, e):
        self.wind.update_idletasks()
        self.wind.overrideredirect(True)
        self.wind.state('normal')
