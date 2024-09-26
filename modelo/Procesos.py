from modelo.Recurso import Recurso

class Procesos:
    def __init__(self, id_proceso, nombre, tamano, prioridad, recursos):
        self.__id_proceso = id_proceso
        self.__nombre = nombre
        self.__tamano = tamano
        self.__prioridad = prioridad
        self.__recursos = recursos
        
    def get_id_proceso(self):
        return self.__id_proceso
    
    def set_id(self, id_proceso):
        if isinstance(id_proceso, str):
            self.__id_proceso = id_proceso
        else:
            raise ValueError("ID debe ser una cadena de texto.")
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            raise ValueError("nombre debe ser una cadena de texto.")
        
    def get_tamano(self):
        return self.__tamano
    
    def set_tamano(self, tamano):
        if isinstance(tamano, (int, float)):
            if tamano >= 0:
                self.__tamano = tamano
            else:
                self.__tamano = 0
        else:
            raise ValueError("Tamaño debe ser un número.")
    
    def is_prioridad(self):
        return self.__prioridad
    
    def set_prioridad(self, prioridad):
        if isinstance(prioridad, bool):
            self.__prioridad = prioridad
        else:
            raise ValueError("Prioridad debe ser un valor booleano.")
        
    def get_recursos(self):
        return self.__recursos
    
    def set_recursos(self, recursos):
        if isinstance(recursos, list) and all(isinstance(r, bool) for r in recursos):
            self.__recursos = recursos
        else:
            raise ValueError("Recursos debe ser una lista de enteros")
        
    def get_nombre_recursos(self):
        return [recurso.get_nombre_recurso() for recurso in self.__recursos]
    
    def mostrar_info(self):
        recursos_nombres = ', '.join(recurso.get_nombre_recurso() for recurso in self.__recursos)
        return (
            f"ID: {self.__id_proceso}, Nombre: {self.__nombre}, Tamaño: {self.__tamano}, "
            f"Prioridad: {self.__prioridad}, Recursos: {recursos_nombres}"
            )
    
    # recursos = [
    # Recurso("001", "Disco duro", None),
    # Recurso("002", "Tarjeta gráfica", None),
    # Recurso("003", "Impresora", None),
    # Recurso("004", "Archivos", None),
    # Recurso("005", "Red", None),
    # Recurso("006", "Teclado", None),
    # Recurso("007", "Ratón", None),
    # Recurso("008", "Pantalla", None),
    # Recurso("009", "Parlante", None)
    # ]