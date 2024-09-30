# from modelo.Recurso import Recurso
import random

class Procesos:
    def __init__(self, id_proceso, nombre_proceso, tamano_proceso, prioridad_proceso, recursos_asignados, recursos_necesarios):
        self.__id_proceso = id_proceso
        self.__nombre_proceso = nombre_proceso
        self.__tamano_proceso = tamano_proceso
        self.__prioridad_proceso = prioridad_proceso
        self.__recursos_asignados = recursos_asignados
        self.__recursos_necesarios = recursos_necesarios
        
    def get_id_proceso(self):
        return self.__id_proceso
    
    def set_id_proceso(self, id_proceso):
        if isinstance(id_proceso, str):
            self.__id_proceso = id_proceso
        else:
            raise ValueError("ID_proceso debe ser una cadena de texto.")
        
    def get_nombre_proceso(self):
        return self.__nombre_proceso
    
    def set_nombre_proceso(self, nombre_proceso):
        if isinstance(nombre_proceso, str):
            self.__nombre_proceso = nombre_proceso
        else:
            raise ValueError("nombre_proceso debe ser una cadena de texto.")
        
    def get_tamano_proceso(self):
        return self.__tamano_proceso
    
    def set_tamano_proceso(self, tamano_proceso):
        if isinstance(tamano_proceso, (int, float)):
            if tamano_proceso >= 0:
                self.__tamano_proceso = tamano_proceso
            else:
                self.__tamano_proceso = 0
        else:
            raise ValueError("Tamaño_proceso debe ser un número.")
    
    def is_prioridad_proceso(self):
        return self.__prioridad_proceso
    
    def set_prioridad_proceso(self, prioridad_proceso):
        if isinstance(prioridad_proceso, bool):
            self.__prioridad_proceso = prioridad_proceso
        else:
            raise ValueError("Prioridad_proceso debe ser un valor booleano.")
        
    def get_recursos_asignados(self):
        return self.__recursos_asignados
    
<<<<<<< HEAD
    def set_recursos(self, recursos):
        if isinstance(recursos, list) and all(isinstance(r, bool) for r in recursos):
            self.__recursos = recursos
        else:
            raise ValueError("Recursos debe ser una lista de enteros")
=======
    def set_recursos_asignados(self, recursos_asignados):
        self.__recursos_asignados = recursos_asignados
        # if isinstance(recursos_asignados, list) and all(isinstance(r, bool) for r in recursos_asignados):
        #     self.__recursos_asignados = recursos_asignados
        # else:
        #     raise ValueError("recursos_asignados debe ser una lista de booleanos")
>>>>>>> main
        
    def get_nombre_recursos(self):
        return [recurso.get_nombre_recurso() for recurso in self.__recursos_asignados]
    
    def get_recursos_necesarios(self):
        return self.__recursos_necesarios
    
<<<<<<< HEAD
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
=======
    def set_recursos_necesarios(self, recursos_necesarios):
        self.__recursos_necesarios = recursos_necesarios
        # if isinstance(recursos_necesarios, list) and all(isinstance(r, bool) for r in recursos_necesarios):
        #     self.__recursos_necesarios = recursos_necesarios
            
    def tiene_todos_los_recursos(self):
        return len(self.__recursos_necesarios) == len(self.__recursos_asignados)
    
    def liberar_recursos(self):
        recursos_libres = []
        for recurso in self.__recursos_necesarios:
            if random.random() < 0.5:
                recurso.set_proceso(None)
                recursos_libres.append(recurso)
            else:
                recurso.set_proceso(self)
        self.__recursos_asignados = [r for r in self.__recursos_necesarios if r not in recursos_libres]
        self.__recursos_necesarios = [r for r in self.__recursos_necesarios if r not in recursos_libres]
        return recursos_libres
    
    def no_pasa_a_bloqueados(self):
        r_disponible = True
        recursos_no_disponibles = []
        for r in self.__recursos_necesarios:
            if r.get_proceso() != self and r.get_proceso() != None:
                r_disponible = False
                recursos_no_disponibles.append(int(r.get_id_recurso()))
        return r_disponible,recursos_no_disponibles
    
    def terminar_ejecucion(self):
        for recurso in self.__recursos_necesarios:
            recurso.set_proceso(None)

    # def mostrar_info(self):
    #     recursos_nombres = ', '.join(recurso.get_nombre_recurso() for recurso in self.__recursos)
    #     return (
    #         f"ID: {self.__id_proceso}, Nombre: {self.__nombre}, Tamaño: {self.__tamano}, "
    #         f"Prioridad: {self.__prioridad}, Recursos: {recursos_nombres}"
    #         )
    
    # recursos = [
    # Recurso("001", "Disco duro", True),
    # Recurso("002", "Tarjeta gráfica", True),
    # Recurso("003", "Impresora", True),
    # Recurso("004", "Archivos", True),
    # Recurso("005", "Red", True),
    # Recurso("006", "Teclado", True),
    # Recurso("007", "Ratón", True),
    # Recurso("008", "Pantalla", True),
    # Recurso("009", "Parlante", True)
>>>>>>> main
    # ]