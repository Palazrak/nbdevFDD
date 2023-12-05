# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_tarea.ipynb.

# %% auto 0
__all__ = ['Tarea']

# %% ../nbs/01_tarea.ipynb 3
class Tarea:
    "Objeto que contiene un título, una descripción, un estado (completado o no completado)"
    def __init__(self,
                 titulo:str, # Titulo de la tarea
                 fecha_entrega:str, # Fecha de entrega en formato dd/mm/aaaa
                 descripcion:str='' # Informacion adicional sobre la tarea
                 ) -> None:
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_entrega = fecha_entrega
        self.completado = False
    
    def __str__(self) -> str:
        "Regresa la informacion completa sobre la tarea en formato String"
        return f"Tarea: {self.titulo}. \nDescripcion: {self.descripcion}. \nFecha de entrega: {self.fecha_entrega}. \nCompletada: {self.completado}"
    __repr__ = __str__
