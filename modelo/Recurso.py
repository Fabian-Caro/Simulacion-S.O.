from modelo.Procesos import Procesos

class Recurso:
    def __init__(self, id_recurso, nombre_recurso, proceso):
        self.__id_recurso = id_recurso
        self.__nombre_recurso = nombre_recurso
        self.__proceso = proceso
        
    def get_id_recurso(self):
        return self.__id_recurso
        
    def get_nombre_recurso(self):
        return self.__nombre_recurso
        
<<<<<<< HEAD
    def get_disponibilidad_recurso(self):
        return self.__disponibilidad_recurso
    
    def set_disponibilidad_recurso(self, disponibilidad_recurso):
        #if isinstance(disponibilidad_recurso, bool):
            self.__disponibilidad_recurso = disponibilidad_recurso
        # else:
        #     raise ValueError("disponibilidad debe ser  debe ser un valor entero.")
        
    def mostrar_info(self):
        return (
            f"ID: {self.__id_recurso}, Nombre: {self.__nombre_recurso}, Disponibilidad: {self.__disponibilidad_recurso}")
    
# recursos = [
#     Recurso("001", "Disco duro", None),
#     Recurso("002", "Tarjeta gráfica", None),
#     Recurso("003", "Impresora", None),
#     Recurso("004", "Archivos", None),
#     Recurso("005", "Red", None),
#     Recurso("006", "Teclado", None),
#     Recurso("007", "Ratón", None),
#     Recurso("008", "Pantalla", None),
#     Recurso("009", "Parlante", None)
=======
    def get_proceso(self):
        return self.__proceso
    
    def set_proceso(self, proceso):
        self.__proceso= proceso
        # if isinstance(proceso, Procesos):
        #     self.__proceso= proceso
        # else:
        #     raise ValueError("Ingrese dato valido.")
        
    def mostrar_info(self):
        return (
            f"ID: {self.__id_recurso}, Nombre: {self.__nombre_recurso}, Prioridad: {self.__proceso.get_nombre_proceso()}")
    
# recursos = [
#     Recurso("001", "Disco duro", True),
#     Recurso("002", "Tarjeta gráfica", True),
#     Recurso("003", "Impresora", True),
#     Recurso("004", "Archivos", True),
#     Recurso("005", "Red", True),
#     Recurso("006", "Teclado", True),
#     Recurso("007", "Ratón", True),
#     Recurso("008", "Pantalla", True),
#     Recurso("009", "Parlante", True)
>>>>>>> main
# ]

# def imprimir_recursos(recursos):
#     for recurso in recursos:
#         print(recurso.mostrar_info())


# imprimir_recursos(recursos)