from collections import deque
from modelo.Procesos import Procesos
from modelo.Recurso import Recurso

class Bloqueados(object):
    # Declaración de variables estáticas
    # si quieres puedes dejarlo asi : r1 = []
    recurso1 = deque()
    recurso2 = deque()
    recurso3 = deque()
    recurso4 = deque()
    recurso5 = deque()

    interbloqueados = []
    def __init__(self):
        pass  # No se necesitan variables de instancia, ya que usamos variables estáticas

    @staticmethod
    def enviar_a_cola_bloqueados(recurso, proceso):
        
        if recurso == 1:
            Bloqueados.recurso1.append(proceso)
        elif recurso == 2:
            Bloqueados.recurso2.append(proceso)
        elif recurso == 3:
            Bloqueados.recurso3.append(proceso)
        elif recurso == 4:
            Bloqueados.recurso4.append(proceso)
        else:
            Bloqueados.recurso5.append(proceso)
        
        Bloqueados.interbloqueados = Bloqueados.interbloqueado(proceso,recurso)

    @staticmethod
    def interbloqueado(proceso,cola_actual):
        interbloqueado = None
        print("se envia a cola bloqueado "+str(cola_actual)+": "+str(proceso.get_nombre_proceso()))
        colas = []
        for r in proceso.get_recursos_necesarios():
            if r.get_proceso()==proceso:
                print(proceso.get_nombre_proceso()+" "+str(r.get_nombre_recurso()))
                colas.append(r.get_id_recurso())
                
        for cola in colas:
            temp = Bloqueados.verificar_interbloqueo(int(cola),cola_actual)
            if temp:
                interbloqueado = temp
        if interbloqueado:
            return [interbloqueado,proceso]

    @staticmethod
    def verificar_interbloqueo(cola,cola_actual):
        if cola == 1:
            for p in Bloqueados.recurso1:
                for r in p.get_recursos_necesarios():
                    if r.get_proceso()==p and int(r.get_id_recurso())==cola_actual:
                        return p
        elif cola == 2:
            for p in Bloqueados.recurso2:
                for r in p.get_recursos_necesarios():
                    if r.get_proceso()==p and int(r.get_id_recurso())==cola_actual:
                        return p
        elif cola == 3:
            for p in Bloqueados.recurso3:
                for r in p.get_recursos_necesarios():
                    if r.get_proceso()==p and int(r.get_id_recurso())==cola_actual:
                        return p
        elif cola == 4:
            for p in Bloqueados.recurso4:
                for r in p.get_recursos_necesarios():
                    if r.get_proceso()==p and int(r.get_id_recurso())==cola_actual:
                        return p
        elif cola == 5:
            for p in Bloqueados.recurso5:
                for r in p.get_recursos_necesarios():
                    if r.get_proceso()==p and int(r.get_id_recurso())==cola_actual:
                        return p
        return None

    def recursos_interbloqueos(procesos,cola_listos):
        recursos_interbloqueos = []

        for proceso in procesos:
            cola_listos.append(proceso)
            if Bloqueados.recurso1.__contains__(proceso):
                Bloqueados.recurso1.remove(proceso)
                recursos_interbloqueos.append(1)
            if Bloqueados.recurso2.__contains__(proceso):
                Bloqueados.recurso2.remove(proceso)
                recursos_interbloqueos.append(2)
            if Bloqueados.recurso3.__contains__(proceso):
                Bloqueados.recurso3.remove(proceso)
                recursos_interbloqueos.append(3)
            if Bloqueados.recurso4.__contains__(proceso):
                Bloqueados.recurso4.remove(proceso)
                recursos_interbloqueos.append(4)
            if Bloqueados.recurso5.__contains__(proceso):
                Bloqueados.recurso5.remove(proceso)
                recursos_interbloqueos.append(5)
        return recursos_interbloqueos
    
    def sacar_de_bloqueado1(proceso):
        
        Bloqueados.recurso1.remove(proceso)
    @staticmethod
    def get_cola_bloqueados(id_recurso):
        if id_recurso == "001":
            return list(Bloqueados.recurso1)
        elif id_recurso == "002":
            return list(Bloqueados.recurso2)
        elif id_recurso == "003":
            return list(Bloqueados.recurso3)
        elif id_recurso == "004":
            return list(Bloqueados.recurso4)
        elif id_recurso == "005":
            return list(Bloqueados.recurso5)
        else:
            return "No hay procesos bloqueados."
    def to_string():
        print("cola R1")
        for p in Bloqueados.recurso1:
            print(p.get_nombre_proceso())
        print("cola R2")
        for p in Bloqueados.recurso2:
            print(p.get_nombre_proceso())
        print("cola R3")
        for p in Bloqueados.recurso3:
            print(p.get_nombre_proceso())
        print("cola R4")
        for p in Bloqueados.recurso4:
            print(p.get_nombre_proceso())
        print("cola R5")
        for p in Bloqueados.recurso5:
            print(p.get_nombre_proceso())