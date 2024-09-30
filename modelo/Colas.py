from collections import deque

class Bloqueados(object):
    # Declaración de variables estáticas
    # si quieres puedes dejarlo asi : r1 = []
    r1 = deque()
    r2 = deque()
    r3 = deque()
    r4 = deque()
    r5 = deque()

    def __init__(self):
        pass  # No se necesitan variables de instancia, ya que usamos variables estáticas

    @staticmethod
    def enviar_a_cola_bloqueados(recurso, proceso):
        if recurso == 1:
            Bloqueados.r1.append(proceso)
        elif recurso == 2:
            Bloqueados.r2.append(proceso)
        elif recurso == 3:
            Bloqueados.r3.append(proceso)
        elif recurso == 4:
            Bloqueados.r4.append(proceso)
        else:
            Bloqueados.r5.append(proceso)
    
    # es la logica para liberar cola de bloqueado que estaba desarrollando en el proyecto anterior
#     @staticmethod
#     def liberar_cola_bloqueados():
        
#         if Recurso.recurso_proceso[0] == None and len(Bloqueados.r1)>0:
#             proceso_por_liberar = Bloqueados.r1.popleft()
#             Listos.listos.append(proceso_por_liberar)
#             proceso_por_liberar.ultimoRecursoIndex+=1
#         elif Recurso.recurso_proceso[1] == None and len(Bloqueados.r2)>0:
#             proceso_por_liberar = Bloqueados.r2.popleft()
#             Listos.listos.append(proceso_por_liberar)
#             proceso_por_liberar.ultimoRecursoIndex+=1
#         elif Recurso.recurso_proceso[2] == None and len(Bloqueados.r3)>0:
#             proceso_por_liberar = Bloqueados.r3.popleft()
#             Listos.listos.append(proceso_por_liberar)
#             proceso_por_liberar.ultimoRecursoIndex+=1
#         elif Recurso.recurso_proceso[3] == None and len(Bloqueados.r4)>0:
#             proceso_por_liberar = Bloqueados.r4.popleft()
#             Listos.listos.append(proceso_por_liberar)
#             proceso_por_liberar.ultimoRecursoIndex+=1
#         elif Recurso.recurso_proceso[4] == None and len(Bloqueados.r5)>0:
#             proceso_por_liberar = Bloqueados.r5.popleft()
#             Listos.listos.append(proceso_por_liberar)
#             proceso_por_liberar.ultimoRecursoIndex+=1

# class Listos(object):
#     # Declaración de variables estáticas
#     listos = deque()

#     def __init__(self):
#         pass  # No se necesitan variables de instancia, ya que usamos variables estáticas

# class Recurso(object):
#     recurso_proceso = [None,None,None,None,None] # Si es None, por ejemplo recurso_proceso[0] = r1 = None esta libre. 

#     @staticmethod
#     def MostrarRecurso_Proceso():
#         i = 1
#         for elemento in Recurso.recurso_proceso:
#             if elemento != None:
#                 print("R"+str(i)+" esta asignado a: "+str(elemento.nombre))
#                 i+=1