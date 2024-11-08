from flask import Flask, request, render_template, redirect, url_for, jsonify
from modelo.Procesos import Procesos
from modelo.Recurso import recursos as listaRecursos
from modelo.Bloqueados import Bloqueados
from modelo.Memoria import Memoria

app = Flask(__name__)

memoria_instance = Memoria()

cola_nuevos = []
cola_listos = []
proceso_ejecucion = None
proceso_bloqueado = None
terminados = []

@app.route('/', methods=['GET'])
def index():
    bloqueados = Bloqueados.bloqueados()
    recursos = listaRecursos

    return render_template('index.html', procesos_nuevos=cola_nuevos, procesos_listos=cola_listos, proceso_ejecucion=proceso_ejecucion, 
                           proceso_bloqueado=proceso_bloqueado, recursos=recursos, terminados=terminados, bloqueados=bloqueados)

@app.route('/crear_proceso', methods=['GET', 'POST'])
def crear_proceso():
    bloqueados = Bloqueados.bloqueados()
    recursos = listaRecursos
    
    siguiente_id = id_autoincremental()

    if request.method == 'POST':
        global proceso_ejecucion

        id_proceso = request.form.get('id')
        nombre = request.form.get('nombre')
        tamano = request.form.get('tamano')
        recurso_seleccionado =  request.form.getlist('recursos')

        recursos_necesarios = []

        for recurso_id in recurso_seleccionado:
            recurso = next((r for r in recursos if r.get_id_recurso() == recurso_id), None)
            if recurso:
                recursos_necesarios.append(recurso)

        print(f"ID: {id_proceso}, Nombre: {nombre}, Tamaño: {tamano}, ")
        for recurso in recursos:
            print(f"Recursos: {recurso}")

        nuevo_proceso = Procesos(id_proceso, nombre, tamano, recursos_necesarios)

        if memoria_instance.memoria_disponible(memoria_instance.memoria_principal):
            cola_nuevos.append(nuevo_proceso)

            if not memoria_instance.agregar_proceso_aleatorio(nuevo_proceso):
                print("No se pudo agregar el proceso a la memoria.")

        else:
            print("No hay espacio disponible en la memoria principal. No se creará el proceso.")

        return redirect(url_for('crear_proceso'))

    return render_template('creacion.html', siguiente_id = siguiente_id, procesos_nuevos=cola_nuevos, procesos_listos=cola_listos, 
                           proceso_ejecucion=proceso_ejecucion, proceso_bloqueado=proceso_bloqueado, recursos=recursos, terminados=terminados,
                           bloqueados=bloqueados)

@app.route('/modelo', methods=['GET', 'POST'])
def modelo():
    bloqueados = Bloqueados.bloqueados()
    recursos = listaRecursos
    
    if request.method == 'POST':
        ejecutar_proceso()

    return render_template('modelo.html', procesos_listos=cola_listos, proceso_ejecucion=proceso_ejecucion, proceso_bloqueado=proceso_bloqueado, 
                           recursos=recursos, terminados=terminados, bloqueados=bloqueados)

@app.route('/memoria', methods=['GET'])
def memoria():
    memoria_principal = memoria_instance.obtener_memoria_principal()
    memoria_virtual = memoria_instance.obtener_memoria_virtual()
    return render_template('memoria.html', memoria_principal=memoria_principal, memoria_virtual = memoria_virtual)

def id_autoincremental():
    if not len(cola_nuevos):
        return len(cola_listos) + (len(Bloqueados.recurso1) + len(Bloqueados.recurso2) 
                                    + len(Bloqueados.recurso3) + len(Bloqueados.recurso4) 
                                    + len(Bloqueados.recurso5)) + len(terminados) + 1
    else:
        return len(cola_nuevos) + len(terminados) + 1

def ejecutar_proceso():
    global proceso_ejecucion
    de_nuevo_a_listo()
    if not proceso_ejecucion:
        de_listos_a_ejecucion()
    else:
        proceso_ejecucion = enviar_a_listo_o_bloqueado_o_terminado()

    Bloqueados.mostrar_estado_colas(terminados)
    verificar_bloqueados()        
    return redirect(url_for('modelo'))

@staticmethod
def de_ejecucion_a_listos():
    recursos_liberados = proceso_ejecucion.liberar_recursos()
    recursos_necesarios = proceso_ejecucion.get_recursos_necesarios()
    for recurso in recursos_liberados:
        print(f"Recurso { recurso.get_nombre_recurso() } liberado.")

    for recurso in recursos_necesarios:
        print(f"Recurso { recurso.get_nombre_recurso() } necesarios.") 

    cola_listos.append(proceso_ejecucion)

