import random

class Memoria:
    def __init__(self):
        self.memoria = [[] for _ in range(10)]
        
    def obtener_memoria(self):
        return self.memoria
    
    def agregar_proceso(self, nuevo_proceso):
        print("Estado de la memoria antes de agregar:", self.memoria)
        for fila in self.memoria:
            if len(fila) < 10:
                fila.append(nuevo_proceso)  # Agregamos el id o atributo que necesites
                print("Proceso agregado a la memoria:", nuevo_proceso)
                return True
        return False
    
    def agregar_proceso_aleatorio(self, proceso):
        while True:
            fila = random.randint(0, 9)  # Genera un número aleatorio entre 0 y 9
            columna = random.randint(0, 9)  # Genera un número aleatorio entre 0 y 9
            
            if self.memoria[fila][columna] is None:  # Verifica si la celda está vacía
                self.memoria[fila][columna] = proceso  # Agrega el proceso en la posición elegida
                print(f"Proceso {proceso} agregado en la posición ({fila}, {columna}).")
                break  # Salir del bucle una vez que se ha agregado el proceso
            else:
                print(f"Posición ({fila}, {columna}) ocupada. Buscando otra posición...")