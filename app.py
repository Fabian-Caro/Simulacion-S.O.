from flask import Flask, request, render_template, redirect, url_for
from modelo.Procesos import Procesos
from modelo.Recurso import Recurso

app = Flask(__name__)

cola_listos = []
cola_ejecución = []
cola_bloqueados= []
proceso_ejecucion = None

recursos = [
    Recurso("001", "Disco duro", True),
    Recurso("002", "Tarjeta gráfica", True),
    Recurso("003", "Impresora", True),
    Recurso("004", "Archivos", True),
    Recurso("005", "Red", True),
    # Recurso("006", "Teclado", True),
    # Recurso("007", "Ratón", True),
    # Recurso("008", "Pantalla", True),
    # Recurso("009", "Parlante", True)
]

terminados = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', procesos_listos=cola_listos, proceso_ejecucion=proceso_ejecucion, recursos=recursos, terminados=terminados)

@app.route('/crear_proceso', methods=['POST'])
def crear_proceso():
    global proceso_ejecucion
    
    id_proceso = request.form.get('id')
    nombre = request.form.get('nombre')
    tamano = request.form.get('tamano')
    prioridad = request.form.get('prioridad')
    recurso_seleccionado =  request.form.getlist('recursos')
    
    recursos_asignados = []
    recursos_necesarios = []
    
    # for recurso in recurso_seleccionado:
    #     recursos_necesarios.append(recurso)
    for recurso_id in recurso_seleccionado:
        recurso = next((r for r in recursos if r.get_id_recurso() == recurso_id), None)
        if recurso:
            recursos_necesarios.append(recurso)
            # if recurso.is_disponibilidad_recurso():
            #     recursos_asignados.append(recurso)
            #     recurso.set_disponibilidad_recurso(False)
                
    ##recursos_asignados = [rec for rec in recursos if rec.get_id_recurso() in request.form.getlist('recursos')]
    
    # Imprimir los datos en la consola para verificar
    print(f"ID: {id_proceso}, Nombre: {nombre}, Tamaño: {tamano}, Prioridad: {prioridad}, Recursos: {recursos}")
    nuevo_proceso = Procesos(id_proceso, nombre, tamano, prioridad, recursos_asignados, recursos_necesarios)
    
    cola_listos.append(nuevo_proceso)
    
    if not proceso_ejecucion and cola_listos:
        posible_proceso = cola_listos.pop(0)
        
        proceso_ejecucion = posible_proceso
        # if posible_proceso.tiene_todos_los_recursos():
        #     proceso_ejecucion = posible_proceso
        # else:
        #     cola_bloqueados.append(posible_proceso)
        
    return redirect(url_for('index'))
    
    # return render_template('index.html', procesos_listos=cola_listos, proceso_ejecucion=None)

# @app.route('/ejecutar', methods=['POST'])
# def Ejecutar():
#     global proceso_ejecucion
    
#     if proceso_ejecucion:
#         cola_listos.append(proceso_ejecucion)
#         proceso_ejecucion = None
        
#     if cola_listos:
#         proceso_ejecucion = cola_listos.pop(0)
        
#     return redirect(url_for('index'))

@staticmethod
def de_ejecucion_a_listos():
    recursos_liberados = proceso_ejecucion.liberar_recursos()
    recursos_asginados = proceso_ejecucion.get_recursos_asignados()
    recursos_necesarios = proceso_ejecucion.get_recursos_necesarios()
    for recurso in recursos_liberados:
        print(f"Recurso { recurso.get_nombre_recurso() } liberado.")
    for recurso in recursos_asginados:
        print(f"Recurso { recurso.get_nombre_recurso() } asignado.")
    for recurso in recursos_necesarios:
        print(f"Recurso { recurso.get_nombre_recurso() } necesarios.") 
    cola_listos.append(proceso_ejecucion)

@staticmethod
def de_ejecucion_a_terminados():
    terminados.append(proceso_ejecucion.get_nombre_proceso())

#bloqueados
@staticmethod
def ver_si_estan_disponibles_recursos():
    R =  proceso_ejecucion.get_recursos()
    flag = True
    for r in R:
        if recursos[r].get_disponibilidad_recurso() != proceso_ejecucion and R[r].get_disponibilidad_recurso() != None:
            flag = False
            break
    return flag

@app.route('/ejecutar_proceso', methods=['POST'])
def ejecutar_proceso():
    global proceso_ejecucion
    
    proceso_ejecucion.set_tamano_proceso(int (proceso_ejecucion.get_tamano_proceso())-2)
    if cola_listos:
        if proceso_ejecucion.get_tamano_proceso() > 0:

            de_ejecucion_a_listos()
        else:
            de_ejecucion_a_terminados()
        if cola_listos:
            proceso_ejecucion = cola_listos.pop(0)
    else:
        if proceso_ejecucion.get_tamano_proceso() == 0:
            de_ejecucion_a_terminados()
            proceso_ejecucion = None
    # if len(terminados>0):
    resultado = ', '.join(map(str, terminados))
    print("procesos terminados: "+str(resultado))
    # else:
    #     print("No hay ningun proceso terminado") 
    return redirect(url_for('index'))
#    if cola_listos:
#        proceso_a_ejecutar = cola_listos.pop(0)

#        if len(cola_ejecución) == 0:
#            cola_ejecución.append(proceso_a_ejecutar)
   # return render_template('index.html', procesos_listos=cola_listos, proceso_ejecucion = cola_ejecución[0] if cola_ejecución else None)

if __name__ == '__main__':
    app.run(debug=True)