@staticmethod
def enviar_a_listo_o_bloqueado_o_terminado():
    global proceso_ejecucion

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

        proceso_ejecucion.liberar_todos_recursos()

    return None

@staticmethod
def de_ejecucion_a_terminados():
    terminados.append(proceso_ejecucion)
    memoria_instance.limpiar_memoria(proceso_ejecucion)
    proceso_ejecucion.liberar_todos_recursos()

@staticmethod
def de_listos_a_ejecucion():
    global proceso_ejecucion
    if cola_listos:
        proceso_ejecucion = cola_listos.pop(0)

@staticmethod
def de_nuevo_a_listo():
    while cola_nuevos:
        proceso_nuevo = cola_nuevos.pop(0)
        cola_listos.append(proceso_nuevo)
        print(f"Proceso {proceso_nuevo.get_id_proceso()} movido a cola de listos.")

def verificar_bloqueados():
    global proceso_bloqueado
    recursos = listaRecursos

    for recurso_actual in recursos:
        if recurso_actual.get_proceso() is None:
            if recurso_actual.get_id_recurso() == "001" and Bloqueados.recurso1:
                print(f"Recurso 1: Por aquí es, { Bloqueados.recurso1 }")
                proceso_bloqueado = Bloqueados.recurso1.popleft()
                asignar_recurso(proceso_bloqueado, recurso_actual)
                verificar_si_esta_bloqueado(proceso_bloqueado)
            elif recurso_actual.get_id_recurso() == "002" and Bloqueados.recurso2:
                print(f"Recurso 2: Por aquí es, { Bloqueados.recurso2 }")
                proceso_bloqueado = Bloqueados.recurso2.popleft()
                asignar_recurso(proceso_bloqueado, recurso_actual)
                verificar_si_esta_bloqueado(proceso_bloqueado)
            elif recurso_actual.get_id_recurso() == "003" and Bloqueados.recurso3:
                print(f"Recurso 3: Por aquí es, { Bloqueados.recurso3 }")
                proceso_bloqueado = Bloqueados.recurso3.popleft()
                asignar_recurso(proceso_bloqueado, recurso_actual)
                verificar_si_esta_bloqueado(proceso_bloqueado)
            elif recurso_actual.get_id_recurso() == "004" and Bloqueados.recurso4:
                print(f"Recurso 4: Por aquí es, { Bloqueados.recurso4 }")
                proceso_bloqueado = Bloqueados.recurso4.popleft()
                asignar_recurso(proceso_bloqueado, recurso_actual)
                verificar_si_esta_bloqueado(proceso_bloqueado)
            elif recurso_actual.get_id_recurso() == "005" and Bloqueados.recurso5:
                print(f"Recurso 5: Por aquí es, { Bloqueados.recurso5 }")
                proceso_bloqueado = Bloqueados.recurso5.popleft()
                asignar_recurso(proceso_bloqueado, recurso_actual)
                verificar_si_esta_bloqueado(proceso_bloqueado)
            else:
                print(f"Recurso '{recurso_actual.get_nombre_recurso()}' libre")
    
def asignar_recurso(proceso_bloqueado, recurso_actual):
    for recurso_necesitado in proceso_bloqueado.get_recursos_necesarios():
        print(f"Recursos necesarios de {proceso_bloqueado.get_nombre_proceso()}: {recurso_necesitado.get_nombre_recurso()}")
    
    recurso_actual.set_proceso(proceso_bloqueado)
    
    if not verificar_si_esta_bloqueado(proceso_bloqueado):
        print(f"Proceso {proceso_bloqueado.get_nombre_proceso()} tiene todos los recursos necesarios, moviéndolo a cola de listos.")
        cola_listos.append(proceso_bloqueado)
    else:
        print(f"Proceso {proceso_bloqueado.get_nombre_proceso()} aún necesita más recursos.")
        
def verificar_si_esta_bloqueado(proceso):
    for recurso_bloqueado in [Bloqueados.recurso1, Bloqueados.recurso2, Bloqueados.recurso3, Bloqueados.recurso4, Bloqueados.recurso5]:
        if proceso in recurso_bloqueado:
            return True
        
    return False
   
if __name__ == '__main__':
    app.run(debug=True)