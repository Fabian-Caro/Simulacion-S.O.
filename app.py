from flask import Flask, request, render_template, redirect, url_for
from modelo.Procesos import Procesos

app = Flask(__name__)

cola_listos = []
cola_ejecución = []
proceso_ejecucion = None

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', procesos_listos=cola_listos, proceso_ejecucion=proceso_ejecucion)

@app.route('/crear_proceso', methods=['POST'])
def crear_proceso():
    global proceso_ejecucion
    
    id_proceso = request.form.get('id')
    nombre = request.form.get('nombre')
    tamano = request.form.get('tamano')
    prioridad = request.form.get('prioridad')
    recursos = [rec for rec in request.form.getlist('recursos')]
    
    # Imprimir los datos en la consola para verificar
    print(f"ID: {id_proceso}, Nombre: {nombre}, Tamaño: {tamano}, Prioridad: {prioridad}, Recursos: {recursos}")

    nuevo_proceso = Procesos(id_proceso, nombre, tamano, prioridad, recursos)
    
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
def de_ejecucion_a_listos():
    proceso_ejecucion.set_tamano(int (proceso_ejecucion.get_tamano())-2)
    cola_listos.append(proceso_ejecucion)

@app.route('/ejecutar_proceso', methods=['POST'])
def ejecutar_proceso():
   global proceso_ejecucion
   if cola_listos:
       de_ejecucion_a_listos()
       proceso_ejecucion = cola_listos.pop(0)

   return redirect(url_for('index'))
#    if cola_listos:
#        proceso_a_ejecutar = cola_listos.pop(0)

#        if len(cola_ejecución) == 0:
#            cola_ejecución.append(proceso_a_ejecutar)
   # return render_template('index.html', procesos_listos=cola_listos, proceso_ejecucion = cola_ejecución[0] if cola_ejecución else None)

if __name__ == '__main__':
    app.run(debug=True)
