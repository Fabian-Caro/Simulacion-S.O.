from flask import Flask, request, render_template, redirect, url_for
from modelo.Procesos import Procesos
from modelo.Recurso import Recurso
import random

app = Flask(__name__)

cola_listos = []
# cola_ejecución = []
proceso_ejecucion = None

R = [
    Recurso("001", "Disco duro", None),
    Recurso("002", "Tarjeta gráfica", None),
    Recurso("003", "Impresora", None),
    Recurso("004", "Archivos", None),
    Recurso("005", "Red", None),
    Recurso("006", "Teclado", None),
    Recurso("007", "Raton", None),
    Recurso("008", "Pantalla", None),
    Recurso("009", "Parlante", None)
]

terminados = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', procesos_listos=cola_listos, proceso_ejecucion=proceso_ejecucion, recursos=R, terminados=terminados)

@app.route('/crear_proceso', methods=['POST'])
def crear_proceso():
    global proceso_ejecucion
    
    id_proceso = request.form.get('id')
    nombre = request.form.get('nombre')
    tamano = request.form.get('tamano')
    prioridad = request.form.get('prioridad')
    recursos_asignados = [rec for rec in R if rec.get_id_recurso() in request.form.getlist('recursos')]
    # Imprimir los datos en la consola para verificar
    print(f"ID: {id_proceso}, Nombre: {nombre}, Tamaño: {tamano}, Prioridad: {prioridad}, Recursos: {recursos_asignados[0].get_nombre_recurso()}")
    nuevo_proceso = Procesos(id_proceso, nombre, tamano, prioridad, recursos_asignados)
    
    cola_listos.append(nuevo_proceso)
    
    if not proceso_ejecucion and cola_listos:
        proceso_ejecucion = cola_listos.pop(0)
        
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
def ver_si_estan_disponibles_recursos():
    recursos =  proceso_ejecucion.get_recursos()
    flag = True
    for r in recursos:
        if R[r].get_disponibilidad_recurso() != proceso_ejecucion and R[r].get_disponibilidad_recurso() != None:
            flag = False
            break
    return flag

@staticmethod
def de_ejecucion_a_listos():
    cola_listos.append(proceso_ejecucion)

@staticmethod
def liberar_o_no_recurso():
    recursos =  proceso_ejecucion.get_recursos()
    i = 0
    for r in recursos:
        se_libera = random.randint(True,False)
        if se_libera:
            proceso_ejecucion.get_recursos().pop(i)
            R[r] = None

@staticmethod
def de_ejecucion_a_terminados():
    terminados.append(proceso_ejecucion.get_nombre())

@app.route('/ejecutar_proceso', methods=['POST'])
def ejecutar_proceso():
    global proceso_ejecucion
    proceso_ejecucion.set_tamano(int (proceso_ejecucion.get_tamano())-2)
    if cola_listos:
        if proceso_ejecucion.get_tamano() > 0:
            if ver_si_estan_disponibles_recursos(proceso_ejecucion):
                de_ejecucion_a_listos()
            # else:
            #     enviar_a_bloqueados()
        else:
            de_ejecucion_a_terminados()
        proceso_ejecucion = cola_listos.pop(0)
    else:
        if proceso_ejecucion.get_tamano() == 0:
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