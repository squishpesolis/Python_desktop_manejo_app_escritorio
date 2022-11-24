import tkinter as tk
import tkinter.ttk as ttk


font_family_title = "Helvetica"

size_font_btn= 12
size_font_btn_medium = 7

color_windows = "red"
color_frame_contenedor = "white"
color_btn_warning ="red"
color_text_button = "white"
color_text_button_warning = "red"

width_frame_btn = 55
height_frame_btn = 40


def GetColorPrograma(programa:str):
    color = "#000000"
    colores = {
        "zoom" : '#2D8CFF',
        "skype" : '#00aff0',
        "teams" : '#464EB8',
       
    }

    if programa not in colores.keys():
        return color
    
    return colores.get(programa)
   


def CustomStyle():
    style = ttk.Style()

    style.configure("F-LEFT.TFrame",background=color_frame_contenedor)

    return style 
