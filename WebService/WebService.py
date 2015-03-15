import json
from flask import Flask, request, abort, render_template, json, jsonify
from ListaDobleAirport import DoubleListAirport

app = Flask(__name__)

# lista doble Aeropuertos
aeroPuertos = DoubleListAirport()

USERS = {
    'user1': {'name': 'mike', 'email':'aaa@gmail.com'},
    'user2': {'name': 'lalit','email':'aaa@gmail.com'},
    'user3': {'name': 'sunil','email':'aaa@gmail.com'},
}

VUELOS = {
    'vuelo1': {'name': 'mike', 'email':'aaa@gmail.com'},
    'vuelo2': {'name': 'lalit','email':'aaa@gmail.com'},
    'vuelo3': {'name': 'sunil','email':'aaa@gmail.com'},
}

def abort_if_user_doesnt_exist(user_id):
    if user_id not in USERS:
        abort(404, message="User {} doesn't exist".format(user_id))

@app.route('/')
def index():
    return render_template('hello.html', name='Estructuras De Datos')

# User
#   Muestra la lista completa de usuarios
@app.route('/usuarios', methods=['GET'])
def usuarios():
    return json.dumps(USERS)
#   Muestra un usuario por su id
@app.route('/usuario/<user_id>', methods=['GET'])
def usuario(user_id):
    abort_if_user_doesnt_exist(user_id)
    return json.dumps(USERS[user_id])

# Vuelos
#   Muestra la lista completa de vuelos
@app.route('/vuelos', methods=['GET'])
def vuelos():
    return json.dumps(VUELOS)
#   Muestra un vuelo por su id
@app.route('/vuelo/<string:vuelo_id>', methods=['GET'])
def vuelo(vuelo_id):
    return json.dumps('VUELO: '+vuelo_id)

# Aeropuertos
#   Crea un nuevo aeropuerto
@app.route('/aeropuerto/crear', methods=['POST'])
def aeropuerto():
    id = request.form['id']
    nombre = request.form['nombre']
    pais = request.form['pais']
    contra = request.form['contra']
    aeroPuertos.append(id, nombre, pais, contra)
    return "creado", 200
#   Muestra la lista completa de aeropuertos
@app.route('/aeropuertos', methods=['GET'])
def aeropuertos():
    res = aeroPuertos.show()
    return json.dumps(res)

if __name__ == '__main__':
    app.run(
        # host="0.0.0.0",
        # port=int("5000")
        debug=True
    )