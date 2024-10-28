import random

class Memoria:
    def __init__(self):
        self.memoria_principal = [["" for _ in range(5)] for _ in range(5)]
        self.memoria_virtual = [["" for _ in range(10)] for _ in range(10)]
        self.inicializar_memoria()
        
    def inicializar_memoria(self):
        self.memoria_principal[0][0] = "SO"
        self.memoria_principal[0][1] = "SO"
        self.memoria_principal[1][0] = "SO"
        self.memoria_principal[1][1] = "SO"
        
    def obtener_memoria_principal(self):
        return self.memoria_principal
    
    def obtener_memoria_virtual(self):
        return self.memoria_virtual
    
    def agregar_proceso(self, nuevo_proceso):
        print("Estado de la memoria antes de agregar:", self.memoria_principal)
        for fila in self.memoria_principal:
            if "" in fila:
                index = fila.index("")
                fila[index] = nuevo_proceso
                print("Proceso agregado a la memoria principal:", nuevo_proceso)
                break
            
        for fila in self.memoria_virtual:
            if len(fila) < 10:
                fila.append(nuevo_proceso)
                print("Proceso agregado a la memoria virtual: ", nuevo_proceso)
                return True
        return False
    
    def limpiar_memoria(self, proceso):
        print("Estado de la memoria antes de limpiarla:")
        print("Memoria principal:", self.memoria_principal)
        print("Memoria virtual:", self.memoria_virtual)
        
        for i in range(len(self.memoria_principal)):
            for j in range(len(self.memoria_principal[i])):
                if self.memoria_principal[i][j] == proceso:
                    self.memoria_principal[i][j] = ""  # Restablece a cadena vacía si coincide con el proceso
                    
        for i in range(len(self.memoria_virtual)):
            for j in range(len(self.memoria_virtual[i])):
                if self.memoria_virtual[i][j] == proceso:
                    self.memoria_virtual[i][j] = ""
    
        print("Estado de la memoria después de limpiarla:")
        print("Memoria principal:", self.memoria_principal)
        print("Memoria virtual:", self.memoria_virtual)
            
    
    def agregar_proceso_aleatorio(self, proceso):
        while True:
            fila_memoria_principal = random.randint(0, 4)  # Genera un número aleatorio entre 0 y 9
            columna_memoria_principal = random.randint(0, 4)  # Genera un número aleatorio entre 0 y 9
            fila_memoria_virtual = random.randint(0,9)
            columna_memoria_virtual = random.randint(0,9)
            
            if self.memoria_principal[fila_memoria_principal][columna_memoria_principal] == "":  # Verifica si la celda está vacía
                self.memoria_principal[fila_memoria_principal][columna_memoria_principal] = proceso  # Agrega el proceso en la posición elegida
                print(f"Proceso {proceso} agregado en la posición ({fila_memoria_principal}, {columna_memoria_principal}).")
            else:
                print(f"Posición ({fila_memoria_principal}, {columna_memoria_principal}) ocupada. Buscando otra posición...")
                
            if self.memoria_virtual[fila_memoria_virtual][columna_memoria_virtual] == "":
                self.memoria_virtual[fila_memoria_virtual][columna_memoria_virtual] = proceso
                print(f"Proceso {proceso} agregado en la posición ({fila_memoria_virtual}, {columna_memoria_virtual}).")
                break  # Salir del bucle una vez que se ha agregado el proceso
            else:
                print(f"Posición ({fila_memoria_virtual}, {columna_memoria_virtual}) ocupada. Buscando otra posición...")