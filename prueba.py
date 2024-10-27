from modelo.Procesos import Procesos
from modelo.Recurso import Recurso
from modelo.Colas import Bloqueados
import random

recursos = [
    Recurso("001", "Disco duro", None),
    Recurso("002", "Tarjeta gráfica", None),
    Recurso("003", "Impresora", None),
    Recurso("004", "Archivos", None),
    Recurso("005", "Red", None),
]

r1 = {recursos[0],recursos[1]}
p = [None]*2
p[0] = Procesos(1, 'p1', 10, r1)
p[1] = Procesos(2, 'p2', 10, r1)

recursos[0].set_proceso(p[0])
recursos[1].set_proceso(p[1])

for proceso in p:
    no_pasa_a_bloqueados,id_recursos = proceso.no_pasa_a_bloqueados()
    if no_pasa_a_bloqueados:
        print(str(proceso.get_nombre_proceso())+"  no pasa a bloqueado")
    else:
        for idR in id_recursos:
            Bloqueados.enviar_a_cola_bloqueados(idR,proceso)
        proceso.terminar_ejecucion()


# print(Bloqueados.get_cola_bloqueados("001"))
# print(Bloqueados.get_cola_bloqueados("002"))
