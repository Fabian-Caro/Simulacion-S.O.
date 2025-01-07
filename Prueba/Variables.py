from modelo.Colas import Bloqueados
from modelo.Recurso import Recurso
from modelo.Memoria import Memoria
class Variables(object):
    memoria_instance = Memoria()

    cola_nuevos = []
    cola_listos = []
    cola_prioridad1 = []
    cola_bloqueados = []
    proceso_ejecucion = None
    proceso_bloqueado = None
    idProceso = 1

    proceso_creado = []
    recursos = [
        Recurso("001", "Disco duro", None),
        Recurso("002", "Tarjeta gráfica", None),
        Recurso("003", "Impresora", None),
        Recurso("004", "Archivos", None),
        Recurso("005", "Red", None),
    ]
    bloqueados = {
        'DiscoDuro': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso1],
        'TarjetaGrafica': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso2],
        'Impresora': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso3],
        'Archivos': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso4],
        'Red': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso5]
    }
    terminados = []
    recursos_libres = []