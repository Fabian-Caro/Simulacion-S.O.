from flask import Flask, request, render_template, redirect, url_for, jsonify
from modelo.Procesos import Procesos
from modelo.Recurso import Recurso
from modelo.Colas import Bloqueados
from modelo.Memoria import Memoria
app = Flask(__name__)

memoria_instance = Memoria()

cola_nuevos = []
cola_listos = []
cola_bloqueados = []
proceso_ejecucion = None
proceso_bloqueado = None

recursos = [
    Recurso("001", "Disco duro", None),
    Recurso("002", "Tarjeta gráfica", None),
    Recurso("003", "Impresora", None),
    Recurso("004", "Archivos", None),
    Recurso("005", "Red", None),
]

terminados = []
recursos_libres = []

@app.route('/', methods=['GET'])
def index():
    bloqueados = {
        'DiscoDuro': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso1],
        'TarjetaGrafica': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso2],
        'Impresora': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso3],
        'Archivos': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso4],
        'Red': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso5]
    }

    return render_template(
        'index.html', 
        procesos_nuevos=cola_nuevos,
        procesos_listos=cola_listos, 
        proceso_ejecucion=proceso_ejecucion, 
        proceso_bloqueado=proceso_bloqueado, 
        recursos=recursos, 
        terminados=terminados,
        bloqueados=bloqueados)

@app.route('/modelo', methods=['GET'])
def modelo():
    bloqueados = {
        'DiscoDuro': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso1],
        'TarjetaGrafica': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso2],
        'Impresora': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso3],
        'Archivos': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso4],
        'Red': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso5]
    }

    return render_template(
        'modelo.html', 
        procesos_listos=cola_listos, 
        proceso_ejecucion=proceso_ejecucion, 
        proceso_bloqueado=proceso_bloqueado, 
        recursos=recursos, 
        terminados=terminados,
        bloqueados=bloqueados)

@app.route('/memoria', methods=['GET'])
def memoria():
    memoria_principal = memoria_instance.obtener_memoria_principal()
    memoria_virtual = memoria_instance.obtener_memoria_virtual()
    return render_template('memoria.html', memoria_principal=memoria_principal, memoria_virtual = memoria_virtual)

@app.route('/crear_proceso', methods=['POST'])
def crear_proceso():
    global proceso_ejecucion
    
    id_proceso = request.form.get('id')
    nombre = request.form.get('nombre')
    tamano = request.form.get('tamano')
    recurso_seleccionado =  request.form.getlist('recursos')
    
    # recursos_asignados = []
    recursos_necesarios = []
    
    for recurso_id in recurso_seleccionado:
        recurso = next((r for r in recursos if r.get_id_recurso() == recurso_id), None)
        if recurso:
            recursos_necesarios.append(recurso)

    print(f"ID: {id_proceso}, Nombre: {nombre}, Tamaño: {tamano}, ")
    for recurso in recursos:
        print(f"Recursos: {recurso}")
    nuevo_proceso = Procesos(id_proceso, nombre, tamano, recursos_necesarios)
    
    cola_listos.append(nuevo_proceso)
    
    if not memoria_instance.agregar_proceso(nuevo_proceso.get_id_proceso()):
        print("No se pudo agregar el proceso a la memoria.")
        
    return redirect(url_for('modelo'))

@app.route('/creacion', methods=['GET', 'POST'])
def creacion():
    bloqueados = {
        'DiscoDuro': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso1],
        'TarjetaGrafica': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso2],
        'Impresora': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso3],
        'Archivos': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso4],
        'Red': [proceso.get_nombre_proceso() for proceso in Bloqueados.recurso5]
    }
    
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
        
        cola_nuevos.append(nuevo_proceso)
        
        if not memoria_instance.agregar_proceso_aleatorio(nuevo_proceso):
            print("No se pudo agregar el proceso a la memoria.")
            
        return redirect(url_for('creacion'))
    return render_template(
        'creacion.html',
        procesos_nuevos=cola_nuevos,
        procesos_listos=cola_listos, 
        proceso_ejecucion=proceso_ejecucion, 
        proceso_bloqueado=proceso_bloqueado, 
        recursos=recursos, 
        terminados=terminados,
        bloqueados=bloqueados)  # Devuelve la vista cuando es un GET

    
@staticmethod
def de_ejecucion_a_listos():
    recursos_liberados = proceso_ejecucion.liberar_recursos()
    # recursos_asginados = proceso_ejecucion.get_recursos_asignados()
    recursos_necesarios = proceso_ejecucion.get_recursos_necesarios()
    for recurso in recursos_liberados:
        print(f"Recurso { recurso.get_nombre_recurso() } liberado.")
    # for recurso in recursos_asginados:
    #     print(f"Recurso { recurso.get_nombre_recurso() } asignado.")
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
        
@app.route('/a_listos', methods=['POST'])
def a_listos():
    de_nuevo_a_listo()
    return redirect(url_for('modelo'))

@app.route('/ejecutar_proceso', methods=['POST'])
def ejecutar_proceso():
    global proceso_ejecucion
    de_nuevo_a_listo()
    if not proceso_ejecucion:
        de_listos_a_ejecucion()
    else:
        proceso_ejecucion = enviar_a_listo_o_bloqueado_o_terminado()

    resultado = ', '.join(map(str, terminados))
    print("Cola de bloqueados Disco duro: " + str(list(Bloqueados.recurso1)))
    print("Cola de bloqueados Tarjeta gráfica: " + str(list(Bloqueados.recurso2)))
    print("Cola de bloqueados Impresora: " + str(list(Bloqueados.recurso3)))
    print("Cola de bloqueados Archivos: " + str(list(Bloqueados.recurso4)))
    print("Cola de bloqueados Red: " + str(list(Bloqueados.recurso5)))
    print("procesos terminados: "+str(resultado))
    
    verificar_bloqueados()        
    return redirect(url_for('modelo'))

def verificar_bloqueados():
    global proceso_bloqueado
    
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
        cola_listos.append(proceso_bloqueado)
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