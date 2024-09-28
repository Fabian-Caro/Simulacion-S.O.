class Recurso:
    def __init__(self, id_recurso, nombre_recurso, disponibilidad_recurso):
        self.__id_recurso = id_recurso
        self.__nombre_recurso = nombre_recurso
        self.__disponibilidad_recurso = disponibilidad_recurso
        
    def get_id_recurso(self):
        return self.__id_recurso
        
    def get_nombre_recurso(self):
        return self.__nombre_recurso
        
    def is_disponibilidad_recurso(self):
        return self.__disponibilidad_recurso
    
    def set_disponibilidad_recurso(self, disponibilidad_recurso):
        if isinstance(disponibilidad_recurso, bool):
            self.__disponibilidad_recurso = disponibilidad_recurso
        else:
            raise ValueError("disponibilidad debe ser  debe ser un valor booleano.")
        
    def mostrar_info(self):
        return (
            f"ID: {self.__id_recurso}, Nombre: {self.__nombre_recurso}, Prioridad: {self.__disponibilidad_recurso}")
    
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
# ]

# def imprimir_recursos(recursos):
#     for recurso in recursos:
#         print(recurso.mostrar_info())


# imprimir_recursos(recursos)