from flask import Flask, request, render_template, redirect, url_for, jsonify
from modelo.Procesos import Procesos
from modelo.Colas import Bloqueados
from Prueba.Operacion import Cambio_estado
from Prueba.Variables import Variables
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():

    return render_template(
        'index.html', 
        procesos_nuevos=Variables.cola_nuevos,
        procesos_listos=Variables.cola_listos,
        procesos_prioridad1 = Variables.cola_prioridad1,
        proceso_ejecucion=Variables.proceso_ejecucion,
        proceso_bloqueado=Variables.proceso_bloqueado,
        recursos=Variables.recursos,
        proceso_creado = Variables.proceso_creado,
        terminados=Variables.terminados,
        bloqueados=Variables.bloqueados)

@app.route('/modelo', methods=['GET'])
def modelo():

    return render_template(
        'modelo.html', 
        procesos_listos=Variables.cola_listos, 
        procesos_prioridad1 = Variables.cola_prioridad1,
        proceso_ejecucion=Variables.proceso_ejecucion, 
        proceso_bloqueado=Variables.proceso_bloqueado, 
        recursos=Variables.recursos, 
        proceso_creado = Variables.proceso_creado,
        terminados=Variables.terminados,
        bloqueados=Variables.bloqueados)

@app.route('/memoria', methods=['GET'])
def memoria():
    memoria_principal = Variables.memoria_instance.obtener_memoria_principal()
    memoria_virtual = Variables.memoria_instance.obtener_memoria_virtual()
    return render_template('memoria.html', memoria_principal=memoria_principal, memoria_virtual = memoria_virtual)

@app.route('/crear_proceso', methods=['POST']) # para que sirve???
def crear_proceso():    
    id_proceso = request.form.get('id')
    nombre = request.form.get('nombre')
    tamano = request.form.get('tamano')
    prioridad = request.form.get('prioridad')
    recurso_seleccionado =  request.form.getlist('recursos')
    
    # recursos_asignados = []
    recursos_necesarios = []
    
    for recurso_id in recurso_seleccionado:
        recurso = next((r for r in Variables.recursos if r.get_id_recurso() == recurso_id), None)
        if recurso:
            recursos_necesarios.append(recurso)

    print(f"ID: {id_proceso}, Nombre: {nombre}, Tamaño: {tamano}, prioridad: {prioridad}")
    for recurso in Variables.recursos:
        print(f"Recursos: {recurso}")
    nuevo_proceso = Procesos(id_proceso, nombre, tamano, prioridad, recursos_necesarios,"nuevo")
    
    Variables.cola_nuevos.append(nuevo_proceso)
    Variables.proceso_creado.append(nuevo_proceso)
    if not Variables.memoria_instance.agregar_proceso(nuevo_proceso.get_id_proceso()):
        print("No se pudo agregar el proceso a la memoria.")
        
    return redirect(url_for('modelo'))

@app.route('/creacion', methods=['GET', 'POST'])
def creacion():
    
    if request.method == 'POST':
        id_proceso = Variables.idProceso
        Variables.idProceso+=1
        nombre = request.form.get('nombre')
        tamano = request.form.get('tamano')
        prioridad = int(request.form.get('prioridad',0))
        recurso_seleccionado =  request.form.getlist('recursos')

        recursos_necesarios = []
        
        for recurso_id in recurso_seleccionado:
            recurso = next((r for r in Variables.recursos if r.get_id_recurso() == recurso_id), None)
            if recurso:
                recursos_necesarios.append(recurso)

        # print(f"ID: {id_proceso}, Nombre: {nombre}, Tamaño: {tamano}, prioridad: {prioridad}")
        # for recurso in recursos:
        #     print(f"Recursos: {recurso}")
        nuevo_proceso = Procesos(id_proceso, nombre, tamano, prioridad, recursos_necesarios,"nuevo")
        Variables.proceso_creado.append(nuevo_proceso)
        Variables.cola_nuevos.append(nuevo_proceso)
        
        if not Variables.memoria_instance.agregar_proceso_aleatorio(nuevo_proceso):
            print("No se pudo agregar el proceso a la memoria.")
            
        return redirect(url_for('creacion'))
    return render_template(
        'creacion.html',
        procesos_nuevos=Variables.cola_nuevos,
        procesos_listos=Variables.cola_listos, 
        procesos_prioridad1 = Variables.cola_prioridad1,
        proceso_ejecucion=Variables.proceso_ejecucion, 
        proceso_bloqueado=Variables.proceso_bloqueado, 
        recursos=Variables.recursos, 
        proceso_creado = Variables.proceso_creado,
        terminados=Variables.terminados,
        bloqueados=Variables.bloqueados)  # Devuelve la vista cuando es un GET

@app.route('/a_listos', methods=['POST'])
def a_listos():
    Cambio_estado.de_nuevo_a_listo()
    return redirect(url_for('modelo'))

