from modelo.Procesos import Procesos
from modelo.Recurso import Recurso
import random

@staticmethod
def ver_si_estan_disponibles_recursos(proceso):
    recursos =  proceso.get_recursos()
    flag = True
    for r in recursos:
        if R[r].get_disponibilidad_recurso() != proceso and R[r].get_disponibilidad_recurso() != None:
            flag = False
            break
    return flag

@staticmethod
def liberar_o_no_recurso(proceso_ejecucion):
    recursos =  proceso_ejecucion.get_recursos()
    new_recusros = []

    for r in recursos:
        se_libera = True #random.randint(True,False)
        print(str(se_libera)+" "+str(r))
        if not se_libera:
            new_recusros.append(r)
        else:
            R[r].set_disponibilidad_recurso(None)
    return new_recusros

p1 = Procesos(1,'p1',10,None,[0])
p2 = Procesos(2,'p2',10,None,[0])

R = [
    Recurso("001", "Disco duro", p1),
    Recurso("002", "Tarjeta gráfica", None),
    Recurso("003", "Impresora", None),
    Recurso("004", "Archivos", None),
    Recurso("005", "Red", None),
    Recurso("006", "Teclado", None),
    Recurso("007", "Raton", None),
    Recurso("008", "Pantalla", None),
    Recurso("009", "Parlante", None)
]

print("Estan disponible los recursos?"+str(ver_si_estan_disponibles_recursos(p1)))

print()
new_recursos = liberar_o_no_recurso(p1)

print()
recursos =  new_recursos
for r in recursos:
    print(r)

print()

print(R[0].get_disponibilidad_recurso().get_nombre())
print(R[1].get_disponibilidad_recurso().get_nombre())
print(R[2].get_disponibilidad_recurso().get_nombre())
print(R[3].get_disponibilidad_recurso().get_nombre())

# for i in range(0,3):
#     if R[i].get_disponibilidad_recurso() == None:
#         print(None)
        # print(R[i].get_disponibilidad_recurso().get_nombre())
    # else:
    #     print(None)