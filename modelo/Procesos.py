class Procesos:
    def __init__(self, id, nombre, tamano, prioridad, recursos):
        self.__id = id
        self.__nombre = nombre
        self.__tamano = tamano
        self.__prioridad = prioridad
        self.__recursos = recursos
        
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        if isinstance(id, str):
            self.__id = id
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
            self.__tamano = tamano
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
            raise ValueError("Recursos debe ser una lista de booleanos")
        
    def mostrar_info(self):
        return (
            f"ID: {self.__id}, Nombre: {self.__nombre}, Tamaño: {self.__tamano}, "
            f"Prioridad: {self.__prioridad}, "
            f"Recursos: {', '.join(self.__recursos)}"
            )