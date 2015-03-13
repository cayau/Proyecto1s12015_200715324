import json
from flask import Flask, request, abort
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'post'
    else:
        return 'get'

@app.route('/users', methods=['GET'])
def users():
    return json.dumps(USERS)

# User
#   show a single user and lets you delete them
@app.route('/user/<user_id>', methods=['GET'])
def user(user_id):
    abort_if_user_doesnt_exist(user_id)
    return json.dumps(USERS[user_id])

# ListaVuelos
#   Muestra la lista completa de vuelos y permite borrar un vuelo
@app.route('/vuelos', methods=['GET'])
def vuelos():
    return json.dumps(VUELOS)

# Vuelos
#   Muestra un vuelo por su id
@app.route('/vuelo/<string:vuelo_id>', methods=['GET'])
def vuelo(vuelo_id):
    return json.dumps('VUELO')

# Vuelos
#   Muestra un vuelo por su id
@app.route('/aeropuerto/crear', methods=['POST'])
def aeropuerto():
    aeroPuertos.show()
    # aeroPuertos.append(id, nombre, pais, contra)
    return json.dumps('posted', 201)

# @app.route('/aeropuertos', methods=['GET'])
def aeropuertos():
    res = aeroPuertos.show()
    return json.dumps(res)

if __name__ == '__main__':
	app.run(
        # host="0.0.0.0",
        # port=int("5000")
        debug=True
  )