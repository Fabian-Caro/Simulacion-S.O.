from modelo.Colas import Bloqueados
from modelo.Procesos import Procesos
from modelo.Recurso import Recurso

cola_nuevos = []
cola_listos = []
cola_bloqueados = []
proceso_ejecucion = None
proceso_bloqueado = None

terminados = []
recursos_libres = []

recursos = [
    Recurso("001", "R1", None),
    Recurso("002", "R2", None),
    Recurso("003", "R3", None),
    Recurso("004", "R4", None),
    Recurso("005", "R5", None),
]

def main():
    p1 = Procesos(1, "p1", 10,0, {recursos[0],recursos[1],recursos[2]})
    p2 = Procesos(2, "p2", 10,0, {recursos[0],recursos[1],recursos[2],recursos[3]})

    recursos[0].set_proceso(p1)
    recursos[1].set_proceso(p2)
    recursos[2].set_proceso(p1)
    recursos[3].set_proceso(p2)

    for r in recursos:
        if r.get_proceso():
            print(r.get_nombre_recurso()+" "+str(r.get_proceso().get_nombre_proceso()))

    enviar_a_listo_o_bloqueado_o_terminado(p1)
    enviar_a_listo_o_bloqueado_o_terminado(p2)
        
    interblouqeados = Bloqueados.interbloqueados
    print(len(interblouqeados))
    for p in interblouqeados:
        if p:
            print(p.get_nombre_proceso())
    
    for i in Bloqueados.romper_interbloqueo(interblouqeados):
        recursos[i-1].set_proceso(None)

    Bloqueados.to_string()

    for r in recursos:
        if r.get_proceso():
            print(r.get_nombre_recurso()+" "+str(r.get_proceso().get_nombre_proceso()))
@staticmethod
def enviar_a_listo_o_bloqueado_o_terminado(proceso_ejecucion):

    no_pasa_a_bloqueados,id_recursos = proceso_ejecucion.no_pasa_a_bloqueados()

    if no_pasa_a_bloqueados:
        proceso_ejecucion.set_tamano_proceso(int (proceso_ejecucion.get_tamano_proceso())-2)
        if int (proceso_ejecucion.get_tamano_proceso()) > 0:
            de_ejecucion_a_listos()
        else:
            de_ejecucion_a_terminados()
    else:
        for idR in id_recursos:
            Bloqueados.enviar_a_cola_bloqueados(idR,proceso_ejecucion)

    return None

@staticmethod
def de_ejecucion_a_listos():
    recursos_liberados = proceso_ejecucion.liberar_recursos_L()
    # recursos_asginados = proceso_ejecucion.get_recursos_asignados()
    recursos_necesarios = proceso_ejecucion.get_recursos_necesarios()
    for recurso in recursos_liberados:
        print(f"Recurso { recurso.get_nombre_recurso() } liberado.")
    # for recurso in recursos_asginados:
    #     print(f"Recurso { recurso.get_nombre_recurso() } asignado.")
    for recurso in recursos_necesarios:
        print(f"Recurso { recurso.get_nombre_recurso() } necesarios.") 
    if proceso_ejecucion.get_prioridad()==0:
        cola_listos.append(proceso_ejecucion)
    elif proceso_ejecucion.get_prioridad()==1:
        cola_prioridad1.append(proceso_ejecucion)

@staticmethod
def de_ejecucion_a_terminados():
    terminados.append(proceso_ejecucion)
    memoria_instance.limpiar_memoria(proceso_ejecucion)
    proceso_ejecucion.liberar_todos_recursos()

@staticmethod
def de_listos_a_ejecucion():
    global proceso_ejecucion
    if cola_prioridad1:
        proceso_ejecucion = cola_prioridad1.pop(0)
    elif cola_listos:
        proceso_ejecucion = cola_listos.pop(0)
        
@staticmethod
def de_nuevo_a_listo():
    while cola_nuevos:
        proceso_nuevo = cola_nuevos.pop(0)
        if proceso_nuevo.get_prioridad()==0:
            cola_listos.append(proceso_nuevo)
        elif proceso_nuevo.get_prioridad()==1:
            cola_prioridad1.append(proceso_nuevo)
        print(f"Proceso {proceso_nuevo.get_id_proceso()} movido a cola de listos.")

if __name__ == "__main__":
    main()