@app.route('/ejecutar_proceso', methods=['POST'])
def ejecutar_proceso():
    
    Cambio_estado.de_nuevo_a_listo()
    if not Variables.proceso_ejecucion:
        if Bloqueados.interbloqueados:
            Cambio_estado.romper_interbloqueo()
        else:
            Cambio_estado.de_listos_a_ejecucion()
    else:
        if Variables.cola_prioridad1 and Variables.proceso_ejecucion.get_prioridad()==0 and Variables.cola_prioridad1[0].get_prioridad()==2:
            Cambio_estado.expulsar_un_proceso_e_ingresar_otro() # envia el proceso en ejecucion a listo sin descontar el tamano
        else:
            Variables.proceso_ejecucion = Cambio_estado.enviar_a_listo_o_bloqueado_o_terminado()

    # resultado = ', '.join(map(str, terminados))
    # print("Cola de bloqueados Disco duro: " + str(list(Bloqueados.recurso1)))
    # print("Cola de bloqueados Tarjeta gráfica: " + str(list(Bloqueados.recurso2)))
    # print("Cola de bloqueados Impresora: " + str(list(Bloqueados.recurso3)))
    # print("Cola de bloqueados Archivos: " + str(list(Bloqueados.recurso4)))
    # print("Cola de bloqueados Red: " + str(list(Bloqueados.recurso5)))
    # print("procesos terminados: "+str(resultado))
    
    verificar_bloqueados()        
    return redirect(url_for('modelo'))


def verificar_bloqueados():    
    for recurso_actual in Variables.recursos:
        if recurso_actual.get_proceso() is None:
            if recurso_actual.get_id_recurso() == "001" and Bloqueados.recurso1:
                print(f"Recurso 1: Por aquí es, { Bloqueados.recurso1 }")
                Variables.proceso_bloqueado = Bloqueados.recurso1.popleft()
                asignar_recurso(Variables.proceso_bloqueado, recurso_actual)
                verificar_si_esta_bloqueado(Variables.proceso_bloqueado)
            elif recurso_actual.get_id_recurso() == "002" and Bloqueados.recurso2:
                print(f"Recurso 2: Por aquí es, { Bloqueados.recurso2 }")
                Variables.proceso_bloqueado = Bloqueados.recurso2.popleft()
                asignar_recurso(Variables.proceso_bloqueado, recurso_actual)
                verificar_si_esta_bloqueado(Variables.proceso_bloqueado)
            elif recurso_actual.get_id_recurso() == "003" and Bloqueados.recurso3:
                print(f"Recurso 3: Por aquí es, { Bloqueados.recurso3 }")
                Variables.proceso_bloqueado = Bloqueados.recurso3.popleft()
                asignar_recurso(Variables.proceso_bloqueado, recurso_actual)
                verificar_si_esta_bloqueado(Variables.proceso_bloqueado)
            elif recurso_actual.get_id_recurso() == "004" and Bloqueados.recurso4:
                print(f"Recurso 4: Por aquí es, { Bloqueados.recurso4 }")
                Variables.proceso_bloqueado = Bloqueados.recurso4.popleft()
                asignar_recurso(Variables.proceso_bloqueado, recurso_actual)
                verificar_si_esta_bloqueado(Variables.proceso_bloqueado)
            elif recurso_actual.get_id_recurso() == "005" and Bloqueados.recurso5:
                print(f"Recurso 5: Por aquí es, { Bloqueados.recurso5 }")
                Variables.proceso_bloqueado = Bloqueados.recurso5.popleft()
                asignar_recurso(Variables.proceso_bloqueado, recurso_actual)
                verificar_si_esta_bloqueado(Variables.proceso_bloqueado)
            else:
                print(f"Recurso '{recurso_actual.get_nombre_recurso()}' libre")
    
    ## proceso_bloqueado.tiene_todos_los_recursos_listos()
    ## Bloqueados.sacar_de_bloqueado1(Bloqueados.recurso1[0])
    ## cola_listos.append(Bloqueados.recurso1[0])
    
def asignar_recurso(proceso_bloqueado, recurso_actual):
    for recurso_necesitado in proceso_bloqueado.get_recursos_necesarios():
        print(f"Recursos necesarios de {proceso_bloqueado.get_nombre_proceso()}: {recurso_necesitado.get_nombre_recurso()}")
    
    recurso_actual.set_proceso(proceso_bloqueado)
    # proceso_bloqueado.agregar_recurso_asignado(recurso_actual)

    # for recurso_asignado in proceso_bloqueado.get_recursos_asignados():
    #     print(f"Recursos asignados de {proceso_bloqueado.get_nombre_proceso()}: {recurso_asignado.get_nombre_recurso()}")
    
    if not verificar_si_esta_bloqueado(proceso_bloqueado):
        print(f"Proceso {proceso_bloqueado.get_nombre_proceso()} tiene todos los recursos necesarios, moviéndolo a cola de listos.")
        Variables.cola_listos.append(proceso_bloqueado)
        proceso_bloqueado.set_estado("listo")
    else:
        print(f"Proceso {proceso_bloqueado.get_nombre_proceso()} aún necesita más recursos.")

def verificar_si_esta_bloqueado(proceso):
    # Verifica si el proceso está en alguna de las colas de bloqueados
    for recurso_bloqueado in [Bloqueados.recurso1, Bloqueados.recurso2, Bloqueados.recurso3, Bloqueados.recurso4, Bloqueados.recurso5]:
        if proceso in recurso_bloqueado:
            return True
    return False
   
if __name__ == '__main__':
    app.run(debug=True)