import json, random
from flask import Flask, request, abort, render_template, json, jsonify
from ListaDobleAirport import DoubleListAirport
from arbolAVLVuelos import AVLTree

app = Flask(__name__)

# lista doble Aeropuertos
aeroPuertos = DoubleListAirport()
# Arbol de Vuelos
avlVuelos = AVLTree()

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
    res=[]
    avlVuelos.inorder(avlVuelos.rootNode, res)
    return json.dumps(res)

@app.route('/vuelo/id', methods=['POST'])
def vuelosId():
    id_fly = request.form['id_fly']
    res = avlVuelos.searchItem(id_fly)
    return json.dumps(res)

#   Muestra un vuelo por su id
@app.route('/vuelo/crear', methods=['POST'])
def vuelo():
    id_fly = request.form['id_fly']
    origin = request.form['origin']
    destiny = request.form['destiny']
    date_out = request.form['date_out']
    date_in = request.form['date_in']
    price_fc = request.form['price_fc']
    price_tc = request.form['price_tc']
    price_ec = request.form['price_ec']
    amount_fc = request.form['amount_fc']
    amount_tc = request.form['amount_tc']
    amount_ec = request.form['amount_ec']
    state = request.form['state']
    res = avlVuelos.insert(id_fly, origin, destiny, date_out, date_in, price_fc, price_tc, price_ec, amount_fc, amount_tc, amount_ec, state)
    return json.dumps({'created':res}), 200

# Actualiza la informacion de un vuelo
@app.route('/vuelo/actualizar', methods=['POST'])
def vueloActualizar():
    id_fly = request.form['id_fly']
    date_out = request.form['date_out']
    date_in = request.form['date_in']
    price_fc = request.form['price_fc']
    price_tc = request.form['price_tc']
    price_ec = request.form['price_ec']
    amount_fc = request.form['amount_fc']
    amount_tc = request.form['amount_tc']
    amount_ec = request.form['amount_ec']
    state = request.form['state']
    res = avlVuelos.update(id_fly, date_out, date_in, price_fc, price_tc, price_ec, amount_fc, amount_tc, amount_ec, state)
    return json.dumps({'updated':res}), 200

# Eliminar la informacion de un vuelo
@app.route('/vuelo/eliminar', methods=['POST'])
def vueloEliminar():
    id_fly = request.form['id_fly']
    state = request.form['state']
    print(state)
    if state != 'En Vuelo':
        avlVuelos.remove(id_fly)
        res = True
    else:
        res = False
    return json.dumps({'deleted':res}), 200

# <--- Aeropuertos --->
# Crea un nuevo aeropuerto
@app.route('/aeropuerto/crear', methods=['POST'])
def aeropuerto():
    id = request.form['id']
    nombre = request.form['nombre']
    pais = request.form['pais']
    contra = request.form['contra']
    res = aeroPuertos.append(id, nombre, pais, contra)
    return json.dumps({'created':res}), 200

# Muestra la lista completa de aeropuertos
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