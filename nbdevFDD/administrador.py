# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_administrador.ipynb.

# %% auto 0
__all__ = ['Administrador']

# %% ../nbs/02_administrador.ipynb 3
class Administrador:
    "El administrador se inicializa con una lista vacía que se llenará manualmente con tareas"
    def __init__(self) -> None:
        self.lista_tareas = []
    
    def agrega_tarea (self,
                      titulo:str, #Título de la tarea
                      fecha_entrega:str, #Fecha de entrega en formato dd/mm/aaaa. De no estar en este formato, el método no funcionará
                      descripcion:str='' #Información adicional sobre la tarea
                      ) -> bool: #Regresa True si la tarea se agregó exitosamente, False en caso contrario
        "Crea un objeto tipo Tarea, lo agrega a la lista interna y ordena con base en la fecha de entrega"
        tarea = Tarea(titulo=titulo, fecha_entrega=fecha_entrega, descripcion=descripcion)
        self.lista_tareas.append(tarea)
        self.lista_tareas = sorted(self.lista_tareas, key=lambda x: datetime.strptime(x.fecha_entrega, "%d/%m/%Y"))
        
    def imprime_completo (self) -> str:
        "Imprime todas las tareas contenidas en la lista, tanto las completadas como las faltantes"
        for tarea in self.lista_tareas:
            print(tarea)
    
    def imprime_faltantes(self) ->str:
        "Imprime las tareas en la lista que su atributo 'completado' esté en False"
        for tarea in self.lista_tareas:
            if tarea.completado == False:
                print(tarea)
    
    __repr__ = imprime_completo
    
    def tarea_completada(self,
                         titulo:str # Título de la tarea que se busca
                         ) -> bool: # Regresa True si la tarea estaa en la lista y la marcó como completada
        "Busca una tarea por su nombre y cambia su atributo 'completado' a True"
        for tarea in self.lista_tareas:
            if tarea.titulo == titulo:
                tarea.completado = True
                return True
        return False