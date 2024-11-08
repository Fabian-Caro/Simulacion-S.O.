import random

class Memoria:
    def __init__(self):
        self.memoria_principal = [["" for _ in range(4)] for _ in range(4)]
        self.memoria_virtual = [["" for _ in range(8)] for _ in range(8)]
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
            if len(fila) < 8:
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
        
    def memoria_disponible(self, memoria):
        for fila in memoria:
            if "" in fila:
                return True
        return False
            
    
    def agregar_proceso_aleatorio(self, proceso):
        if not self.memoria_disponible(self.memoria_principal):
            print("No hay espacio disponible en la memoria principal.")
            return False
        
        agregado_en_principal = False
        agregado_en_virtual = False
        
        while not (agregado_en_principal and agregado_en_virtual):
            fila_memoria_principal = random.randint(0, 3)  # Genera un número aleatorio entre 0 y 9
            columna_memoria_principal = random.randint(0, 3)  # Genera un número aleatorio entre 0 y 9
            fila_memoria_virtual = random.randint(0,7)
            columna_memoria_virtual = random.randint(0,7)
            
            if not agregado_en_principal and self.memoria_principal[fila_memoria_principal][columna_memoria_principal] == "":  # Verifica si la celda está vacía
                self.memoria_principal[fila_memoria_principal][columna_memoria_principal] = proceso # Agrega el proceso en la posición elegida
                agregado_en_principal = True
                print(f"Proceso {proceso} agregado en la posición ({fila_memoria_principal}, {columna_memoria_principal}).")
            else:
                print(f"Posición ({fila_memoria_principal}, {columna_memoria_principal}) ocupada. Buscando otra posición...")
                
            if not agregado_en_virtual and self.memoria_virtual[fila_memoria_virtual][columna_memoria_virtual] == "":
                self.memoria_virtual[fila_memoria_virtual][columna_memoria_virtual] = proceso
                agregado_en_virtual = True
                print(f"Proceso {proceso} agregado en la posición ({fila_memoria_virtual}, {columna_memoria_virtual}).")
            else:
                print(f"Posición ({fila_memoria_virtual}, {columna_memoria_virtual}) ocupada. Buscando otra posición...")
                
        return True