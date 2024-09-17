from flask import Flask, request, render_template
from modelo.Procesos import Procesos

app = Flask(__name__)

@app.route('/', methods=['GET'])

def index():
    return render_template('index.html', proceso=None)

@app.route('/crear_proceso', methods=['POST'])

def crear_proceso():
    id = request.form.get('id')
    nombre = request.form.get('nombre')
    tamano = request.form.get('tamano')
    prioridad = request.form.get('prioridad')
    recursos = [rec for rec in request.form.getlist('recursos')]
    
    # Imprimir los datos en la consola para verificar
    print(f"ID: {id}, Nombre: {nombre}, Tamaño: {tamano}, Prioridad: {prioridad}, Recursos: {recursos}")

    nuevo_proceso = Procesos(id=id, nombre=nombre, tamano=tamano, prioridad=prioridad, recursos=recursos)
    
    return render_template('index.html', proceso=nuevo_proceso)

if __name__ == '__main__':
    app.run(debug=True)
