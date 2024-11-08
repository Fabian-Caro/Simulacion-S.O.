from collections import deque

class Bloqueados(object):
    # Declaración de variables estáticas
    # si quieres puedes dejarlo asi : r1 = []
    recurso1 = deque()
    recurso2 = deque()
    recurso3 = deque()
    recurso4 = deque()
    recurso5 = deque()

    def __init__(self):
        pass  # No se necesitan variables de instancia, ya que usamos variables estáticas

    @staticmethod
    def bloqueados():
        return {
            'DiscoDuro': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso1],
            'TarjetaGrafica': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso2],
            'Impresora': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso3],
            'Archivos': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso4],
            'Red': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso5]
        }
    
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

    @staticmethod
    def mostrar_estado_colas(terminados):
        resultado = ', '.join(map(str, terminados))
        print("Cola de bloqueados Disco duro: " + str(list(Bloqueados.recurso1)))
        print("Cola de bloqueados Tarjeta gráfica: " + str(list(Bloqueados.recurso2)))
        print("Cola de bloqueados Impresora: " + str(list(Bloqueados.recurso3)))
        print("Cola de bloqueados Archivos: " + str(list(Bloqueados.recurso4)))
        print("Cola de bloqueados Red: " + str(list(Bloqueados.recurso5)))
        print("procesos terminados: "+str(resultado))